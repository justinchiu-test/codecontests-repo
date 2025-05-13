#!/usr/bin/env python3

from library import read_ints, mod_add

def vasya_and_array():
    n, k, leng = read_ints()
    if leng == 1:
        return 0
    
    a = read_ints()
    
    # Custom modulus for this problem
    mod = 998244353
    
    # Make array 1-indexed for easier DP
    a.insert(0, 0)
    
    # dp[i][j] = number of ways to assign values up to position i with last value j
    dp = [[0 for x in range(k + 1)] for y in range(n + 1)]
    
    # Sum of dp values for each position
    sumdp = [0 for _ in range(n + 1)]
    sumdp[0] = 1
    
    # Count of consecutive elements with value j
    count = [0 for _ in range(k + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if a[i] == -1 or a[i] == j:
                # Valid assignment
                dp[i][j] = sumdp[i - 1]
                count[j] += 1
                
                # Check if we're exceeding the allowed length of consecutive values
                if count[j] >= leng:
                    dp[i][j] -= (sumdp[i - leng] - dp[i - leng][j])
                
                dp[i][j] %= mod
                
                # Update sum of dp values for this position
                sumdp[i] = mod_add(sumdp[i], dp[i][j], mod)
            else:
                # Reset count for this value
                count[j] = 0
    
    return sumdp[n]

print(vasya_and_array())