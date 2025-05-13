#!/usr/bin/env python3
"""
Solution for CF 1068B: number of distinct values of lcm(a,b)/a = number of divisors of b.
"""
from library import ni, divisors

b = ni()
print(len(divisors(b)))
