#!/usr/bin/env python3

from library import get_ints, power_mod, MOD_SMALL, prime_factors

def solve(x, n):
    # Get prime factors of x
    factors = prime_factors(x)
    result = 1
    
    for p in factors:
        nn = n
        # Calculate p^(sum of floor(n/p^i) for i=1,2,...)
        while nn > 0:
            result = (result * power_mod(p, nn // p, MOD_SMALL)) % MOD_SMALL
            nn = nn // p
            
    return result

x, n = get_ints()
print(solve(x, n))