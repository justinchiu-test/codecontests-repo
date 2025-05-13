#!/usr/bin/env python3

#!/usr/bin/env python3
"""
Solution for CF 1076B: compute number of subtractions in divisor subtraction algorithm.
"""
from library import ni, is_prime, prime_factors

n = ni()
if n % 2 == 0:
    print(n // 2)
elif is_prime(n):
    print(1)
else:
    # subtract smallest prime divisor once, then even n-p uses n/2 subtractions
    p = prime_factors(n)[0]
    print(1 + (n - p) // 2)
