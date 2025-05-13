#!/usr/bin/env python3

from library import read_int, read_ints, count_coprime_numbers

t = read_int()
for _ in range(t):
    a, m = read_ints()
    print(count_coprime_numbers(a, m))