#!/usr/bin/env python3

from library import read_ints

s, x = read_ints()
if s < x or (s - x) & 1:
    print(0)
    exit(0)
u, d = (s - x) // 2, x
res = 1
while u or d:
    uu, dd = u & 1, d & 1
    if uu and dd:
        res *= 0
    elif uu == 0 and dd == 1:
        res *= 2
    u, d = u >> 1, d >> 1
if s == x:
    res = max(0, res - 2)
print(res)
