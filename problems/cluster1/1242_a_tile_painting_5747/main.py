#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import read_int, get_unique_prime_factors

n = read_int()
prime_factors = get_unique_prime_factors(n)

if len(prime_factors) == 0:  # n = 1
    print(1)
elif len(prime_factors) == 1:  # n is a prime or prime power
    print(prime_factors[0])
else:
    print(1)  # Multiple prime factors, GCD of proper divisors is 1
