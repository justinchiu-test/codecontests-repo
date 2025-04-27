"""
Mathematical utilities for competitive programming.
"""

from math import gcd as math_gcd
from typing import Dict, List, Optional, Tuple


def lcm(a: int, b: int) -> int:
    """Calculate the least common multiple of a and b."""
    return a * b // math_gcd(a, b)


def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """Extended Euclidean Algorithm.

    Returns (gcd, x, y) such that a*x + b*y = gcd
    """
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def mod_inverse(a: int, m: int) -> int:
    """Find the modular multiplicative inverse of a under modulo m.

    Returns x such that (a * x) % m = 1
    """
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError(f"{a} has no modular inverse under modulo {m}")
    else:
        return (x % m + m) % m  # Handle negative x


def chinese_remainder_theorem(remainders: List[int], moduli: List[int]) -> int:
    """Solve a system of linear congruences using Chinese remainder theorem.

    Args:
        remainders: List of remainders in the equations
        moduli: List of moduli in the equations

    Returns:
        The solution to the system of congruences
    """
    if len(remainders) != len(moduli):
        raise ValueError("The number of remainders must equal the number of moduli")

    # Check if moduli are pairwise coprime
    for i in range(len(moduli)):
        for j in range(i + 1, len(moduli)):
            if math_gcd(moduli[i], moduli[j]) != 1:
                raise ValueError("Moduli must be pairwise coprime")

    n = 1
    for mod in moduli:
        n *= mod

    result = 0
    for rem, mod in zip(remainders, moduli):
        m = n // mod
        result += rem * m * mod_inverse(m, mod)
        result %= n

    return result


def euler_totient(n: int) -> int:
    """Calculate Euler's totient function φ(n).

    φ(n) is the number of positive integers up to n that are coprime to n.

    Args:
        n: The integer to calculate φ(n) for

    Returns:
        φ(n)
    """
    result = n
    i = 2

    while i * i <= n:
        if n % i == 0:
            # Remove all factors i from n
            while n % i == 0:
                n //= i
            # Update result
            result -= result // i
        i += 1

    if n > 1:
        result -= result // n

    return result


def is_prime(n: int) -> bool:
    """Check if n is prime using trial division."""
    if n <= 1:
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


def prime_factors(n: int) -> Dict[int, int]:
    """Find the prime factorization of n."""
    factors = {}
    d = 2

    while d * d <= n:
        while n % d == 0:
            if d in factors:
                factors[d] += 1
            else:
                factors[d] = 1
            n //= d
        d += 1

    if n > 1:
        if n in factors:
            factors[n] += 1
        else:
            factors[n] = 1

    return factors


def sieve_of_eratosthenes(n: int) -> List[int]:
    """Generate all primes less than or equal to n using Sieve of Eratosthenes."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return [i for i in range(n + 1) if sieve[i]]


def factorial_mod(n: int, mod: int) -> int:
    """Calculate n! % mod efficiently."""
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % mod
    return result


def binomial_coefficient(n: int, k: int, mod: Optional[int] = None) -> int:
    """Calculate binomial coefficient C(n, k) = n! / (k! * (n-k)!).

    Args:
        n: The upper value
        k: The lower value
        mod: Optional modulo for the result

    Returns:
        C(n, k) (optionally modulo mod)
    """
    k = min(k, n - k)

    if k < 0:
        return 0
    if k == 0:
        return 1

    numerator = 1
    denominator = 1

    for i in range(1, k + 1):
        numerator = (numerator * (n - k + i)) % mod if mod else numerator * (n - k + i)
        denominator = (denominator * i) % mod if mod else denominator * i

    if mod:
        return (numerator * mod_inverse(denominator, mod)) % mod
    else:
        return numerator // denominator


def powmod(base: int, exp: int, mod: int) -> int:
    """Calculate (base^exp) % mod efficiently."""
    if mod == 1:
        return 0

    result = 1
    base %= mod

    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        exp >>= 1
        base = (base * base) % mod

    return result


def matrix_multiply(
    A: List[List[int]], B: List[List[int]], mod: Optional[int] = None
) -> List[List[int]]:
    """Multiply two matrices A and B.

    Args:
        A: First matrix
        B: Second matrix
        mod: Optional modulo for the result

    Returns:
        The product A * B
    """
    if not A or not B or not A[0] or not B[0]:
        return [[]]

    n, m = len(A), len(A[0])
    p, q = len(B), len(B[0])

    if m != p:
        raise ValueError("Matrix dimensions do not match for multiplication")

    C = [[0] * q for _ in range(n)]

    for i in range(n):
        for j in range(q):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]
                if mod:
                    C[i][j] %= mod

    return C


def matrix_power(
    A: List[List[int]], p: int, mod: Optional[int] = None
) -> List[List[int]]:
    """Calculate A^p efficiently using binary exponentiation.

    Args:
        A: The matrix to raise to a power
        p: The power to raise A to
        mod: Optional modulo for the result

    Returns:
        A^p
    """
    if not A or not A[0]:
        return [[]]

    n = len(A)
    if any(len(row) != n for row in A):
        raise ValueError("Matrix must be square")

    # Identity matrix
    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    while p > 0:
        if p & 1:
            result = matrix_multiply(result, A, mod)
        A = matrix_multiply(A, A, mod)
        p >>= 1

    return result


def fibonacci(n: int, mod: Optional[int] = None) -> int:
    """Calculate the nth Fibonacci number efficiently using matrix exponentiation.

    Args:
        n: The index (0-based) of the Fibonacci number to calculate
        mod: Optional modulo for the result

    Returns:
        The nth Fibonacci number
    """
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Matrix to represent the Fibonacci recurrence relation
    F = [[1, 1], [1, 0]]

    # F^(n-1) gives the nth Fibonacci number in the (0, 0) position
    result = matrix_power(F, n - 1, mod)

    return result[0][0]
