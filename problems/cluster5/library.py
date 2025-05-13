"""
Library file for cluster5.
This contains shared code that can be imported by problems in this cluster.
"""
import os
import sys
from io import BytesIO, IOBase
from collections import defaultdict, deque, Counter
from functools import reduce, lru_cache
from itertools import accumulate, combinations
from math import gcd

# Constants
MOD = 10**9 + 7
INF = float('inf')
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

# Fast I/O
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)

class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")

def setup_fast_io():
    """Set up fast I/O for competitive programming."""
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    return lambda: sys.stdin.readline().rstrip("\r\n")

# Input helpers
def iinput():
    """Read a single integer."""
    return int(input())

def tinput():
    """Read a space-separated string."""
    return input().split()

def rinput():
    """Read space-separated integers as a map object."""
    return map(int, tinput())

def rlinput():
    """Read space-separated integers as a list."""
    return list(rinput())

def multi_input(n, f=int):
    """Read n lines, each converted by function f."""
    return [f(input()) for _ in range(n)]

def char_to_idx(c):
    """Convert character to index (0-25 for a-z)."""
    return ord(c) - ord('a')

def idx_to_char(i):
    """Convert index to character (0-25 to a-z)."""
    return chr(i + ord('a'))

# String algorithms
def zfunction(s):
    """
    Z-function implementation for string matching.
    Returns an array where Z[i] is the length of the longest common
    prefix between s[i:] and s.
    """
    n = len(s)
    l, r = 0, 0
    Z = [0] * n
    for i in range(1, n):
        if i <= r:
            Z[i] = min(r - i + 1, Z[i - l])
        while i + Z[i] < n and s[Z[i]] == s[i + Z[i]]:
            Z[i] += 1
        if i + Z[i] - 1 > r:
            l, r = i, i + Z[i] - 1
    return Z

def prefix_function(s):
    """
    Prefix function (KMP) for string matching.
    Returns pi array where pi[i] is the length of the longest proper
    prefix of s[0:i+1] which is also a suffix of s[0:i+1].
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

def build_next_occurrences(s, alphabet=ALPHABET):
    """
    Build a next occurrence array for each character in the alphabet.
    next_occ[c][i] will be the next position where character c occurs after position i.
    If there's no occurrence, it will be len(s).
    
    Args:
        s: The input string
        alphabet: The alphabet to consider
        
    Returns:
        A list of lists where next_occ[ord(c) - ord('a')][i] is the next position of c after i.
    """
    n = len(s)
    next_occ = [[n] * (n + 1) for _ in range(len(alphabet))]
    
    for i in range(n - 1, -1, -1):
        c = char_to_idx(s[i])
        if 0 <= c < len(alphabet):
            for j in range(len(alphabet)):
                next_occ[j][i] = next_occ[j][i + 1]
            next_occ[c][i] = i
    
    return next_occ

def run_length_encode(s):
    """
    Run length encoding of a string.
    Returns a list of tuples (char, count).
    """
    if not s:
        return []
    result = []
    curr_char = s[0]
    curr_count = 1
    for i in range(1, len(s)):
        if s[i] == curr_char:
            curr_count += 1
        else:
            result.append((curr_char, curr_count))
            curr_char = s[i]
            curr_count = 1
    result.append((curr_char, curr_count))
    return result

def is_subsequence(s, t):
    """
    Check if s is a subsequence of t.
    """
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)

def find_all_occurences(pattern, text):
    """
    Find all occurrences of pattern in text.
    Returns a list of starting indices.
    """
    result = []
    z = zfunction(pattern + "#" + text)
    n = len(pattern)
    for i in range(n + 1, len(z)):
        if z[i] == n:
            result.append(i - n - 1)
    return result

def max_consecutive_chars(s):
    """
    Count maximum consecutive occurrences of each character.
    Returns a dictionary {char: max_consecutive_count}.
    """
    if not s:
        return {}
    
    counts = {ch: 0 for ch in set(s)}
    i = 0
    while i < len(s):
        j = i + 1
        while j < len(s) and s[i] == s[j]:
            j += 1
        counts[s[i]] = max(counts[s[i]], j - i)
        i = j
    return counts

# Segment tree operations
def build_segment_tree(arr):
    """Build a segment tree from an array."""
    n = len(arr)
    si = 1 << (n.bit_length() - (not n & (n - 1)))
    tree = [0] * (si << 1)
    for i in range(n):
        tree[si + i] = arr[i]
    for i in range(si - 1, 0, -1):
        tree[i] = tree[i << 1] + tree[i << 1 | 1]
    return tree, si

def update(tree, pos, diff, si):
    """Update a position in the segment tree by diff."""
    pos += si - 1
    while pos:
        tree[pos] += diff
        pos >>= 1

def query(tree, l, r, si):
    """Query the segment tree for the sum from l to r inclusive."""
    ans, l, r = 0, l + si - 1, r + si - 1
    while l < r:
        if l & 1:
            ans += tree[l]
            l += 1
        if not r & 1:
            ans += tree[r]
            r -= 1
        l, r = l >> 1, r >> 1
    return ans + (0 if l != r else tree[l])

# Math functions
def factors(n):
    """Get all factors of a number."""
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def pow_mod(x, n, mod=MOD):
    """Calculate (x^n) % mod efficiently."""
    result = 1
    while n > 0:
        if n & 1:
            result = (result * x) % mod
        x = (x * x) % mod
        n >>= 1
    return result

# Dynamic Programming Utilities
def lcs(a, b):
    """Find the longest common subsequence of two strings."""
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Reconstruct the LCS
    lcs_str = []
    i, j = n, m
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            lcs_str.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(lcs_str)), dp[n][m]

def edit_distance(a, b):
    """Calculate the edit distance (Levenshtein distance) between two strings."""
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],      # Delete
                                   dp[i][j - 1],      # Insert
                                   dp[i - 1][j - 1])  # Replace
    
    return dp[n][m]

# Advanced DP utilities for strings
def can_interleave(s1, s2, s3):
    """
    Check if s3 is an interleaving of s1 and s2.
    An interleaving means s3 can be formed by interleaving the characters of s1 and s2 
    while maintaining the relative order of characters in both.
    """
    if len(s1) + len(s2) != len(s3):
        return False
        
    # Create a 2D DP array dp[i][j] which is True if s3[0...i+j-1]
    # is an interleaving of s1[0...i-1] and s2[0...j-1]
    dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    
    # Initialize base case
    dp[0][0] = True
    
    # Fill the dp array
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i > 0 and s1[i-1] == s3[i+j-1]:
                dp[i][j] |= dp[i-1][j]
            if j > 0 and s2[j-1] == s3[i+j-1]:
                dp[i][j] |= dp[i][j-1]
    
    return dp[len(s1)][len(s2)]

def longest_palindromic_substring(s):
    """
    Find the longest palindromic substring in string s.
    Uses dynamic programming. Returns the palindrome string and its length.
    """
    n = len(s)
    if n <= 1:
        return s, n
        
    # dp[i][j] is True if s[i:j+1] is a palindrome
    dp = [[False] * n for _ in range(n)]
    
    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True
        
    start, max_len = 0, 1
    
    # Check for substrings of length 2
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            start, max_len = i, 2
    
    # Check for substrings of length > 2
    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i + length - 1  # ending index
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                start, max_len = i, length
    
    return s[start:start+max_len], max_len

def dp_subsequence_count(s, t, mod=MOD):
    """
    Count the number of distinct subsequences of s that equals t.
    Returns count % mod.
    """
    n, m = len(s), len(t)
    # dp[i][j] = number of distinct subsequences of s[0:i] that equals t[0:j]
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    # Empty string is a subsequence of any string once
    for i in range(n+1):
        dp[i][0] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % mod
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[n][m]

# String compression utilities
def compress_string(s):
    """
    Compress a string by replacing consecutive repeated characters with count+char.
    e.g., 'aabccc' -> '2a1b3c'
    """
    if not s:
        return ""
    
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(str(count) + s[i-1])
            count = 1
    
    # Add the last group
    result.append(str(count) + s[-1])
    return ''.join(result)

def count_subsequences(s, pattern):
    """
    Count the number of times pattern appears as a subsequence in s.
    
    For example:
    count_subsequences("banana", "ban") would count how many ways
    "ban" appears as a subsequence in "banana".
    """
    n, m = len(s), len(pattern)
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    # Base case: empty pattern occurs once in any string
    for i in range(n+1):
        dp[i][0] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            # If current characters match, we have two choices:
            # 1. Include current char in the match: dp[i-1][j-1]
            # 2. Skip current char and look for pattern in previous: dp[i-1][j]
            if s[i-1] == pattern[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[n][m]

def is_disjoint_subsequence_possible(s, subsequences):
    """
    Check if multiple subsequences can be extracted from s in a disjoint manner.
    
    Args:
        s: The main string to extract from
        subsequences: List of strings to extract as disjoint subsequences
        
    Returns:
        Boolean indicating if it's possible
    """
    @lru_cache(maxsize=None)
    def can_extract(i, masks):
        # Base case - all subsequences found
        if masks == (1 << len(subsequences)) - 1:
            return True
            
        # Base case - end of string but not all subsequences found
        if i >= len(s):
            return False
            
        # Skip current character
        if can_extract(i+1, masks):
            return True
            
        # Try to use current character for each subsequence
        for j in range(len(subsequences)):
            # If subsequence j is not yet matched and matches at current position
            if not (masks & (1 << j)):
                subseq = subsequences[j]
                k = 0
                pos = i
                
                # Try to match subsequence j from position i
                while k < len(subseq) and pos < len(s):
                    if s[pos] == subseq[k]:
                        k += 1
                    pos += 1
                    
                # If subsequence j can be matched
                if k == len(subseq):
                    if can_extract(pos, masks | (1 << j)):
                        return True
        
        return False
    
    return can_extract(0, 0)

# LRU Cache decorator for memoization
def memoize(func):
    """Decorator to memoize a function with cache."""
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper