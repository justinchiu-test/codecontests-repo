#!/usr/bin/env python3

from library import get_int, is_prime

def solve(n):
    """
    Find all numbers from 2 to n that are either prime or powers of primes.
    """
    result = []
    
    # First, add powers of each prime in the correct order
    for prime in range(2, n + 1):
        if is_prime(prime):
            # Add all powers of this prime
            power = prime
            while power <= n:
                result.append(power)
                power *= prime
    
    return result

n = get_int()
answer = solve(n)
print(len(answer))
print(" ".join(map(str, answer)))