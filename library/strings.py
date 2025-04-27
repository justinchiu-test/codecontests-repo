"""
String algorithms for competitive programming.
"""

from collections import Counter
from typing import Dict, List, Tuple


def z_function(s: str) -> List[int]:
    """Compute Z-array for a string.

    Z[i] = the length of the longest substring starting at i
           which is also a prefix of s.

    Args:
        s: The input string

    Returns:
        The Z-array
    """
    n = len(s)
    z = [0] * n

    # Initial window
    l, r = 0, 0

    for i in range(1, n):
        # Check if i is within the current window
        if i <= r:
            # Use the value computed before, but limit it to the window size
            z[i] = min(r - i + 1, z[i - l])

        # Try to extend the match
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        # Extend the window if needed
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1

    return z


def kmp_prefix_function(s: str) -> List[int]:
    """Compute the prefix function for KMP algorithm.

    Args:
        s: The input string

    Returns:
        The prefix function array, where pi[i] is the length of the longest proper
        prefix of s[0:i+1] which is also a suffix of s[0:i+1]
    """
    n = len(s)
    pi = [0] * n

    for i in range(1, n):
        j = pi[i - 1]

        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]

        if s[i] == s[j]:
            j += 1

        pi[i] = j

    return pi


def string_matching(text: str, pattern: str) -> List[int]:
    """Find all occurrences of a pattern in a text using KMP algorithm.

    Args:
        text: The text to search in
        pattern: The pattern to search for

    Returns:
        List of starting positions of matches
    """
    combined = pattern + "#" + text
    pi = kmp_prefix_function(combined)

    matches = []
    pattern_len = len(pattern)

    for i in range(pattern_len + 1, len(combined)):
        if pi[i] == pattern_len:
            matches.append(i - 2 * pattern_len)

    return matches


def manacher(s: str) -> List[int]:
    """Compute the lengths of the longest palindromic substring centered at each position.

    Args:
        s: The input string

    Returns:
        List p where p[i] is the half-length of the longest palindromic substring centered at i
    """
    # Preprocess string to handle even-length palindromes
    t = "#" + "#".join(s) + "#"
    n = len(t)
    p = [0] * n

    c, r = 0, 0  # Center and right boundary of the rightmost palindrome

    for i in range(n):
        # Check if i is within the rightmost palindrome
        if i < r:
            p[i] = min(r - i, p[2 * c - i])

        # Try to extend the palindrome
        while (
            i - p[i] - 1 >= 0
            and i + p[i] + 1 < n
            and t[i - p[i] - 1] == t[i + p[i] + 1]
        ):
            p[i] += 1

        # Update center and right boundary if needed
        if i + p[i] > r:
            c, r = i, i + p[i]

    return p


def longest_palindrome(s: str) -> str:
    """Find the longest palindromic substring in a string.

    Args:
        s: The input string

    Returns:
        The longest palindromic substring
    """
    t = "#" + "#".join(s) + "#"
    p = manacher(t)

    max_len = max(p)
    center = p.index(max_len)

    # Extract the palindrome from the expanded string
    expanded_start = center - max_len
    expanded_end = center + max_len

    # Convert positions in the expanded string to the original string
    # Remove the added '#' characters
    palindrome = "".join(
        t[i] for i in range(expanded_start, expanded_end + 1) if t[i] != "#"
    )

    return palindrome


def rabin_karp(
    text: str, pattern: str, base: int = 31, mod: int = 10**9 + 9
) -> List[int]:
    """Find all occurrences of a pattern in a text using Rabin-Karp algorithm.

    Args:
        text: The text to search in
        pattern: The pattern to search for
        base: The base for the hash function
        mod: The modulo for the hash function

    Returns:
        List of starting positions of matches
    """
    n, m = len(text), len(pattern)

    if m > n:
        return []

    # Compute base powers
    base_powers = [1]
    for i in range(m):
        base_powers.append((base_powers[-1] * base) % mod)

    # Compute pattern hash
    pattern_hash = 0
    for i in range(m):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % mod

    # Compute text hashes
    text_hashes = [0]
    for i in range(n):
        text_hashes.append((text_hashes[-1] * base + ord(text[i])) % mod)

    # Find matches
    matches = []

    for i in range(n - m + 1):
        # Compute hash of the current substring
        curr_hash = (text_hashes[i + m] - text_hashes[i] * base_powers[m]) % mod

        if curr_hash == pattern_hash:
            # Verify match character by character to avoid hash collisions
            if text[i : i + m] == pattern:
                matches.append(i)

    return matches


def suffix_array(s: str) -> Tuple[List[int], List[int]]:
    """Compute the suffix array and LCP array for a string.

    Args:
        s: The input string

    Returns:
        Tuple (sa, lcp) where:
        - sa is the suffix array (indices sorted by lexicographical order of suffixes)
        - lcp is the LCP array (lcp[i] = length of the longest common prefix between
          suffixes at sa[i] and sa[i-1])
    """
    n = len(s)

    # Initial ranking by characters
    order = [0] * n
    equiv_classes = [0] * n

    # Count sort for characters
    count = Counter(s)
    char_order = sorted(count.keys())

    for i, c in enumerate(char_order):
        count[c] = i

    for i in range(n):
        equiv_classes[i] = count[s[i]]

    # Sort suffixes by first character
    order = sorted(range(n), key=lambda i: equiv_classes[i])

    # Iterate through powers of 2 (length of substrings to compare)
    length = 1
    while length < n:
        # Sort by second half
        count = [0] * n
        new_order = [0] * n

        for i in range(n):
            count[equiv_classes[i]] += 1

        for i in range(1, n):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            start = (order[i] - length) % n
            cl = equiv_classes[start]
            count[cl] -= 1
            new_order[count[cl]] = start

        order = new_order

        # Update equivalence classes
        new_classes = [0] * n
        new_classes[order[0]] = 0

        for i in range(1, n):
            curr = order[i]
            prev = order[i - 1]
            mid = (curr + length) % n
            midPrev = (prev + length) % n

            if (
                equiv_classes[curr] != equiv_classes[prev]
                or equiv_classes[mid] != equiv_classes[midPrev]
            ):
                new_classes[curr] = new_classes[prev] + 1
            else:
                new_classes[curr] = new_classes[prev]

        equiv_classes = new_classes
        length *= 2

    # Calculate LCP array using Kasai's algorithm
    rank = [0] * n
    lcp = [0] * n

    for i in range(n):
        rank[order[i]] = i

    k = 0
    for i in range(n):
        if rank[i] == n - 1:
            k = 0
            continue

        j = order[rank[i] + 1]

        while i + k < n and j + k < n and s[i + k] == s[j + k]:
            k += 1

        lcp[rank[i]] = k

        if k > 0:
            k -= 1

    return order, lcp


def trie_build(words: List[str]) -> Dict:
    """Build a trie from a list of words.

    Args:
        words: List of words to add to the trie

    Returns:
        The root node of the trie
    """
    trie = {}

    for word in words:
        node = trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["$"] = True  # Mark the end of a word

    return trie


def trie_search(trie: Dict, word: str) -> bool:
    """Check if a word exists in the trie.

    Args:
        trie: The trie
        word: The word to search for

    Returns:
        True if the word exists in the trie, False otherwise
    """
    node = trie

    for char in word:
        if char not in node:
            return False
        node = node[char]

    return "$" in node


def trie_prefix_search(trie: Dict, prefix: str) -> List[str]:
    """Find all words in the trie with a given prefix.

    Args:
        trie: The trie
        prefix: The prefix to search for

    Returns:
        List of words with the given prefix
    """
    node = trie

    for char in prefix:
        if char not in node:
            return []
        node = node[char]

    words = []

    def dfs(node: Dict, curr: str) -> None:
        if "$" in node:
            words.append(prefix + curr)

        for char in sorted(node.keys()):
            if char != "$":
                dfs(node[char], curr + char)

    dfs(node, "")

    return words
