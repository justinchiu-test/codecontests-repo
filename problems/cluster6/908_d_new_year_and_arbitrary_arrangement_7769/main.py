#!/usr/bin/env python3

import sys
import os

# Add parent directory to path to import library
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import read_ints, mod_inverse, MOD

k, pa, pb = read_ints()

# Calculate frequently used values
inv_sum = mod_inverse(pa + pb)
inv_b = mod_inverse(pb)

memo = {}

def dfs(a, ab):
    if ab >= k:
        return ab
    if a + ab >= k:
        return (a - 1 + (pa + pb) * inv_b + ab) % MOD
    if (a, ab) in memo:
        return memo[a, ab]
    
    res = (dfs(a + 1, ab) * pa * inv_sum) + (dfs(a, ab + a) * pb * inv_sum)
    memo[a, ab] = res = res % MOD
    return res

print(dfs(1, 0))