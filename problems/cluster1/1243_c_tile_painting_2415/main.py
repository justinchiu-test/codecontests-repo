#!/usr/bin/env python3

from library import get_int, prime_factors

def min_reachable_tile(n):
    """
    Determine the minimum index of a tile reachable from any starting tile
    based on the prime factorization of n.
    """
    # Get prime factorization
    factors = prime_factors(n)
    
    # If n has only one unique prime factor, return that factor
    if len(factors) == 1:
        # Return the only key in the dictionary
        return list(factors.keys())[0]
    else:
        # If n has multiple different prime factors, return 1
        return 1

n = get_int()
print(min_reachable_tile(n))