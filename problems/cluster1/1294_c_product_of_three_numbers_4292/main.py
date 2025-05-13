#!/usr/bin/env python3

from library import read_int, find_three_factors

t = read_int()
for _ in range(t):
    n = read_int()
    possible, factors = find_three_factors(n)
    
    if possible:
        print("YES")
        print(*factors)
    else:
        print("NO")