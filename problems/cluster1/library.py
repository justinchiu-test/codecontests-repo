"""
Shared library of utilities for common Codeforces-style problems.
Imported by each problem's main.py via `from library import ...`.
"""
import sys
import math
from sys import stdin

def I():
    """Read a single integer from stdin."""
    return int(stdin.readline())

def MI():
    """Read a line of space-separated integers as map(int, ...)."""
    return map(int, stdin.readline().split())

def LI():
    """Read a line of space-separated integers as a list."""
    return list(map(int, stdin.readline().split()))

def LLI(n):
    """Read n lines, each as a list of integers."""
    return [LI() for _ in range(n)]

def S():
    """Read a stripped string."""
    return stdin.readline().strip()

def SS():
    """Read a line of space-separated strings."""
    return stdin.readline().split()

def gcd(a, b):
    """Greatest common divisor."""
    return math.gcd(a, b)

def lcm(a, b):
    """Least common multiple."""
    return a // gcd(a, b) * b

def factors(n):
    """Return sorted list of all divisors of n."""
    small, large = [], []
    r = int(n**0.5)
    for i in range(1, r+1):
        if n % i == 0:
            small.append(i)
            if i != n // i:
                large.append(n // i)
    return small + large[::-1]

def is_prime(n):
    """Check primality in O(√n)."""
    if n < 2:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_sieve(n):
    """Return list of primes up to n."""
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i:n+1:i] = [False] * len(range(i*i, n+1, i))
    return [i for i, ok in enumerate(sieve) if ok]

def factorize(n):
    """Return prime factorization of n as {prime: exponent}."""
    fs = {}
    r = int(n**0.5)
    for p in prime_sieve(r + 1):
        while n % p == 0:
            fs[p] = fs.get(p, 0) + 1
            n //= p
    if n > 1:
        fs[n] = fs.get(n, 0) + 1
    return fs

def nCr(n, r):
    """Compute C(n, r) exactly."""
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    num = 1
    den = 1
    for i in range(1, r + 1):
        num *= n - r + i
        den *= i
    return num // den
def spf(n):
    """Return the smallest prime divisor of n (n >= 1)."""
    if n % 2 == 0:
        return 2
    i = 3
    r = int(n**0.5)
    while i <= r:
        if n % i == 0:
            return i
        i += 2
    return n
