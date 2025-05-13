#!/usr/bin/env python3

from library import get_int

def sphere_transmission(n):
    """
    Calculate the possible sums of arithmetical progressions 
    for the sphere transmission process.
    """
    # Calculate all divisors of n
    divisors_set = {1, n}  # Start with 1 and n as divisors
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_set.add(i)
            divisors_set.add(n // i)
    
    results = []
    
    for k in divisors_set:
        # Calculate the number of terms in the arithmetic progression
        term_count = n // k
        
        # Calculate the sum of the arithmetic progression
        # First term: 1
        # Last term: 1 + (term_count - 1) * k
        # Sum = (term_count * (first_term + last_term)) / 2
        result = (term_count * (2 + (term_count - 1) * k)) // 2
        results.append(result)
    
    return sorted(results)

n = get_int()
result = sphere_transmission(n)
print(*result)