#!/usr/bin/env python3

from library import ni

for _ in range(ni()):
    m = ni()
    # find smallest k >=2 such that (2^k - 1) divides m
    k = 2
    while m % ((1 << k) - 1) != 0:
        k += 1
    print(m // ((1 << k) - 1))
