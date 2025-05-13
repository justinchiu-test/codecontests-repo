#!/usr/bin/env python3

from library import read_int, read_ints, get_prime_factors_with_counts

def max_divisible_by_not_q(p, q):
    """
    Find the maximum integer x such that:
    1. x divides p
    2. x is not divisible by q
    """
    # If p is not divisible by q, then p itself is the answer
    if p % q != 0:
        return p
    
    # Get prime factorization of q
    q_factors = get_prime_factors_with_counts(q)
    
    # For each prime factor of q, find its count in p
    min_div = float('inf')
    for prime, q_count in q_factors.items():
        # Count how many times this prime divides p
        p_count = 0
        temp_p = p
        while temp_p % prime == 0:
            p_count += 1
            temp_p //= prime
        
        # We need to remove enough factors to make x not divisible by q
        # For each prime factor, we need to leave (q_count-1) copies in x
        divisor = prime ** (p_count - (q_count - 1))
        min_div = min(min_div, divisor)
    
    # Divide p by the smallest required divisor
    return p // min_div

t = read_int()
for _ in range(t):
    p, q = read_ints()
    print(max_divisible_by_not_q(p, q))