"""
Library file for cluster1.
This contains shared code that can be imported by problems in this cluster.
"""
import sys
import math

def input_int():
    return int(sys.stdin.readline())

def input_str():
    return sys.stdin.readline().strip()

def get_ints():
    return map(int, sys.stdin.readline().split())

def get_array():
    return list(get_ints())

def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return a // gcd(a, b) * b if a and b else 0

def extended_gcd(a, b):
    if b == 0:
        return (1, 0, a)
    x, y, g = extended_gcd(b, a % b)
    return (y, x - a // b * y, g)

def modular_inverse(a, m):
    x, y, g = extended_gcd(a, m)
    if g != 1:
        return None
    return x % m

def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    r = int(n ** 0.5)
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True

def sieve(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i, is_p in enumerate(sieve) if is_p]

def prime_factors(n):
    d = {}
    while n % 2 == 0:
        d[2] = d.get(2, 0) + 1
        n //= 2
    f = 3
    while f * f <= n:
        while n % f == 0:
            d[f] = d.get(f, 0) + 1
            n //= f
        f += 2
    if n > 1:
        d[n] = 1
    return d

def get_all_prime_factors(n):
    return list(prime_factors(n).keys())

def all_divisors(n):
    pf = prime_factors(n)
    divs = [1]
    for p, exp in pf.items():
        divs = [d * p ** e for d in divs for e in range(exp + 1)]
    return sorted(divs)

def count_divisors(n):
    pf = prime_factors(n)
    res = 1
    for exp in pf.values():
        res *= (exp + 1)
    return res

def nth_divisor(n, k):
    divs = all_divisors(n)
    return divs[k - 1] if 1 <= k <= len(divs) else -1

def mod_pow(base, exp, mod):
    return pow(base, exp, mod)

def mod_add(a, b, mod):
    """Return (a + b) % mod"""
    return (a + b) % mod

def mod_mul(a, b, mod):
    """Return (a * b) % mod"""
    return (a * b) % mod

def mod_div(a, b, mod):
    """Return (a / b) % mod, using modular inverse of b"""
    inv = modular_inverse(b, mod)
    return (a * inv) % mod if inv is not None else None

def factorial(n, mod=None):
    """Compute n! (optionally modulo mod)"""
    if mod:
        res = 1
        for i in range(1, n + 1):
            res = res * i % mod
        return res
    from math import factorial as _fact
    return _fact(n)

def nCr(n, r, mod=None):
    """Compute C(n, r) = n! / (r! (n-r)!) (optionally modulo mod)"""
    if r < 0 or r > n:
        return 0
    if mod:
        num = factorial(n, mod)
        den = factorial(r, mod) * factorial(n - r, mod) % mod
        inv_den = modular_inverse(den, mod)
        return num * inv_den % mod
    from math import comb
    return comb(n, r)

def nPr(n, r, mod=None):
    """Compute P(n, r) = n! / (n-r)! (optionally modulo mod)"""
    if r < 0 or r > n:
        return 0
    if mod:
        num = factorial(n, mod)
        den = factorial(n - r, mod)
        inv_den = modular_inverse(den, mod)
        return num * inv_den % mod
    from math import perm
    return perm(n, r)

def next_power_of_two(n):
    """Return the smallest power of two >= n"""
    if n <= 1:
        return 1
    return 1 << ((n - 1).bit_length())

def count_set_bits(n):
    return bin(n).count('1')

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0
