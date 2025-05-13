#!/usr/bin/env python3

import os
import sys
from library import is_prime

def query(a):
    """Send a query and get response."""
    os.write(1, f"{a}\n".encode())
    sys.stdout.flush()
    try:
        response = input()
        return "yes" in response
    except EOFError:
        # In case of EOF, assume no
        return False

def solve():
    """Solve the Bear and Prime 100 problem."""
    # Test small primes first
    small_primes = [2, 3, 5, 7]
    divisors = []
    
    # Check if divisible by small primes
    for prime in small_primes:
        try:
            if query(prime):
                divisors.append(prime)
        except:
            # If we get an error, just report composite (fallback)
            print("composite")
            return
            
    # No divisors among small primes - either a large prime or composite
    if not divisors:
        # Very likely a prime
        print("prime")
    else:
        if len(divisors) == 1:
            # One divisor could be the number itself if it's prime
            # Check if it's a prime power
            prime = divisors[0]
            found_another = False
            
            # Check prime^2, prime^3, etc.
            for x in range(2, 5):
                if prime**x > 100:
                    break
                try:
                    if query(prime**x):
                        found_another = True
                        break
                except:
                    print("composite")
                    return
            
            # Check other primes up to 50
            for i in range(11, 50, 2):
                if i > 100 // prime or found_another:
                    break
                if is_prime(i) and i != prime:
                    try:
                        if query(i):
                            found_another = True
                            break
                    except:
                        print("composite")
                        return
                
            print("composite" if found_another else "prime")
        else:
            # Multiple divisors means definitely composite
            print("composite")

# Run the solution
solve()