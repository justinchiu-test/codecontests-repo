#!/usr/bin/env python3

from library import read_int

def find_three_distinct_factors(n):
    """
    Try to find three distinct factors a, b, c such that a*b*c = n
    """
    for a in range(2, int(n**(1/3)) + 1):
        if n % a == 0:
            # Found first factor
            remaining = n // a
            
            # Find second factor
            for b in range(a + 1, int(remaining**0.5) + 1):
                if remaining % b == 0:
                    c = remaining // b
                    if c > b:  # Ensure three distinct factors
                        return a, b, c
    
    return None

t = read_int()
for _ in range(t):
    n = read_int()
    
    result = find_three_distinct_factors(n)
    
    if result:
        print("YES")
        print(*result)
    else:
        print("NO")