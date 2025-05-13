#!/usr/bin/env python3
from library import *

n = read_int()
p = [0, 0] + read_ints()
d = [0] * (n + 1)
for i in range(n, 1, -1):
    if d[i] == 0:
        d[i] = 1
    d[p[i]] += d[i]
if n == 1:
    d[1] = 1
res = sorted(d[1:])
print(*res)
