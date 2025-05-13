#!/usr/bin/env python3

from library import read_int, read_ints, max_divisor_not_divisible_by_q

t = read_int()
for _ in range(t):
    p, q = read_ints()
    print(max_divisor_not_divisible_by_q(p, q))