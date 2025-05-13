#!/usr/bin/env python3

import sys
from library import read_int_tuple, mod_add

# Use fast input
input = sys.stdin.readline

# Custom modulus for this problem
MOD = 998244353

# Read input
n, m = read_int_tuple()
A = [0] + sorted(list(map(int, input().split())))

# Initialize result
ans = 0

# DP table: f[i][j] = number of ways to choose i elements ending with A[j]
# with difference at least x
f = [[0] * (n + 10) for _ in range(m + 10)]

# Iterate over all possible minimum differences
for x in range(1, (A[n] - A[1]) // (m - 1) + 1):
    # Base case: 1 element
    for i in range(1, n + 1):
        f[1][i] = 1
    
    # Fill DP table for each subsequence length
    for i in range(2, m + 1):
        sum_prev = 0
        pre = 1
        
        for j in range(1, n + 1):
            # Find all previous elements that satisfy the minimum difference
            while pre <= n and A[pre] + x <= A[j]:
                sum_prev = (sum_prev + f[i - 1][pre]) % MOD
                pre += 1
            
            f[i][j] = sum_prev
    
    # Add up all ways to form a beautiful array of length m
    for i in range(1, n + 1):
        ans = mod_add(ans, f[m][i], MOD)

print(ans)