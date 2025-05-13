#!/usr/bin/env python3

# written with help of editorial
from library import ni, na, gcd, divisors

n = ni()
m = ni()
a = na(n)
# compute gcd of (ai - 1)
g = 0
for ai in a:
    g = gcd(g, ai - 1)

res = 0
for d in divisors(g):
    # only odd divisors
    if d % 2 == 0:
        continue
    v = d
    while v <= m:
        res += m - v
        v <<= 1
print(res)
