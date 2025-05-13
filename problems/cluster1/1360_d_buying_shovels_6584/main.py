#!/usr/bin/env python3

from library import read_int, read_ints, get_all_divisors

def min_package_size(n, k):
    """
    Find the minimum package size such that you can buy exactly n shovels
    with package sizes not exceeding k.
    """
    if k >= n:
        return 1
    
    # Get all divisors of n
    divisors = get_all_divisors(n)
    
    # Find the minimum package size
    min_size = n
    for d in divisors:
        if d <= k:
            package_size = n // d
            min_size = min(min_size, package_size)
    
    return min_size

t = read_int()
for _ in range(t):
    n, k = read_ints()
    print(min_package_size(n, k))