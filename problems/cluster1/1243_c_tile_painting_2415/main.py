#!/usr/bin/env python3

#!/usr/bin/env python3
"""
Solution for CF 1243C: tile painting maximum colors via gcd of prime factors.
"""
from library import ni, unique_prime_factors

n = ni()
ups = unique_prime_factors(n)
print(ups[0] if len(ups) == 1 else 1)
