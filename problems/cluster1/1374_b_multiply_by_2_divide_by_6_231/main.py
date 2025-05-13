#!/usr/bin/env python3

from library import read_int, read_test_cases, min_moves_to_one

t = read_int()
for _ in range(t):
    n = read_int()
    print(min_moves_to_one(n))