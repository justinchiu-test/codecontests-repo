#!/usr/bin/env python3
"""
Solution for CF 1110C: maximize gcd(a⊕b, a&b) via bit manipulations.
"""
from library import ni, prime_factors

q = ni()
for _ in range(q):
    n = ni()
    # if n+1 is not a power of two, answer is next all-ones: (1<<bit_length)-1
    if (n + 1) & n:
        print((1 << n.bit_length()) - 1)
    else:
        # n = 2^k - 1; find smallest divisor p and print n//p (or 1 if prime)
        p = prime_factors(n)[0]
        print(n // p)
