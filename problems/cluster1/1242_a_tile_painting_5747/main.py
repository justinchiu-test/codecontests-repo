#!/usr/bin/env python3
"""
Solution for CF 1242A: maximum colors = gcd of all divisors >1, or 1 if mixed primes.
"""
from library import ni, unique_prime_factors

n = ni()
ups = unique_prime_factors(n)
print(ups[0] if len(ups) == 1 else 1)
