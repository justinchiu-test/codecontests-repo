#!/usr/bin/env python3

import sys
sys.path.append('..')
from library import zfunction, rlinput

a = rlinput()
n, a, b = a[0], a[1], a[2]
s = input()

dp = [0] * n
dp[0] = a

for i in range(1, n):
    t = s[:i + 1]
    dp[i] = dp[i - 1] + a
    
    q = zfunction(t[::-1])
    maxs = [0] * (i + 1)
    maxs[0] = q[i]
    
    for j in range(1, i):
        maxs[j] = max(maxs[j - 1], q[i - j])
    
    for j in range(i):
        if maxs[j] >= i - j:
            dp[i] = min(dp[i], dp[j] + b)

print(dp[-1])