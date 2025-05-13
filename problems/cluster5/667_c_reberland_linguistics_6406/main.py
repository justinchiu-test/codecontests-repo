#!/usr/bin/env python3

from library import read_str, create_array

def reberland_linguistics():
    """
    Solution for the Reberland Linguistics problem.

    The problem asks to find all distinct strings of length 2 or 3,
    which can be suffixes of a given word according to Reberland language rules.

    A word in Reberland language consists of a root (>= 5 characters)
    and suffixes (length 2 or 3). The same suffix cannot be appended twice in a row.
    """
    # Read the input word
    word = read_str()

    # Remove the root (first 5 characters) and reverse for easier processing
    # We reverse the string because we'll be working from the end of the word
    s = word[5:][::-1]
    n = len(s)

    # If the word is too short (only contains the root), no suffixes are possible
    if n == 0:
        print(0)
        return

    # Set to store unique suffixes
    suffixes = set()

    # Dynamic programming arrays to track if we can form a valid suffix
    # can2[i] = 1 if we can form a valid suffix of length 2 ending at position i
    # can3[i] = 1 if we can form a valid suffix of length 3 ending at position i
    can2 = create_array(n + 1)
    can3 = create_array(n + 1)

    # Initialize base cases
    if n >= 2:
        # First suffix of length 2
        suffixes.add(s[0:2][::-1])
        can2[2] = 1

    if n >= 3:
        # First suffix of length 3
        suffixes.add(s[0:3][::-1])
        can3[3] = 1

    if n >= 4 and s[0:2] != s[2:4]:
        # Second suffix of length 2 (if not the same as the first one)
        suffixes.add(s[2:4][::-1])
        can2[4] = 1

    if n >= 5:
        # Add possible suffixes at position 5
        suffixes.add(s[2:5][::-1])  # Length 3 suffix
        suffixes.add(s[3:5][::-1])  # Length 2 suffix
        can2[5] = 1
        can3[5] = 1

    # Dynamic programming to find all possible suffixes
    for i in range(6, n + 1):
        # If we can form a suffix of length 2 ending at position i-3,
        # we can append a suffix of length 3 ending at position i
        if can2[i - 3]:
            suffixes.add(s[i - 3:i][::-1])
            can3[i] = 1

        # If we can form a suffix of length 2 ending at position i-2,
        # we can append a suffix of length 2 ending at position i
        # (if it's not the same as the previous one)
        if can2[i - 2] and s[i - 2:i] != s[i - 4:i - 2]:
            suffixes.add(s[i - 2:i][::-1])
            can2[i] = 1

        # If we can form a suffix of length 3 ending at position i-2,
        # we can append a suffix of length 2 ending at position i
        if can3[i - 2]:
            suffixes.add(s[i - 2:i][::-1])
            can2[i] = 1

        # If we can form a suffix of length 3 ending at position i-3,
        # we can append a suffix of length 3 ending at position i
        # (if it's not the same as the previous one)
        if can3[i - 3] and s[i - 3:i] != s[i - 6:i - 3]:
            suffixes.add(s[i - 3:i][::-1])
            can3[i] = 1

    # Print the result in lexicographical order
    print(len(suffixes))
    for suffix in sorted(list(suffixes)):
        print(suffix)

if __name__ == "__main__":
    reberland_linguistics()