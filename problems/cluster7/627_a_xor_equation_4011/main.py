#!/usr/bin/env python3
from library import ni

s = ni(); x = ni()
if s < x or (s - x) & 1:
    print(0)
    exit()
u = (s - x) // 2
d = x
# if any bit set in both u and d, no solution
if u & d:
    print(0)
    exit()
# number of ways = 2^(popcount of d)
res = 1 << d.bit_count()
if s == x:
    # exclude trivial all-zero selection
    res = max(0, res - 2)
print(res)
