#!/usr/bin/env python3

from library import get_int, is_prime, smallest_divisor

def min_operations(n):
    """
    Find the minimum number of operations to reduce n to 0 by
    repeatedly subtracting the smallest divisor and then dividing by 2.
    """
    # If n is prime, we need only one operation
    if is_prime(n):
        return 1
    
    # If n is even, we can keep dividing by 2
    if n % 2 == 0:
        return n // 2
    
    # For odd non-prime n, find the smallest prime factor
    smallest_div = smallest_divisor(n)
    
    # After subtracting the smallest prime factor, the number becomes even
    # So we can perform (n - smallest_div) / 2 more operations + 1 for the initial subtraction
    return ((n - smallest_div) // 2) + 1

n = get_int()
print(min_operations(n))