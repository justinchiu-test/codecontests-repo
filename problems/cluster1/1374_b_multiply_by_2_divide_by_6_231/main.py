#!/usr/bin/env python3

from library import read_int, get_prime_factors_with_counts

t = read_int()
for _ in range(t):
    n = read_int()
    
    if n == 1:
        print(0)
        continue
    
    # To reach 1, we need to divide by powers of 3 and multiply by powers of 2
    # This is equivalent to dividing by powers of 6 = 2*3
    # Get the prime factorization
    factors = get_prime_factors_with_counts(n)
    
    # Check if n can be reduced to 1
    if any(p != 2 and p != 3 for p in factors.keys()):
        print(-1)
        continue
    
    # Get counts of factors
    twos = factors.get(2, 0)
    threes = factors.get(3, 0)
    
    # Check if reduction is possible
    if twos > threes:
        print(-1)
    else:
        # Each operation either adds one 2 or removes one 3
        # We need to perform (threes - twos) divisions by 3, and then
        # threes divisions by 6 (which remove both a 2 and a 3)
        print(2 * threes - twos)