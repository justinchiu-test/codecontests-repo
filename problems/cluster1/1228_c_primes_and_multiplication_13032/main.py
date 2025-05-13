#!/usr/bin/env python3
"""
Solution for CF 1228C: count prime factor exponents in n! for primes dividing x, then compute product mod.
"""
from library import ni, unique_prime_factors

MOD = 10**9 + 7
x = ni()
n = ni()
res = 1
for p in unique_prime_factors(x):
     tot = 0
     nn = n
     while nn:
         nn //= p
         tot += nn
     res = res * pow(p, tot, MOD) % MOD
print(res)
