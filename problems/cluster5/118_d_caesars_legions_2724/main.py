#!/usr/bin/env python3

from library import read_int_tuple, mod_add, initialize_dp_table

# Custom modulus for this problem
MOD = 100000000

def main():
    # Read input
    n1, n2, k1, k2 = read_int_tuple()
    
    # Limit consecutive soldiers to minimum of constraint and total soldiers
    k1 = min(k1, n1)
    k2 = min(k2, n2)
    
    # Initialize DP table: dp[i][j][t] = ways to arrange i footmen, j horsemen ending with type t
    # where t=0 means ending with footman, t=1 means ending with horseman
    dp = initialize_dp_table([n1 + 1, n2 + 1, 2], 0)
    
    # Base cases: ways to arrange only footmen or only horsemen
    for i in range(1, k1 + 1):
        dp[i][0][0] = 1  # i footmen, 0 horsemen, ending with footman
    for i in range(1, k2 + 1):
        dp[0][i][1] = 1  # 0 footmen, i horsemen, ending with horseman
    
    # Fill DP table
    for i in range(n1 + 1):
        for j in range(n2 + 1):
            # Skip the base cases we already set
            if i == 0 or j == 0:
                continue
                
            # Ways to end with a footman (type 0)
            for k in range(max(0, i - k1), i):
                dp[i][j][0] = mod_add(dp[i][j][0], dp[k][j][1], MOD)
            
            # Ways to end with a horseman (type 1)
            for k in range(max(0, j - k2), j):
                dp[i][j][1] = mod_add(dp[i][j][1], dp[i][k][0], MOD)
    
    # Sum the total ways to arrange n1 footmen and n2 horsemen
    result = mod_add(dp[n1][n2][0], dp[n1][n2][1], MOD)
    return result

if __name__ == "__main__":
    print(main())