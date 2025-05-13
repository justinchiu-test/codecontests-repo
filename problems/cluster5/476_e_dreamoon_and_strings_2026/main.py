#!/usr/bin/env python3

from library import read_str, create_dp_table

def dreamoon_and_strings():
    """
    Solution for the Dreamoon and Strings problem.

    The problem asks to calculate the maximum number of non-overlapping occurrences
    of a pattern p in string s after removing exactly x characters, for all x from 0 to |s|.
    """
    # Read input strings
    s = read_str()
    p = read_str()

    # Get lengths
    n = len(s) + 1  # Adding 1 for 1-indexing
    m = len(p)

    # Create DP table:
    # dp[i][j] = maximum number of non-overlapping occurrences of pattern p
    # in the prefix of s of length i after removing j characters
    dp = create_dp_table(n, n)

    # Process each position in the string s
    for pos in range(1, n):
        # Try to match the pattern p ending at position pos
        i, j = pos, m

        # Backtrack from the current position trying to match pattern p
        while i > 0 and j > 0:
            # If characters match, move to previous characters in both strings
            # Otherwise, only move in the original string
            if s[i - 1] == p[j - 1]:
                j -= 1
            i -= 1

        # If we've matched the entire pattern
        if j == 0:
            # i now points to the position before the start of pattern
            # Calculate how many characters were removed
            removed_chars = pos - i - m

            # For all possible previous states, update with a new pattern match
            for prev_removed in range(i + 1):
                # Current removed = previous removed + chars removed for this match
                dp[pos][prev_removed + removed_chars] = dp[i][prev_removed] + 1

        # Propagate best results from previous position
        for y in range(pos):
            dp[pos][y] = max(dp[pos][y], dp[pos - 1][y])

    # The last row contains the answers for all x from 0 to |s|
    return dp[-1]

print(*dreamoon_and_strings())