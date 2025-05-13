#!/usr/bin/env python3

from library import get_int, prime_factors

def min_operations(n):
    """
    Find the minimum number of operations to transform n to 1
    by either multiplying by 2 or dividing by 6. Return -1 if impossible.
    """
    if n == 1:
        return 0
    
    # Get prime factorization
    factors = prime_factors(n)
    
    # Extract factors of 2 and 3
    twos = factors.get(2, 0)
    threes = factors.get(3, 0)
    
    # Check if n can be reduced to 1
    # n must be of the form 2^a * 3^b * 1 (all other factors must be 1)
    if len(factors) > 2 or (len(factors) == 2 and (2 not in factors or 3 not in factors)):
        return -1
    
    # We need at least as many 3s as 2s
    if twos > threes:
        return -1
    
    # Each factor of 3 requires two operations:
    # First, multiply by 2 to get a factor of 6
    # Second, divide by 6 to remove both a factor of 2 and 3
    # However, if there are already twos in n, we can skip some multiply by 2 steps
    return 2 * threes - twos

for _ in range(get_int()):
    n = get_int()
    print(min_operations(n))