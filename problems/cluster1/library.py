"""
Shared utility library for Code Compression Task.
Provides token-based I/O and common math functions.
"""
import sys
import math

# --- Token-based input ---
_data = sys.stdin.read().split()
_it = iter(_data)
def ni():
    """Read next token as integer."""
    return int(next(_it))
def ns():
    """Read next token as string."""
    return next(_it)
def na(n):
    """Read next n tokens as a list of integers."""
    return [int(next(_it)) for _ in range(n)]

# --- Math utilities ---
def gcd(a, b):
    """Greatest common divisor."""
    return math.gcd(a, b)

def lcm(a, b):
    """Least common multiple."""
    return a // math.gcd(a, b) * b

def is_prime(n):
    """Return True if n is prime (trial division)."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = int(math.isqrt(n))
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    """Return prime factorization of n as a list (with repetition)."""
    res = []
    # factor out 2s
    while n % 2 == 0:
        res.append(2)
        n //= 2
    # odd factors
    f = 3
    lim = int(math.isqrt(n)) + 1
    while f <= lim and n > 1:
        while n % f == 0:
            res.append(f)
            n //= f
            lim = int(math.isqrt(n)) + 1
        f += 2
    if n > 1:
        res.append(n)
    return res

def unique_prime_factors(n):
    """Return sorted unique prime factors of n."""
    return sorted(set(prime_factors(n)))

def divisors(n):
    """Return sorted list of all divisors of n."""
    res = []
    r = int(math.isqrt(n))
    for i in range(1, r + 1):
        if n % i == 0:
            res.append(i)
            j = n // i
            if j != i:
                res.append(j)
    return sorted(res)

def prefix_sums(arr):
    """Return prefix sums (length len(arr)+1)."""
    ps = [0]
    for x in arr:
        ps.append(ps[-1] + x)
    return ps

def totient(n):
    """Euler's totient function."""
    res = n
    for p in unique_prime_factors(n):
        res = res // p * (p - 1)
    return res
