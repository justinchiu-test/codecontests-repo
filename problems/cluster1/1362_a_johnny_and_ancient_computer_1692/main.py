#!/usr/bin/env python3

from library import read_int, read_ints, min_operations_power_of_two

t = read_int()
for _ in range(t):
    a, b = read_ints()
    print(min_operations_power_of_two(a, b))