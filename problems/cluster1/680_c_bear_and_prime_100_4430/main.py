#!/usr/bin/env python3

import sys
import os
from library import is_prime

def query(a):
    """Send query to the judge and get response"""
    print(a, flush=True)
    return input()

def main():
    # List of small primes and their powers to check
    test_numbers = []
    
    # Add small primes and their powers up to 100
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]:
        test_numbers.append(p)  # Add the prime itself
        power = p * p
        while power <= 100:
            test_numbers.append(power)  # Add powers of the prime
            power *= p
    
    # Make sure we have no duplicates and sort
    test_numbers = sorted(set(test_numbers))
    
    # Limit to at most 20 queries
    test_numbers = test_numbers[:20]
    
    # Query each number and count how many divisors we find
    divisors_found = 0
    for num in test_numbers:
        response = query(num)
        if response == "yes":
            divisors_found += 1
    
    # If the number has more than 1 divisor, or it has a divisor that's a prime power > 1,
    # then it's composite, otherwise it's prime
    if divisors_found > 1 or any(x > 10 for x in test_numbers if query(x) == "yes"):
        print("composite", flush=True)
    else:
        print("prime", flush=True)

if __name__ == "__main__":
    main()