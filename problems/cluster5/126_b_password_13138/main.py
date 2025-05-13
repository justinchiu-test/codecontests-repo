#!/usr/bin/env python3

import sys
sys.path.append('..')
from library import zfunction

s = input().strip()
n = len(s)
Z = zfunction(s)

third = []
for i in range(n):
    if i + Z[i] == n:
        third.append(Z[i])
ll = len(third)

ans = ""
if ll == 0:
    ans = 'Just a legend'
elif ll == 1:
    if Z.count(third[0]) >= 2 or max(Z) > third[0]:
        ans = s[:third[0]]
    else:
        ans = 'Just a legend'
else:
    if Z.count(third[0]) >= 2 or max(Z) > third[0]:
        ans = s[:third[0]]
    else:
        ans = s[:third[1]]
print(ans)