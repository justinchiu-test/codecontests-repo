#!/usr/bin/env python3

from library import read_int, gcd

n = read_int()

if n == 1:
    # For n=1, the answer is 1
    print(1)
else:
    # The answer is the GCD of all divisors of n
    result = n
    
    # Find the GCD of all divisors
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            result = gcd(result, i)
            result = gcd(result, n // i)
            
            # Once we find any divisor, the GCD will be at most that divisor
            # So if we get to 1, we can stop
            if result == 1:
                break
    
    print(result)