#!/usr/bin/env python3

from library import ni, gcd, totient

q = ni()
for _ in range(q):
    a = ni()
    m = ni()
    g = gcd(a, m)
    print(totient(m // g))
