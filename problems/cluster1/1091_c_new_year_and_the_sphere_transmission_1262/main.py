#!/usr/bin/env python3
"""
Solution for CF 1091C: generate sequence based on divisors and formula.
"""
from library import ni, divisors

n = ni()
res = []
for d in divisors(n):
    t = n // d
    # formula: t*(2 + (t-1)*d)//2
    res.append((t * (2 + (t - 1) * d)) // 2)
res.sort()
print(*res)
