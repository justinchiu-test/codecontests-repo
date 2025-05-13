#!/usr/bin/env python3

from sys import path
path.append('..')
from library import read_str, init_dp_3d, MOD_2

def main():
    # Read input strings and convert to character indices
    x = list(map(lambda ch: ord(ch) - 97, read_str()))
    y = list(map(lambda ch: ord(ch) - 97, read_str()))
    
    # Constants
    mod = 998244353  # Use this specific modulo
    m, n = len(x), len(y)
    
    # Precompute the lengths of different character sequences
    v1 = [1] * (m + 1)  # For string x
    v2 = [1] * (n + 1)  # For string y
    
    # Calculate the lengths of sequences with different consecutive characters
    for i in range(m - 2, -1, -1):
        if x[i] != x[i + 1]:
            v1[i] += v1[i + 1]
    
    for i in range(n - 2, -1, -1):
        if y[i] != y[i + 1]:
            v2[i] += v2[i + 1]
    
    # Initialize 3D DP array
    # dp[i][j][k] represents the number of ways to form a chaotic merge
    # starting at positions i in x, j in y, with last character k
    dp = init_dp_3d(m + 1, n + 1, 27)
    
    # Fill DP table from bottom-right to top-left
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            for k in range(27):
                if x[i] == k:
                    # If current character in x matches the last character k
                    if y[j] != k:
                        # And different from current character in y
                        dp[i][j][k] = (dp[i][j + 1][y[j]] + v1[i]) % mod
                elif y[j] == k:
                    # If current character in y matches the last character k
                    dp[i][j][k] = (dp[i + 1][j][x[i]] + v2[j]) % mod
                else:
                    # Neither matches k
                    dp[i][j][k] = (
                        dp[i + 1][j][x[i]] + 
                        dp[i][j + 1][y[j]] + 
                        (1 if x[i] != y[j] else 0) * (v2[j] + v1[i])
                    ) % mod
    
    # Calculate total ways by summing all starting positions with the special "26" character
    ans = 0
    for i in range(m):
        for j in range(n):
            ans = (ans + dp[i][j][26]) % mod
    
    print(ans)

if __name__ == "__main__":
    main()