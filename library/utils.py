"""
Utility functions for competitive programming.
"""

from math import gcd, sqrt
from typing import Dict, List, Tuple, TypeVar

T = TypeVar("T")


def lcm(a: int, b: int) -> int:
    """Calculate the least common multiple of a and b."""
    return a * b // gcd(a, b)


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


def is_prime(n: int) -> bool:
    """Check if n is prime."""
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


def sieve_of_eratosthenes(n: int) -> List[int]:
    """Generate all primes less than or equal to n using Sieve of Eratosthenes."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(sqrt(n)) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return [i for i in range(n + 1) if sieve[i]]


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


def combinations_with_replacement(iterable: List[T], r: int) -> List[Tuple[T, ...]]:
    """Return r length subsequences of elements from iterable, allowing repeat elements."""
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return []
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)


def partial_sum(arr: List[int]) -> List[int]:
    """Calculate the partial sum of an array."""
    n = len(arr)
    psum = [0] * (n + 1)
    for i in range(n):
        psum[i + 1] = psum[i] + arr[i]
    return psum


def binary_search(arr: List[T], x: T) -> int:
    """Binary search for x in sorted array arr.

    Returns the index of x if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def lower_bound(arr: List[T], x: T) -> int:
    """Find the first index where arr[i] >= x."""
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid

    return left


def upper_bound(arr: List[T], x: T) -> int:
    """Find the first index where arr[i] > x."""
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] <= x:
            left = mid + 1
        else:
            right = mid

    return left


def all_subsets(arr: List[T]) -> List[List[T]]:
    """Generate all possible subsets of arr."""
    n = len(arr)
    result = []

    for mask in range(1 << n):
        subset = [arr[i] for i in range(n) if (mask & (1 << i))]
        result.append(subset)

    return result


def compress_coordinates(coordinates: List[int]) -> Dict[int, int]:
    """Compress coordinates to the range [0, n-1]."""
    sorted_coords = sorted(set(coordinates))
    return {x: i for i, x in enumerate(sorted_coords)}


def sliding_window_minimum(arr: List[int], k: int) -> List[int]:
    """Find minimum in all sliding windows of size k."""
    n = len(arr)
    if n == 0 or k == 0:
        return []
    if k == 1:
        return arr

    from collections import deque

    result = []
    dq = deque()

    for i in range(n):
        # Remove elements outside the current window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove elements greater than current (they won't be min)
        while dq and arr[dq[-1]] > arr[i]:
            dq.pop()

        dq.append(i)

        # Add to result if we've reached window size
        if i >= k - 1:
            result.append(arr[dq[0]])

    return result
