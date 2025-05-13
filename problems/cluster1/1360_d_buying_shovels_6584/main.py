#!/usr/bin/env python3

from library import get_int, get_ints, divisor_pairs

def min_packages(n, k):
    """
    Find the minimum number of packages needed to buy n shovels
    with constraint that each package can have at most k shovels.
    """
    if k >= n:
        return 1
    
    smallest_package = n  # Start with the worst case: one shovel per package
    
    # Try all divisor pairs of n
    for a, b in divisor_pairs(n):
        # Check if a is a valid package size (≤ k)
        if a <= k:
            smallest_package = min(smallest_package, b)
        
        # Check if b is a valid package size (≤ k)
        if b <= k:
            smallest_package = min(smallest_package, a)
    
    return smallest_package

for _ in range(get_int()):
    n, k = get_ints()
    print(min_packages(n, k))