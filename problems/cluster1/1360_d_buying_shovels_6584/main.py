#!/usr/bin/env python3

from library import ni, divisors

for _ in range(ni()):
    n = ni()
    k = ni()
    if k >= n:
        print(1)
    else:
        ans = n
        for d in divisors(n):
            if d <= k:
                ans = min(ans, n // d)
        print(ans)
