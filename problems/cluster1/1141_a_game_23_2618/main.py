#!/usr/bin/env python3

from library import get_ints, prime_factors

def min_operations(n, m):
    """
    Find the minimum number of operations to transform n to m
    by multiplying by 2 or 3. Return -1 if impossible.
    """
    if n == m:
        return 0
    if m % n != 0:
        return -1
    
    ratio = m // n
    
    # Get prime factorization of the ratio
    factors = prime_factors(ratio)
    
    # Check if all factors are 2 or 3
    if any(p != 2 and p != 3 for p in factors):
        return -1
    
    # Count total operations (sum of exponents)
    operations = sum(factors.values())
    
    return operations

n, m = get_ints()
print(min_operations(n, m))