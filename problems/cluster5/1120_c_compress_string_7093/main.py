#!/usr/bin/env python3

from library import read_ints, z_algorithm

n, a, b = read_ints()
s = input()

dp = [0] * n
dp[0] = a

for i in range(1, n):
    t = s[:i+1]
    dp[i] = dp[i-1] + a
    
    # Use z_algorithm from the library
    q = z_algorithm(t[::-1])
    
    maxs = [0] * (i+1)
    maxs[0] = q[i]
    
    for j in range(1, i):
        maxs[j] = max(maxs[j-1], q[i-j])
    
    for j in range(i):
        if maxs[j] >= i-j:
            dp[i] = min(dp[i], dp[j] + b)

print(dp[-1])