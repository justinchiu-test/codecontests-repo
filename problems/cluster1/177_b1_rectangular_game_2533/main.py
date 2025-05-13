#!/usr/bin/env python3

from library import ni, prime_factors

n = ni()
res = n
while n > 1:
    pf = prime_factors(n)
    if not pf:
        # n is prime, take one pebble per row
        res += 1
        break
    # choose smallest divisor a to maximize next n = n/a
    a = min(pf)
    n //= a
    res += n
print(res)
