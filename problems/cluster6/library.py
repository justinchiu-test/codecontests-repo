#!/usr/bin/env python3

"""
Library file for cluster6.
This contains shared code that can be imported by problems in this cluster.
"""

import sys
import os
import math
from io import BytesIO, IOBase
from functools import lru_cache, reduce
from collections import defaultdict

# Fast I/O Operations
BUFSIZE = 8192

class FastIO(IOBase):
    newlines = 0
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)

class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")

def setup_io():
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    return lambda: sys.stdin.readline().rstrip("\r\n")

# Common constants
MOD = 10**9 + 7

# Input functions
def read_int():
    """Read a single integer from input"""
    return int(input())

def read_ints():
    """Read multiple integers from a line"""
    return list(map(int, input().split()))

def read_int_tuple():
    """Read integers from a line as tuple"""
    return tuple(map(int, input().split()))

def read_float():
    """Read a single float from input"""
    return float(input())

def read_floats():
    """Read multiple floats from a line"""
    return list(map(float, input().split()))

def read_mixed_types(types):
    """Read values with specified types from a line
    Example: read_mixed_types([int, int, float]) for "5 10 0.5"
    """
    values = input().split()
    return [t(v) for t, v in zip(types, values)]

def read_array(converter=int):
    """Read an array with specified converter function"""
    return list(map(converter, input().split()))

def read_matrix(rows, cols=None, converter=int):
    """Read a matrix with rows x cols elements"""
    if cols is None:
        return [read_array(converter) for _ in range(rows)]
    return [[converter(x) for x in input().split()[:cols]] for _ in range(rows)]

def read_lines(n, strip=True):
    """Read n lines from input"""
    if strip:
        return [input().strip() for _ in range(n)]
    return [input() for _ in range(n)]

# Output functions
def print_float(value, precision=6):
    """Print a float with specified precision"""
    print(f"{value:.{precision}f}")

def print_formatted_float(value, precision=6):
    """Print a float with handling for special cases like 1.0, 0.0"""
    if abs(value - 1.0) < 1e-9:
        # Handle the case where value is very close to 1
        if precision == 6:
            print("1.000000")
        else:
            print(f"1.{'0' * precision}")
    elif abs(value) < 1e-9:
        # Handle the case where value is very close to 0
        if precision == 6:
            print("0.000000")
        else:
            print(f"0.{'0' * precision}")
    else:
        # Standard case
        print(f"{value:.{precision}f}")

def print_case(case_num, value):
    """Print in 'Case #X: Y' format"""
    print(f"Case #{case_num}: {value}")

def print_array(arr, separator=" "):
    """Print an array with the specified separator"""
    print(separator.join(map(str, arr)))

def print_probability_array(arr, precision=6):
    """Print an array of probabilities with specified precision"""
    formatted = [f"{x:.{precision}f}" for x in arr]
    print_array(formatted)

# Math utilities
def gcd(a, b):
    """Calculate greatest common divisor"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Calculate least common multiple"""
    return a * b // gcd(a, b)

def extended_gcd(a, b):
    """Extended Euclidean Algorithm
    Returns (gcd, x, y) such that a*x + b*y = gcd
    """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a, m):
    """Calculate modular multiplicative inverse
    Returns x such that (a * x) % m == 1
    """
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError("Modular inverse does not exist")
    return x % m

@lru_cache(maxsize=None)
def factorial(n):
    """Calculate factorial"""
    if n <= 1:
        return 1
    return n * factorial(n-1)

def factorial_mod(n, mod=MOD):
    """Calculate factorial with modulo"""
    result = 1
    for i in range(2, n+1):
        result = (result * i) % mod
    return result

def binomial(n, k):
    """Calculate binomial coefficient (n choose k)"""
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)
    c = 1
    for i in range(k):
        c = c * (n - i) // (i + 1)
    return c

def binomial_mod(n, k, mod=MOD):
    """Calculate binomial coefficient with modulo"""
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1

    num = 1
    den = 1
    for i in range(k):
        num = (num * (n - i)) % mod
        den = (den * (i + 1)) % mod

    return (num * pow(den, mod-2, mod)) % mod

def simplify_fraction(numerator, denominator):
    """Return simplified fraction as (numerator, denominator)"""
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
    if numerator == 0:
        return (0, 1)
    g = gcd(abs(numerator), abs(denominator))
    sign = 1 if (numerator * denominator) >= 0 else -1
    return (sign * abs(numerator) // g, abs(denominator) // g)

def fraction_to_string(numerator, denominator):
    """Convert fraction to string after simplification"""
    num, den = simplify_fraction(numerator, denominator)
    if den == 1:
        return str(num)
    return f"{num}/{den}"

# Probability functions
def probability_at_least_one(probability, attempts):
    """Calculate probability of at least one success"""
    return 1 - (1 - probability) ** attempts

def expected_value(probabilities, values):
    """Calculate expected value given probabilities and values"""
    return sum(p * v for p, v in zip(probabilities, values))

def probability_of_union(probabilities):
    """Calculate probability of union of independent events"""
    return 1 - reduce(lambda x, y: x * (1 - y), probabilities, 1)

def conditional_probability(p_a_and_b, p_b):
    """Calculate conditional probability P(A|B)"""
    if p_b == 0:
        raise ValueError("P(B) cannot be zero")
    return p_a_and_b / p_b

def markov_chain_dp(states, transition, steps, start_state=0):
    """Calculate probability distribution after steps transitions

    Args:
        states: Number of states in the Markov chain
        transition: Function taking (from_state, to_state) returning probability
        steps: Number of steps to simulate
        start_state: Initial state

    Returns:
        List of probabilities for each state
    """
    # Initial distribution
    dp = [0] * states
    dp[start_state] = 1

    # For each step
    for _ in range(steps):
        new_dp = [0] * states
        for i in range(states):
            if dp[i] > 0:  # Only consider states with non-zero probability
                for j in range(states):
                    prob = transition(i, j)
                    if prob > 0:
                        new_dp[j] += dp[i] * prob
        dp = new_dp

    return dp

# DP utilities
def memoize(func):
    """Memoization decorator for recursive functions"""
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

def init_dp_table(dimensions, initial_value=0):
    """Initialize a DP table with specified dimensions
    Example: init_dp_table([3, 4, 5], 0) for a 3x4x5 table
    """
    if not dimensions:
        return initial_value
    return [init_dp_table(dimensions[1:], initial_value) for _ in range(dimensions[0])]

def init_dp_dict():
    """Initialize a DP dictionary for sparse states"""
    return defaultdict(float)

# Efficient prime number operations
def is_prime(n):
    """Check if a number is prime"""
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

def sieve_of_eratosthenes(n):
    """Generate all primes less than or equal to n"""
    primes = []
    prime = [True for _ in range(n+1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    for p in range(2, n+1):
        if prime[p]:
            primes.append(p)
    return primes

def prime_factors(n):
    """Find all prime factors of a number"""
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors

# Combinatorial functions
def permutations(n, k=None):
    """Number of ways to arrange k elements from n distinct elements
    If k is None, calculate n!
    """
    if k is None:
        return factorial(n)
    if k < 0 or k > n:
        return 0
    return factorial(n) // factorial(n - k)

def combinations_with_replacement(n, k):
    """Number of ways to choose k elements from n elements with replacement
    Also known as (n+k-1 choose k)
    """
    return binomial(n + k - 1, k)

# Matrix operations
def matrix_multiply(A, B, mod=None):
    """Multiply matrices A and B

    Args:
        A: First matrix
        B: Second matrix
        mod: Optional modulo for results

    Returns:
        Result matrix
    """
    n, m = len(A), len(A[0])
    m2, p = len(B), len(B[0])

    if m != m2:
        raise ValueError("Matrix dimensions do not match for multiplication")

    C = [[0 for _ in range(p)] for _ in range(n)]

    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]
            if mod:
                C[i][j] %= mod

    return C

def matrix_power(A, power, mod=None):
    """Raise matrix A to the given power

    Args:
        A: Square matrix
        power: Power to raise to
        mod: Optional modulo for results

    Returns:
        Result matrix
    """
    n = len(A)
    if n != len(A[0]):
        raise ValueError("Matrix must be square for power operation")

    # Identity matrix
    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    # Binary exponentiation
    while power > 0:
        if power & 1:
            result = matrix_multiply(result, A, mod)
        A = matrix_multiply(A, A, mod)
        power >>= 1

    return result