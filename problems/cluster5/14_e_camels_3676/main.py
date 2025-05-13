#!/usr/bin/env python3

from library import read_int_tuple, initialize_dp_table

def main():
    # Read input
    n, t = read_int_tuple()
    
    # Initialize DP table
    # dp[i][j][k] = ways to place camel at position i, with j turns, at height k
    dp = initialize_dp_table([n, 2 * t + 1, 5], 0)
    
    # Base case: first camel can be at any of the 4 heights
    dp[0][0] = [0] + [1] * 4
    
    # Fill the DP table
    for i in range(n - 1):
        for j in range(min(2 * t, i + 1)):
            if (j & 1) == 0:
                # Even number of turns - going up
                for k in range(1, 4):
                    for l in range(k + 1, 5):
                        # Continue going up (//)
                        dp[i + 1][j][l] += dp[i][j][k]
                        # Make a turn (/\)
                        dp[i + 1][j + 1][l] += dp[i][j][k]
            else:
                # Odd number of turns - going down
                for k in range(4, 1, -1):
                    for l in range(k - 1, 0, -1):
                        # Continue going down (\\)
                        dp[i + 1][j][l] += dp[i][j][k]
                        # Make a turn (\/)
                        dp[i + 1][j + 1][l] += dp[i][j][k]
    
    # Sum all ways to place n camels with exactly 2*t turns
    print(sum(dp[n - 1][2 * t]))

if __name__ == "__main__":
    main()