#!/usr/bin/env python3

import sys
sys.path.append('..')
from library import iinput

a = input()
dp = [[0] * 10 for _ in range(len(a))]

# Initialize the first row
for i in range(10):
    dp[0][i] = 1
    
for i in range(len(a) - 1):
    for j in range(10):
        if dp[i][j] != 0:
            c = (int(a[i + 1]) + j) // 2
            d = (int(a[i + 1]) + j + 1) // 2
            if c != d:
                dp[i + 1][c] += dp[i][j]
                dp[i + 1][d] += dp[i][j]
            else:
                dp[i + 1][c] += dp[i][j]

s = sum(dp[-1])
t = 0

# Check if original number is in the set
c = int(a[0])
f = [a[0]]
for i in range(1, len(a)):
    d = (c + int(a[i])) // 2
    e = (c + int(a[i]) + 1) // 2
    if int(a[i]) == d:
        f.append(a[i])
        c = d
    elif int(a[i]) == e:
        f.append(a[i])
        c = e
    else:
        break

if "".join(f) == a:
    t = 1
    
print(s - t)