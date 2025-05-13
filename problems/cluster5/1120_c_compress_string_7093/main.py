#!/usr/bin/env python3
from library import na, input, zf
# read parameters: n words, cost of append, cost of copy
n, a, b = na()
# read the string
s = input()
dp=[0 for i in range(n)]
dp[0]=a
for i in range(1,n):
    t=s[:i+1]
    dp[i]=dp[i-1]+a
    q=zf(t[::-1])
    maxs=[0 for j in range(i+1)]
    maxs[0]=q[i]
    for j in range(1,i):
        maxs[j]=max(maxs[j-1],q[i-j])
    for j in range(i):
        if maxs[j]>=i-j:
            dp[i]=min(dp[i],dp[j]+b)
print(dp[len(dp)-1])
