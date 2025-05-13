#!/usr/bin/env python3

from sys import path
path.append('..')
from library import read_str, init_dp_2d, MOD_2, setup_fast_io

setup_fast_io()

s = read_str()
t = read_str()

r_lim = len(t)
n = len(s)
dp = init_dp_2d(n + 1, n + 1)

# DP[l][r] = number of ways to make A a magic spell
# where l is the current position in prefix and r is position in suffix
for length in range(1, n + 1):
    for l in range(n + 1):
        r = l + length
        if r > n:
            break
        
        if length == 1:
            # Base case: single character
            if l >= r_lim or s[0] == t[l]:
                dp[l][r] = 2  # Two possible operations
            else:
                dp[l][r] = 0
            continue
        
        # Try adding to front of A
        if l >= r_lim or s[length - 1] == t[l]:
            dp[l][r] += dp[l + 1][r]
            dp[l][r] %= MOD_2
        
        # Try adding to back of A
        if r - 1 >= r_lim or s[length - 1] == t[r - 1]:
            dp[l][r] += dp[l][r - 1]
            dp[l][r] %= MOD_2

# Sum up all ways to make A have prefix T
ans = 0
for i in range(r_lim, n + 1):
    ans += dp[0][i]
    ans %= MOD_2

print(ans)