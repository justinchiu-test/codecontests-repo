#!/usr/bin/env python3

from library import get_int

def solve(n):
    """
    Find an integer x such that n = x + 2x + 4x + ... + (2^k-1)x
    This can be rewritten as: n = x * (2^k - 1)
    """
    # Try different values of k, starting from 2
    for k in range(2, 31):  # 2^30 > 10^9, so this is sufficient
        divisor = (1 << k) - 1  # 2^k - 1
        if n % divisor == 0:
            return n // divisor
    
    # This shouldn't happen with the given constraints
    return -1

for _ in range(get_int()):
    n = get_int()
    print(solve(n))