#!/usr/bin/env python3

from library import get_int, get_ints, MOD_SMALL
from collections import defaultdict

def solve():
    n = get_int()
    nums = get_ints()
    
    # Count occurrences of each divisor
    count = defaultdict(int)
    for num in nums:
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                count[i] += 1
                if i != num // i:  # Avoid counting twice for perfect squares
                    count[num // i] += 1
    
    maxk = max(count.keys())
    
    # Calculate 2^count[k] - 1 for each divisor k
    # This represents the number of non-empty subsequences where all elements are divisible by k
    freq = {k: (1 << count[k]) - 1 for k in count}
    
    # Apply inclusion-exclusion principle using Möbius inversion
    for k in sorted(count.keys(), reverse=True):
        for kk in range(k << 1, maxk + 1, k):
            if kk in freq:
                freq[k] -= freq[kk]
    
    # Return the number of subsequences where gcd of all elements is 1
    return freq[1] % MOD_SMALL

print(solve())