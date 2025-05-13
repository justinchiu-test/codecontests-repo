"""
Library file for cluster1.
This contains shared code that can be imported by problems in this cluster.
"""
import math
import sys
from collections import defaultdict, Counter

# IO Utilities
def read_int():
    """Read a single integer from stdin."""
    return int(input())

def read_ints():
    """Read multiple integers from a line in stdin."""
    return map(int, input().split())

def read_int_list():
    """Read a list of integers from stdin."""
    return list(map(int, input().split()))

def read_lines(n):
    """Read n lines of input."""
    return [input() for _ in range(n)]

def read_test_cases(parser_func):
    """
    Read multiple test cases using the provided parser function.
    
    Args:
        parser_func: Function that parses a single test case
        
    Returns:
        list: Results from processing each test case
    """
    t = read_int()
    return [parser_func() for _ in range(t)]

# Number Theory - Prime Functions
def is_prime(n):
    """
    Check if a number is prime using an optimized method.
    
    Args:
        n: The number to check
        
    Returns:
        bool: True if n is prime, False otherwise
    """
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

def get_prime_factors(n):
    """
    Get all prime factors of a number.
    
    Args:
        n: The number to factorize
        
    Returns:
        list: List of prime factors (not unique, with repetition)
    """
    factors = []
    
    # Handle divisions by 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Handle divisions by odd numbers
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    
    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    
    return factors

def get_unique_prime_factors(n):
    """
    Get all unique prime factors of a number.
    
    Args:
        n: The number to factorize
        
    Returns:
        list: List of unique prime factors
    """
    factors = []
    
    # Handle divisions by 2
    if n % 2 == 0:
        factors.append(2)
        while n % 2 == 0:
            n //= 2
    
    # Handle divisions by odd numbers
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n //= i
    
    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    
    return factors

def get_prime_factors_with_counts(n):
    """
    Get prime factorization with count of each prime factor.
    
    Args:
        n: The number to factorize
        
    Returns:
        dict: Dictionary mapping prime factors to their counts
    """
    factors = defaultdict(int)
    
    # Handle divisions by 2
    while n % 2 == 0:
        factors[2] += 1
        n //= 2
    
    # Handle divisions by odd numbers
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors[i] += 1
            n //= i
    
    # If n is a prime number greater than 2
    if n > 2:
        factors[n] += 1
    
    return factors

def get_smallest_prime_factor(n):
    """
    Find the smallest prime factor of a number.
    
    Args:
        n: The number to factorize
        
    Returns:
        int: The smallest prime factor
    """
    if n % 2 == 0:
        return 2
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i
    
    return n  # n is prime

def generate_primes_up_to(n):
    """
    Generate all primes up to n using Sieve of Eratosthenes.
    
    Args:
        n: Upper limit
        
    Returns:
        list: All prime numbers up to n
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    
    return [i for i in range(2, n+1) if sieve[i]]

# Number Theory - Divisors
def get_all_divisors(n):
    """
    Get all divisors of a number in sorted order.
    
    Args:
        n: The number to find divisors for
        
    Returns:
        list: Sorted list of all divisors
    """
    small, large = [], []
    
    # Optimization if n is odd - only check odd divisors
    step = 2 if n % 2 != 0 else 1
    
    for i in range(1, int(math.sqrt(n)) + 1, step):
        if n % i == 0:
            small.append(i)
            if i != n // i:  # Avoid duplicates for perfect squares
                large.append(n // i)
    
    # Combine the lists
    large.reverse()
    return small + large

def count_divisors(n):
    """
    Count the number of divisors for a number.
    
    Args:
        n: The number to count divisors for
        
    Returns:
        int: Count of divisors
    """
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            # If divisors are equal, count only one
            if n // i == i:
                count += 1
            else:  # Otherwise count both
                count += 2
    return count

def count_divisors_from_prime_factors(factors):
    """
    Count divisors using prime factorization.
    
    Args:
        factors: Dictionary of prime factors and their exponents
        
    Returns:
        int: Total number of divisors
    """
    result = 1
    for exponent in factors.values():
        result *= (exponent + 1)
    return result

# Number Theory - GCD, LCM and related
def gcd(a, b):
    """
    Calculate greatest common divisor using Euclidean algorithm.
    
    Args:
        a, b: The numbers to find GCD for
        
    Returns:
        int: The GCD of a and b
    """
    while b:
        a, b = b, a % b
    return a

def gcd_of_list(numbers):
    """
    Calculate GCD of a list of numbers.
    
    Args:
        numbers: List of integers
        
    Returns:
        int: GCD of all numbers
    """
    result = numbers[0]
    for num in numbers[1:]:
        result = gcd(result, num)
    return result

def lcm(a, b):
    """
    Calculate least common multiple.
    
    Args:
        a, b: The numbers to find LCM for
        
    Returns:
        int: The LCM of a and b
    """
    return a * b // gcd(a, b)

def lcm_of_list(numbers):
    """
    Calculate LCM of a list of numbers.
    
    Args:
        numbers: List of integers
        
    Returns:
        int: LCM of all numbers
    """
    result = numbers[0]
    for num in numbers[1:]:
        result = lcm(result, num)
    return result

def extended_gcd(a, b):
    """
    Extended Euclidean Algorithm.
    
    Args:
        a, b: The numbers to find coefficients for
        
    Returns:
        tuple: (gcd, x, y) where ax + by = gcd
    """
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)

def euler_totient(n):
    """
    Calculate Euler's totient function φ(n).
    
    Args:
        n: The number to calculate φ(n) for
        
    Returns:
        int: The value of φ(n)
    """
    result = n  # Initialize result as n
    
    # Consider all prime factors of n and subtract their multiples
    p = 2
    while p * p <= n:
        # Check if p is a prime factor
        if n % p == 0:
            # If yes, then update n and result
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    
    # If n has a prime factor greater than sqrt(n)
    if n > 1:
        result -= result // n
    
    return result

def euler_totient_from_factors(factors):
    """
    Calculate Euler's totient from prime factorization.
    
    Args:
        factors: Dictionary of prime factors and their exponents
        
    Returns:
        int: The value of φ(n)
    """
    result = 1
    for prime, exponent in factors.items():
        result *= (prime - 1) * (prime ** (exponent - 1))
    return result

# Number Theory - Modular arithmetic
MOD = 10**9 + 7

def mod_pow(base, exponent, mod=MOD):
    """
    Calculate (base^exponent) % mod efficiently.
    
    Args:
        base: The base number
        exponent: The exponent
        mod: The modulus (default is 10^9 + 7)
        
    Returns:
        int: The result of (base^exponent) % mod
    """
    result = 1
    base %= mod
    
    while exponent > 0:
        # If exponent is odd, multiply result with base
        if exponent & 1:
            result = (result * base) % mod
        # Exponent = exponent / 2
        exponent >>= 1
        # Base = base^2
        base = (base * base) % mod
    
    return result

def mod_inverse(a, mod=MOD):
    """
    Calculate modular multiplicative inverse.
    
    Args:
        a: The number to find inverse for
        mod: The modulus (default is 10^9 + 7)
        
    Returns:
        int: The modular multiplicative inverse of a under mod
    """
    g, x, y = extended_gcd(a, mod)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % mod

def mod_factorial(n, mod=MOD):
    """
    Calculate factorial modulo mod: n! % mod.
    
    Args:
        n: The number to calculate factorial for
        mod: The modulus (default is 10^9 + 7)
        
    Returns:
        int: n! % mod
    """
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % mod
    return result

def mod_binomial(n, k, mod=MOD):
    """
    Calculate binomial coefficient nCk modulo mod.
    
    Args:
        n, k: Parameters for the binomial coefficient
        mod: The modulus (default is 10^9 + 7)
        
    Returns:
        int: nCk % mod
    """
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    
    # Calculate using modular inverse
    num = 1
    for i in range(n, n-k, -1):
        num = (num * i) % mod
        
    denom = 1
    for i in range(1, k+1):
        denom = (denom * i) % mod
        
    return (num * mod_inverse(denom, mod)) % mod

# Utility functions
def is_power_of_two(n):
    """
    Check if a number is a power of 2.
    
    Args:
        n: The number to check
        
    Returns:
        bool: True if n is a power of 2, False otherwise
    """
    return n > 0 and (n & (n - 1)) == 0

def count_bits(n):
    """
    Count the number of set bits in the binary representation.
    
    Args:
        n: The number to check
        
    Returns:
        int: The number of set bits
    """
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def highest_power_of_2_less_than(n):
    """
    Find the highest power of 2 less than or equal to n.
    
    Args:
        n: The upper bound
        
    Returns:
        int: Highest power of 2 <= n
    """
    return 1 << (n.bit_length() - 1)

def is_power_of(n, base):
    """
    Check if a number is a power of the given base.
    
    Args:
        n: The number to check
        base: The base
        
    Returns:
        bool: True if n is a power of base, False otherwise
    """
    if n <= 0 or base <= 0:
        return False
    if n == 1:
        return True
    if base == 1:
        return n == 1
    
    # Try to divide n by base until we can't anymore
    while n > 1 and n % base == 0:
        n //= base
    
    # If n is 1, it means n was a power of base
    return n == 1

def inclusion_exclusion(universe_size, subsets, subset_sizes, negate=False):
    """
    Apply the inclusion-exclusion principle to count elements.
    
    Args:
        universe_size: Size of the universal set
        subsets: List of subsets to include/exclude
        subset_sizes: Function to compute the size of intersection of given subsets
        negate: Whether to compute complementary set (default: False)
        
    Returns:
        int: The size of the union or intersection of sets
    """
    n = len(subsets)
    result = 0
    
    # Iterate through all possible combinations of subsets
    for mask in range(1, 1 << n):
        # Count the number of sets in the current combination
        bit_count = count_bits(mask)
        
        # Get the indices of sets in the current combination
        indices = [i for i in range(n) if (mask & (1 << i))]
        
        # Get the size of the intersection of these sets
        intersection_size = subset_sizes([subsets[i] for i in indices])
        
        # Add or subtract based on the parity of the number of sets
        if bit_count % 2 == 1:
            result += intersection_size
        else:
            result -= intersection_size
    
    # If we want the complement, return universe_size - result
    return universe_size - result if negate else result