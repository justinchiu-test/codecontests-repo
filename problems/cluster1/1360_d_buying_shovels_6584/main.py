#!/usr/bin/env python3

from library import read_int, read_ints, min_packages

t = read_int()
for _ in range(t):
    n, k = read_ints()
    print(min_packages(n, k))