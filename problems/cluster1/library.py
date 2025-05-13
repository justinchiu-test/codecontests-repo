"""
Library file for cluster1.
This contains shared code that can be imported by problems in this cluster.
"""
import math
import sys
from collections import defaultdict, Counter
from functools import reduce
from typing import List, Tuple, Set, Dict, Any, Optional, Union, Iterator

# Input/Output utilities
def get_ints() -> List[int]:
    """Read a line of integers from stdin."""
    return list(map(int, input().split()))

def get_int() -> int:
    """Read a single integer from stdin."""
    return int(input())

def get_lines(n: int) -> List[str]:
    """Read n lines from stdin."""
    return [input() for _ in range(n)]

def get_all_lines() -> List[str]:
    """Read all remaining lines from stdin."""
    return sys.stdin.read().splitlines()

# Number theory utilities
def gcd(a: int, b: int) -> int:
    """Calculate the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    """Calculate the least common multiple of a and b."""
    return a * b // gcd(a, b)

def gcd_of_list(numbers: List[int]) -> int:
    """Calculate the greatest common divisor of a list of integers."""
    return reduce(gcd, numbers)

def lcm_of_list(numbers: List[int]) -> int:
    """Calculate the least common multiple of a list of integers."""
    return reduce(lcm, numbers)

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
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
    """Calculate the prime factorization of n as a dictionary of factor: exponent."""
    factors = defaultdict(int)
    
    # Handle 2 separately
    while n % 2 == 0:
        factors[2] += 1
        n //= 2
    
    # Handle odd factors
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors[i] += 1
            n //= i
        i += 2
    
    # If n > 1, it's a prime factor
    if n > 1:
        factors[n] += 1
    
    return dict(factors)

def divisors(n: int) -> List[int]:
    """Get all divisors of n in sorted order."""
    small, large = [], []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            small.append(i)
            if i != n // i:  # Avoid duplicates for perfect squares
                large.append(n // i)
    # Combine small and reversed large for sorted list
    return small + large[::-1]

def count_divisors(n: int) -> int:
    """Count the number of divisors of n."""
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 2 if i != n // i else 1
    return count

def smallest_divisor(n: int) -> int:
    """Find the smallest divisor of n greater than 1."""
    if n % 2 == 0:
        return 2
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return i
    
    return n  # If n is prime, it's its own smallest divisor > 1

def divisor_pairs(n: int) -> List[Tuple[int, int]]:
    """Get all divisor pairs (a, b) where a*b = n, sorted by first element."""
    pairs = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            pairs.append((i, n // i))
    return pairs

def power_mod(base: int, exponent: int, modulus: int) -> int:
    """Calculate (base ^ exponent) % modulus efficiently."""
    if modulus == 1:
        return 0
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

def mod_inverse(a: int, m: int) -> int:
    """Calculate the modular multiplicative inverse of a under modulo m."""
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """Extended Euclidean Algorithm to compute gcd(a, b) and coefficients x, y such that ax + by = gcd(a, b)."""
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def totient(n: int) -> int:
    """Calculate Euler's totient function for n."""
    result = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result // i
        i += 1
    if n > 1:
        result -= result // n
    return result

def sieve_of_eratosthenes(n: int) -> List[int]:
    """Generate all prime numbers up to n using the Sieve of Eratosthenes."""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    
    return [i for i in range(n + 1) if is_prime[i]]

def get_primes_less_than(n: int) -> List[int]:
    """Return all prime numbers less than n."""
    return sieve_of_eratosthenes(n - 1)

def coprime_count(n: int) -> int:
    """Count the number of integers from 1 to n that are coprime with n."""
    return totient(n)

def is_coprime(a: int, b: int) -> bool:
    """Check if two numbers are coprime (have a gcd of 1)."""
    return gcd(a, b) == 1

def is_perfect_power(n: int) -> bool:
    """Check if n is a perfect power (n = a^b for some integers a > 1 and b > 1)."""
    for b in range(2, int(math.log2(n)) + 1):
        a = round(n ** (1 / b))
        if a ** b == n:
            return True
    return False

def arithmetic_series_sum(a1: int, d: int, n: int) -> int:
    """Calculate the sum of an arithmetic series with first term a1, common difference d, and n terms."""
    return n * (2 * a1 + (n - 1) * d) // 2

def geometric_series_sum(a: int, r: int, n: int) -> int:
    """Calculate the sum of a geometric series with first term a, common ratio r, and n terms."""
    if r == 1:
        return a * n
    return a * (1 - r**n) // (1 - r)

# Bit manipulation utilities
def count_bits(n: int) -> int:
    """Count the number of set bits in an integer."""
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def is_power_of_two(n: int) -> bool:
    """Check if n is a power of 2."""
    return n > 0 and (n & (n - 1)) == 0

def next_power_of_two(n: int) -> int:
    """Get the next power of 2 after n."""
    if n <= 0:
        return 1
    n -= 1
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    n |= n >> 32
    return n + 1

def log2_floor(n: int) -> int:
    """Calculate the floor of log base 2 of n."""
    return n.bit_length() - 1

def log2_ceil(n: int) -> int:
    """Calculate the ceiling of log base 2 of n."""
    return n.bit_length() if n > 0 and (n & (n - 1)) else n.bit_length() - 1

def xor_range(a: int, b: int) -> int:
    """Compute XOR of all numbers from a to b inclusive: a ^ (a+1) ^ ... ^ b."""
    return xor_from_zero(b) ^ xor_from_zero(a - 1) if a > 0 else xor_from_zero(b)

def xor_from_zero(n: int) -> int:
    """Compute XOR of all numbers from 0 to n: 0 ^ 1 ^ 2 ^ ... ^ n."""
    mod = n % 4
    if mod == 0:
        return n
    elif mod == 1:
        return 1
    elif mod == 2:
        return n + 1
    else:
        return 0

def count_set_bits_up_to_n(n: int) -> int:
    """Count the total number of set bits in all numbers from 1 to n."""
    if n <= 0:
        return 0
    
    # Find the largest power of 2 less than or equal to n
    msb_pos = log2_floor(n)
    
    # Count up to the largest power of 2
    count_up_to_power = (1 << (msb_pos - 1)) * msb_pos + 1
    
    # Count remaining bits
    remaining = n - (1 << msb_pos) + 1
    remaining_bits = remaining + count_set_bits_up_to_n(remaining - 1)
    
    return count_up_to_power + remaining_bits

# Combinatorial utilities
def binomial_coefficient(n: int, k: int) -> int:
    """Calculate the binomial coefficient C(n, k) - the number of ways to choose k items from n items."""
    if k < 0 or k > n:
        return 0
    if k > n - k:  # Take advantage of symmetry
        k = n - k
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    return result

def factorial(n: int) -> int:
    """Calculate n!"""
    return math.factorial(n)

def factorial_mod(n: int, mod: int) -> int:
    """Calculate n! % mod efficiently."""
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % mod
    return result

def combination_mod(n: int, k: int, mod: int) -> int:
    """Calculate C(n,k) % mod efficiently."""
    if k < 0 or k > n:
        return 0
    if k > n - k:
        k = n - k
    
    numerator = 1
    denominator = 1
    
    for i in range(k):
        numerator = (numerator * (n - i)) % mod
        denominator = (denominator * (i + 1)) % mod
    
    return (numerator * power_mod(denominator, mod - 2, mod)) % mod

# Common constants
MOD_SMALL = 10**9 + 7
MOD_LARGE = 998244353