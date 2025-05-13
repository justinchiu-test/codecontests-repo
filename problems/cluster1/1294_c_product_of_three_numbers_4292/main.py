#!/usr/bin/env python3
"""
Solution for CF 1294C: find three distinct integers >1 whose product equals n.
"""
from library import ni, divisors

t = ni()
for _ in range(t):
    n = ni()
    # find divisors excluding 1 and n
    ds = divisors(n)
    mids = [d for d in ds if d not in (1, n)]
    if len(mids) < 2:
        print("NO")
        continue
    a = mids[0]
    rem = n // a
    # find second divisor b different from a
    bs = [d for d in divisors(rem) if d not in (1, rem) and d != a]
    found = False
    for b in bs:
        c = rem // b
        if c > 1 and c != a and c != b:
            print("YES")
            print(a, b, c)
            found = True
            break
    if not found:
        print("NO")
