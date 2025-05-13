#!/usr/bin/env python3

from library import ni, prime_factors, unique_prime_factors

t = ni()
for _ in range(t):
    p = ni()
    q = ni()
    if p % q != 0:
        print(p)
        continue
    ans = 1
    # factorize q and for each prime compute removal
    pf = prime_factors(q)
    for pr in set(pf):
        # count exponent in q
        kq = pf.count(pr)
        # count exponent in p
        kp = 0
        tmp = p
        while tmp % pr == 0:
            tmp //= pr
            kp += 1
        # remove minimal power to make p not divisible by q
        rem = kp - kq + 1
        candidate = p // (pr ** rem)
        ans = max(ans, candidate)
    print(ans)
