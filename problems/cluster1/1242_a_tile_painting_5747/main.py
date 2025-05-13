#!/usr/bin/env python3

from library import get_int, is_prime, divisors, gcd_of_list

def min_colors(n):
    """
    Determine the minimum number of colors needed to paint tiles
    such that no two adjacent tiles have the same color.
    """
    # Special cases for small n
    if n < 3:
        return n
    
    # Check if n is prime
    if is_prime(n):
        return n
    
    # Get all divisors except 1 and n
    all_divisors = [d for d in divisors(n) if d != 1 and d != n]
    
    # If we have divisors, return their GCD
    if all_divisors:
        return gcd_of_list(all_divisors)
    else:
        return n  # This should never happen if n > 2 and not prime

n = get_int()
print(min_colors(n))