#!/usr/bin/env python3

from library import read_ints, get_unique_prime_factors, mod_pow, MOD

def solve(x, n):
    # Get all unique prime factors of x
    prime_factors = get_unique_prime_factors(x)

    result = 1
    for p in prime_factors:
        # For each prime factor, calculate p^(⌊n/p⌋ + ⌊n/p²⌋ + ...)
        exponent = 0
        temp_n = n
        while temp_n > 0:
            exponent = (exponent + temp_n // p) % (MOD - 1)  # Use Fermat's little theorem for exponent
            temp_n //= p

        result = (result * mod_pow(p, exponent, MOD)) % MOD

    return result

x, n = read_ints()
print(solve(x, n))