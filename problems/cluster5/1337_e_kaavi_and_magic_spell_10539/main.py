#!/usr/bin/env python3

import sys
sys.path.append('..')
from library import MOD

# In this problem, MOD is 998244353 not the standard 10^9+7
MOD = 998244353

s = input().strip()
t = input().strip()

n = len(s)
r_lim = len(t)
dp = [[0] * (n + 1) for i in range(n + 1)]

# Dynamic programming approach to count possible operation sequences
for length in range(1, n + 1):
    for l in range(n + 1):
        r = l + length
        if r > n:
            break
            
        # Base case - length 1
        if length == 1:
            if l >= r_lim or s[0] == t[l]:
                dp[l][r] = 2  # Two ways - add at front or back
            else:
                dp[l][r] = 0
            continue

        # Recursive case - add at front
        if l >= r_lim or s[length - 1] == t[l]:
            dp[l][r] += dp[l + 1][r]
            dp[l][r] %= MOD
            
        # Recursive case - add at back
        if r - 1 >= r_lim or s[length - 1] == t[r - 1]:
            dp[l][r] += dp[l][r - 1]
            dp[l][r] %= MOD

# Sum up all possibilities where the prefix T is formed
ans = 0
for i in range(r_lim, n + 1):
    ans += dp[0][i]
    ans %= MOD

print(ans)