#!/usr/bin/env python3

from library import read_int, is_prime, get_smallest_prime_factor

n = read_int()

if is_prime(n):
    print(1)
else:
    if n % 2 == 0:
        print(n // 2)
    else:
        smallest_prime = get_smallest_prime_factor(n)
        print(1 + (n - smallest_prime) // 2)