#!/usr/bin/env python3

from library import read_int, get_unique_prime_factors

n = read_int()
prime_factors = get_unique_prime_factors(n)

if len(prime_factors) == 1:
    print(prime_factors[0])
else:
    print(1)