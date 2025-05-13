#!/usr/bin/env python3

from library import read_ints, get_prime_factors_with_counts

def count_operations(a, b):
    """
    Count the minimum number of operations to transform a to b.
    Each operation is either multiplying by 2 or multiplying by 3.
    Returns -1 if it's impossible.
    """
    if a == b:
        return 0

    if b % a != 0:
        return -1

    ratio = b // a
    factors = get_prime_factors_with_counts(ratio)

    # Check if the only prime factors are 2 and 3
    if set(factors.keys()).issubset({2, 3}):
        return sum(factors.values())

    return -1

a, b = read_ints()
print(count_operations(a, b))