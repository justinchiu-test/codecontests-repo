#!/usr/bin/env python3

from library import read_int, solve_candies

t = read_int()
for _ in range(t):
    n = read_int()
    print(solve_candies(n))