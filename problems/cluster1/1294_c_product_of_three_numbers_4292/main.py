#!/usr/bin/env python3

from library import get_int

def solve(n):
    # Try to find three distinct integers a, b, c such that a * b * c = n
    for a in range(2, int(n**(1/3)) + 2):
        if n % a == 0:
            # Found first factor a
            n_reduced = n // a
            
            # Look for the second factor b
            for b in range(a + 1, int(n_reduced**(1/2)) + 2):
                if n_reduced % b == 0:
                    c = n_reduced // b
                    # Check if all factors are distinct and ≥ 2
                    if c > b and a * b * c == n:
                        return [a, b, c]
    return None

for _ in range(get_int()):
    n = get_int()
    result = solve(n)
    
    if result:
        print("YES")
        print(*result)
    else:
        print("NO")