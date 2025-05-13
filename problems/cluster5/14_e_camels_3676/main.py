#!/usr/bin/env python3

from library import read_int_tuple, create_dp_table_3d

def camels():
    """
    Solution for the Camels problem.

    The task is to count the number of polylines that can represent camels with t humps,
    where each polyline consists of n vertices with specific properties.
    """
    # Read input
    n, t = read_int_tuple()

    # Create DP table
    # dp[i][j][k] = number of ways to construct a polyline up to vertex i
    # with j humps and valleys combined, ending at height k
    dp = create_dp_table_3d(n, 2 * t + 1, 5)

    # Initialize base case:
    # At vertex 0, we have 0 humps and valleys, and can start at any height from 1 to 4
    dp[0][0] = [0] + [1] * 4  # Height 0 is not used

    # Fill DP table
    for i in range(n - 1):
        for j in range(min(2 * t, i + 1)):
            if (j % 2) == 0:
                # For even j (we need to create a hump or continue ascending)
                for current_height in range(1, 4):  # Current heights 1, 2, 3
                    for next_height in range(current_height + 1, 5):  # Next heights must be higher
                        # Continue ascending path (//)
                        dp[i + 1][j][next_height] += dp[i][j][current_height]

                        # Create a hump (/\)
                        dp[i + 1][j + 1][next_height] += dp[i][j][current_height]
            else:
                # For odd j (we need to create a valley or continue descending)
                for current_height in range(4, 1, -1):  # Current heights 4, 3, 2
                    for next_height in range(current_height - 1, 0, -1):  # Next heights must be lower
                        # Continue descending path (\\)
                        dp[i + 1][j][next_height] += dp[i][j][current_height]

                        # Create a valley (\/)
                        dp[i + 1][j + 1][next_height] += dp[i][j][current_height]

    # Sum all possibilities at the final vertex with exactly 2*t humps and valleys
    # (t humps and t-1 valleys)
    return sum(dp[n-1][2*t])

print(camels())
