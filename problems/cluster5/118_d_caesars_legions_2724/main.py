#!/usr/bin/env python3

from library import read_int_tuple, create_dp_table

def main():
    n1, n2, k1, k2 = read_int_tuple()
    k1 = min(k1, n1)
    k2 = min(k2, n2)
    
    # dp[i][j][0] = number of ways to form i footmen and j horsemen ending with footman
    # dp[i][j][1] = number of ways to form i footmen and j horsemen ending with horseman
    dp = [create_dp_table(n2 + 1, 2) for _ in range(n1 + 1)]
    
    # Initialize base cases
    for i in range(1, k1 + 1):
        dp[i][0][0] = 1  # i footmen, 0 horsemen, ending with footman
    
    for i in range(1, k2 + 1):
        dp[0][i][1] = 1  # 0 footmen, i horsemen, ending with horseman
    
    MOD = 100000000
    
    # Fill the DP table
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            # Ways to add a footman at the end (need to check we don't exceed k1 consecutive footmen)
            dp[i][j][0] = sum(dp[k][j][1] for k in range(max(0, i - k1), i)) % MOD
            
            # Ways to add a horseman at the end (need to check we don't exceed k2 consecutive horsemen)
            dp[i][j][1] = sum(dp[i][k][0] for k in range(max(0, j - k2), j)) % MOD
    
    # Final answer is the sum of ways ending with either footman or horseman
    print(sum(dp[n1][n2]) % MOD)

if __name__ == "__main__":
    main()