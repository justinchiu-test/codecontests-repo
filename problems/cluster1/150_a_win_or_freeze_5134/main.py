#!/usr/bin/env python3

from library import read_int, get_prime_factors

n = read_int()
prime_factors = get_prime_factors(n)

if n == 1 or len(prime_factors) == 1:
    # If n is 1 or prime, the first player loses
    print(1)
    print(0)
elif len(prime_factors) == 2:
    # If n has exactly 2 prime factors, the first player wins without taking coins
    print(2)
else:
    # If n has more than 2 prime factors, the first player wins by taking the product of the first two prime factors
    product = prime_factors[0] * prime_factors[1]
    print(1)
    print(product)