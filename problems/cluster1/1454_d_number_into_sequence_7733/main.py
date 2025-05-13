#!/usr/bin/env python3

from library import ni, prime_factors

t = ni()
for _ in range(t):
    x = ni()
    pf = prime_factors(x)
    if not pf:
        print(1)
        print(x)
        continue
    # count prime factor exponents
    cnts = {}
    for pr in pf:
        cnts[pr] = cnts.get(pr, 0) + 1
    pr, cnt = max(cnts.items(), key=lambda it: it[1])
    print(cnt)
    for _ in range(cnt - 1):
        print(pr, end=' ')
    last = x // (pr ** (cnt - 1))
    print(last)
