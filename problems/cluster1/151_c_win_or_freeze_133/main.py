#!/usr/bin/env python3

from library import read_int, get_prime_factors

n = read_int()
factors = get_prime_factors(n)

# This is a similar problem to 150_a_win_or_freeze
if len(factors) == 2:
    # If n has exactly 2 prime factors, the first player wins without taking coins
    print(2)
else:
    # Otherwise, the first player has a strategy
    print(1)
    if len(factors) <= 1:
        # If n is 1 or prime, the first player can't take any coins
        print(0)
    else:
        # If n has more than 2 prime factors, take the product of the first two
        print(factors[0] * factors[1])