#!/usr/bin/env python3

from library import read_str, create_dp_table_3d, mod_add, MOD_998_244_353

def chaotic_merge():
    """
    Solution for the Chaotic Merge problem.

    The problem asks for the number of different merging sequences that produce
    chaotic merges (no two consecutive characters are the same) for all possible
    substring pairs from two strings.
    """
    # Read input strings
    string_x = read_str()
    string_y = read_str()

    # Convert characters to indices (0-25) for easier manipulation
    chars_x = [ord(ch) - ord('a') for ch in string_x]
    chars_y = [ord(ch) - ord('a') for ch in string_y]

    m, n = len(chars_x), len(chars_y)

    # Calculate the maximum length of chaotic subsequence starting at each position
    # v1[i] = maximum length of chaotic subsequence starting at position i in string_x
    # v2[j] = maximum length of chaotic subsequence starting at position j in string_y
    v1 = [1] * (m + 1)
    v2 = [1] * (n + 1)

    # Calculate v1 from right to left
    for i in range(m - 2, -1, -1):
        if chars_x[i] != chars_x[i + 1]:
            v1[i] += v1[i + 1]

    # Calculate v2 from right to left
    for i in range(n - 2, -1, -1):
        if chars_y[i] != chars_y[i + 1]:
            v2[i] += v2[i + 1]

    # dp[i][j][k] = number of different merging sequences that produce chaotic merges
    # where:
    # - i is the current position in string_x
    # - j is the current position in string_y
    # - k is the last character used (0-25) or 26 for the start
    dp = create_dp_table_3d(m + 1, n + 1, 27)

    # Fill DP table from bottom-right to top-left
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            for k in range(27):
                if chars_x[i] == k:
                    # If current char in x equals k, it creates same consecutive chars
                    # Only consider if the current char in y is different
                    if chars_y[j] != k:
                        dp[i][j][k] = mod_add(dp[i][j + 1][chars_y[j]], v1[i], MOD_998_244_353)
                elif chars_y[j] == k:
                    # If current char in y equals k, similar case
                    dp[i][j][k] = mod_add(dp[i + 1][j][chars_x[i]], v2[j], MOD_998_244_353)
                else:
                    # Both current chars are different from k
                    # We can either take from x or y
                    dp[i][j][k] = mod_add(
                        mod_add(dp[i + 1][j][chars_x[i]], dp[i][j + 1][chars_y[j]], MOD_998_244_353),
                        (chars_x[i] != chars_y[j]) * (v2[j] + v1[i]),
                        MOD_998_244_353
                    )

    # Sum up all possibilities for all substrings
    total_ways = 0
    for i in range(m):
        for j in range(n):
            total_ways = mod_add(total_ways, dp[i][j][26], MOD_998_244_353)

    return total_ways

print(chaotic_merge())
