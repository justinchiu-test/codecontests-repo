"""
Library file for cluster1.
This contains shared code that can be imported by problems in this cluster.
"""

import math
from typing import List, Dict, Set, Tuple, Optional, Union, Callable
from collections import Counter, deque
from functools import lru_cache

# I/O functions
def read_int() -> int:
    """Read a single integer from stdin."""
    return int(input())

def read_ints() -> List[int]:
    """Read multiple integers from a single line of stdin."""
    return list(map(int, input().split()))

def read_test_cases() -> int:
    """Read the number of test cases."""
    return int(input())

# Math and number theory functions
def is_prime(n: int) -> bool:
    """Check if a number is prime using trial division."""
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

def get_prime_factors(n: int) -> List[int]:
    """Get all prime factors of a number with repetition."""
    factors = []
    
    # Handle 2 separately
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Check odd numbers up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    
    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    
    return factors

def get_unique_prime_factors(n: int) -> List[int]:
    """Get unique prime factors of a number."""
    return list(set(get_prime_factors(n)))

def get_prime_factor_counts(n: int) -> Dict[int, int]:
    """Get prime factors with their counts."""
    factors = {}
    
    # Handle 2 separately
    count = 0
    while n % 2 == 0:
        count += 1
        n //= 2
    if count > 0:
        factors[2] = count
    
    # Check odd numbers up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        count = 0
        while n % i == 0:
            count += 1
            n //= i
        if count > 0:
            factors[i] = count
    
    # If n is a prime number greater than 2
    if n > 2:
        factors[n] = 1
    
    return factors

def get_divisors(n: int) -> List[int]:
    """Get all divisors of a number in ascending order."""
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

def gcd(a: int, b: int) -> int:
    """Calculate greatest common divisor using Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    """Calculate least common multiple."""
    return a * b // gcd(a, b)

def mod_pow(base: int, exp: int, mod: int) -> int:
    """Modular exponentiation: Calculate (base^exp) % mod efficiently."""
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:  # If exp is odd
            result = (result * base) % mod
        exp >>= 1  # Divide exp by 2
        base = (base * base) % mod
    return result

def phi(n: int) -> int:
    """
    Calculate Euler's totient function (phi) for n.
    Counts positive integers up to n that are relatively prime to n.
    """
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

def lcm_quotient_count(b: int) -> int:
    """
    Count the number of distinct values that can be written as lcm(a,b)/a.
    This is equivalent to counting the number of divisors of b.
    """
    return len(get_divisors(b))

def find_three_factors(n: int) -> Optional[List[int]]:
    """Find three distinct factors of n such that a*b*c = n, or None if not possible."""
    for a in range(2, int(math.sqrt(n)) + 1):
        if n % a == 0:
            n_a = n // a
            for b in range(a + 1, int(math.sqrt(n_a)) + 1):
                if n_a % b == 0:
                    c = n_a // b
                    if c > b:
                        return [a, b, c]
    return None

def count_operations_to_one(n: int) -> int:
    """
    Count operations to reduce n to 0 by repeatedly:
    1. Find smallest prime divisor d of n
    2. Subtract d from n
    """
    if is_prime(n):
        return 1

    if n % 2 == 0:
        return n // 2

    # Find the smallest prime divisor of n
    smallest_divisor = None
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            smallest_divisor = i
            break

    if smallest_divisor is None:  # n is prime
        return 1
    else:
        # After first subtraction, n-smallest_divisor is even (if n is odd)
        # So we can divide by 2 for all remaining operations
        return 1 + (n - smallest_divisor) // 2

def get_power_of_two_count(n: int) -> int:
    """Count the highest power of 2 that divides n."""
    if n == 0:
        return 0
    count = 0
    while n % 2 == 0:
        n //= 2
        count += 1
    return count

def get_power_of_three_count(n: int) -> int:
    """Count the highest power of 3 that divides n."""
    if n == 0:
        return 0
    count = 0
    while n % 3 == 0:
        n //= 3
        count += 1
    return count

def operations_to_multiply_2_divide_6(n: int) -> int:
    """
    Calculate the minimum operations to convert n to 1 using only:
    1. Multiply by 2
    2. Divide by 6 (if divisible by 6)
    Returns -1 if impossible.
    """
    if n == 1:
        return 0
    
    # Get counts of powers of 2 and 3
    factors = get_prime_factor_counts(n)
    count_2 = factors.get(2, 0)
    count_3 = factors.get(3, 0)
    
    # Check for other prime factors
    for p in factors:
        if p != 2 and p != 3:
            return -1
    
    # Check if there are enough 3s to convert to 2s
    if count_3 == 0 or count_2 > count_3:
        return -1
    
    # Each operation either adds one 2 or removes one 3 and one 2
    return 2 * count_3 - count_2

def min_operations_power_of_two(a: int, b: int) -> int:
    """
    Calculate minimum operations to transform a to b where operations are:
    1. Multiply by 2
    2. Multiply by 4
    3. Multiply by 8
    Or divide by these numbers if possible.
    Returns -1 if impossible.
    """
    if a == b:
        return 0
    
    # Ensure a is the smaller number
    if a > b:
        a, b = b, a
    
    # Check if b is divisible by a
    if b % a != 0:
        return -1
    
    # Calculate the division factor
    ratio = b // a
    
    # Check if the ratio is a power of 2
    log2_ratio = math.log2(ratio)
    if 2 ** int(log2_ratio) != ratio:
        return -1
    
    # Calculate the minimum operations
    power = int(log2_ratio)
    operations = 0
    
    # Count operations in chunks of 3, 2, and 1
    operations += power // 3
    power %= 3
    
    operations += power // 2
    power %= 2
    
    operations += power
    
    return operations

def find_max_divisible_x(p: int, q: int) -> int:
    """
    Find the maximum integer x such that:
    1. x divides p
    2. x is not divisible by q
    """
    if p % q != 0:
        return p

    # Get prime factorization of q
    q_factors = get_prime_factor_counts(q)

    # Find the divisor to remove for each prime factor
    min_divisor = float('inf')

    for prime, q_count in q_factors.items():
        # Count how many times this prime divides p
        p_copy = p
        p_count = 0
        while p_copy % prime == 0:
            p_count += 1
            p_copy //= prime

        # Calculate the divisor to remove
        divisor = prime ** (p_count - q_count + 1)
        min_divisor = min(min_divisor, divisor)

    return p // min_divisor

def find_x_for_2k_minus_1_divides_n(n: int) -> int:
    """
    Find a value x where n = x * (2^k - 1) for some k ≥ 2.
    Used in problems where we need to find a value such that n can be
    represented as x * (1 + 2 + 4 + ... + 2^(k-1))
    """
    k = 2
    while True:
        divisor = (1 << k) - 1  # 2^k - 1
        if n % divisor == 0:
            return n // divisor
        k += 1

def min_packages_for_n_items(n: int, k: int) -> int:
    """
    Find minimum number of packages needed to buy exactly n items,
    where each package can contain between 1 and k items.
    """
    if k >= n:
        return 1  # Can buy all n items at once

    divisors = get_divisors(n)
    valid_divisors = [d for d in divisors if d <= k]

    if not valid_divisors:
        return n  # No valid divisors found
    else:
        # Find the minimum packages needed
        return min(n // d for d in valid_divisors)

class Stack:
    """Simple stack implementation."""
    def __init__(self):
        self.data = []
    
    def push(self, x):
        self.data.append(x)
    
    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.data[-1]
        return None
    
    def is_empty(self):
        return len(self.data) == 0
    
    def size(self):
        return len(self.data)

def accumulate_prime_powers(x: int, n: int, mod: int = 1000000007) -> int:
    """
    Calculate the product of prime powers based on unique prime factors of x.
    For each prime factor p of x, calculate p^(n//p + n//p^2 + n//p^3 + ...)
    This is used in problems like primes and multiplication.
    """
    # Get unique prime factors of x
    unique_factors = get_unique_prime_factors(x)

    # Calculate result
    result = 1
    for d in unique_factors:
        nn = n
        while nn > 0:
            result = (result * mod_pow(d, nn // d, mod)) % mod
            nn = nn // d

    return result