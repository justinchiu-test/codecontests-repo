#!/usr/bin/env python3

from library import read_str, create_dp_table, mod_add, MOD_998_244_353

def magic_spell():
    """
    Kaavi's Magic Spell problem solution.

    We use dynamic programming to calculate the number of ways to form magic spells.
    dp[l][r] = number of ways to form substring T[l:r] using the operations.
    """
    # Read input strings
    source_string = read_str()
    target_prefix = read_str()

    # Initialize variables
    target_length = len(target_prefix)
    source_length = len(source_string)

    # Create DP table
    dp = create_dp_table(source_length + 1, source_length + 1)

    # Fill DP table
    for length in range(1, source_length + 1):
        for left in range(source_length + 1):
            right = left + length

            # Skip if out of bounds
            if right > source_length:
                break

            # Base case: length 1
            if length == 1:
                # Either left is beyond target prefix length (so any char is okay),
                # or the first char of source matches the char at position l in target
                if left >= target_length or source_string[0] == target_prefix[left]:
                    dp[left][right] = 2  # Can add to front or back
                else:
                    dp[left][right] = 0  # Can't form valid prefix
                continue

            # Recursive case: add to front of A
            if left >= target_length or source_string[length - 1] == target_prefix[left]:
                dp[left][right] = mod_add(dp[left][right], dp[left + 1][right], MOD_998_244_353)

            # Recursive case: add to back of A
            if right - 1 >= target_length or source_string[length - 1] == target_prefix[right - 1]:
                dp[left][right] = mod_add(dp[left][right], dp[left][right - 1], MOD_998_244_353)

    # Sum up all possibilities for magic spells (where formed string has target as prefix)
    total_ways = 0
    for i in range(target_length, source_length + 1):
        total_ways = mod_add(total_ways, dp[0][i], MOD_998_244_353)

    return total_ways

print(magic_spell())