#!/usr/bin/env python3

from library import read_ints, get_all_divisors

n, k = read_ints()
divisors = get_all_divisors(n)

if k > len(divisors):
    print(-1)
else:
    print(divisors[k-1])