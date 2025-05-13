#!/usr/bin/env python3

from library import read_int, get_all_divisors

n = read_int()
divisors = get_all_divisors(n)

result = []
for d in divisors:
    # For each divisor d, calculate the sum of arithmetic progression
    # with k = n/d terms, first term a1 = 1, and common difference = d
    k = n // d
    result.append((k * (2 + (k - 1) * d)) // 2)

result.sort()
print(*result)