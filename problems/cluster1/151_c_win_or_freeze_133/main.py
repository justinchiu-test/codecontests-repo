#!/usr/bin/env python3

from library import ni, prime_factors

q = ni()
pf = prime_factors(q)
if len(pf) <= 1:
    print(1)
    print(0)
elif len(pf) == 2:
    print(2)
else:
    print(1)
    print(pf[0] * pf[1])
