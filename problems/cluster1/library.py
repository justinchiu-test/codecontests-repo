#!/usr/bin/env python3
"""
Library file for cluster1.
This contains shared code that can be imported by problems in this cluster.
"""

import sys
import math

# IO utilities
def read_int():
    """Read and return a single integer from stdin."""
    return int(sys.stdin.readline())

def read_ints():
    """Read a line of space-separated integers and return as a list."""
    return list(map(int, sys.stdin.readline().split()))

def read_str():
    """Read a line as a string without the trailing newline."""
    return sys.stdin.readline().rstrip("\n")

def read_strs():
    """Read a line and split into a list of strings."""
    return sys.stdin.readline().split()

def read_all_ints():
    """Read all remaining input and return as a list of integers."""
    return list(map(int, sys.stdin.read().split()))

# Math utilities
gcd = math.gcd

def lcm(a, b):
    """Return the least common multiple of a and b."""
    return a // gcd(a, b) * b

def sieve(n):
    """Return list of all primes up to n inclusive using the Sieve of Eratosthenes."""
    is_prime = [True] * (n + 1)
    if n >= 0:
        is_prime[0] = False
    if n >= 1:
        is_prime[1] = False
    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return primes

def prime_factors(n):
    """Return the list of prime factors of n with multiplicity."""
    factors = []
    # handle factor 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # odd factors
    p = 3
    while p * p <= n:
        while n % p == 0:
            factors.append(p)
            n //= p
        p += 2
    if n > 1:
        factors.append(n)
    return factors

def is_prime(n):
    """Return True if n is prime, False otherwise."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = int(n**0.5)
    for i in range(3, r+1, 2):
        if n % i == 0:
            return False
    return True

def prev_pow2(n):
    """Return the largest power of two <= n."""
    if n < 1:
        return 0
    return 1 << (n.bit_length() - 1)

def next_pow2(n):
    """Return the smallest power of two >= n."""
    if n < 1:
        return 1
    return 1 << ((n - 1).bit_length())

# Divisors utility
def divisors(n):
    """Return the sorted list of all positive divisors of n."""
    res = set()
    r = int(n**0.5)
    for i in range(1, r+1):
        if n % i == 0:
            res.add(i)
            res.add(n//i)
    return sorted(res)

# Modular arithmetic
def modpow(a, b, mod):
    """Compute a**b mod mod, using built-in pow."""
    return pow(a, b, mod)

def modinv(a, mod):
    """Compute modular inverse of a under prime mod."""
    return pow(a, mod - 2, mod)

# Solver harness (optional)
def run(solve):
    """
    Entry point for scripts:
    - solve: a no-argument function that reads input, computes, and prints output.
    """
    solve()

if __name__ == "__main__":
    # no-op when run directly
    pass
