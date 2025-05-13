#!/usr/bin/env python3

from library import get_int, prime_factors

def solve(n):
    """
    Find the longest non-decreasing sequence a1, a2, ..., ak such that:
    1. a1 * a2 * ... * ak = n
    2. gcd(a1, a2, ..., ak) > 1
    """
    # Get prime factorization
    factors = prime_factors(n)
    
    # If n is prime (only one factor with power 1)
    if len(factors) == 1 and list(factors.values())[0] == 1:
        return [1, n]
    
    # Find the prime with the highest power
    prime, max_power = max(factors.items(), key=lambda x: x[1])
    
    # Create the sequence
    sequence = [prime] * (max_power - 1)
    
    # Calculate the last element (all remaining factors combined)
    last_element = n
    for _ in range(max_power - 1):
        last_element //= prime
    
    sequence.append(last_element)
    
    return [len(sequence)] + sequence

for _ in range(get_int()):
    n = get_int()
    result = solve(n)
    print(result[0])
    print(*result[1:])