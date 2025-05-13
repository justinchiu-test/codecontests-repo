#!/usr/bin/env python3

from library import get_ints, divisors

n, k = get_ints()
all_divisors = divisors(n)

if k > len(all_divisors):
    print(-1)
else:
    print(all_divisors[k-1])