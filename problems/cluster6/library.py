"""
Library file for cluster6.
This contains shared code that can be imported by problems in this cluster.
"""

import math
import os
import sys
from collections import defaultdict, Counter
from functools import lru_cache
from io import BytesIO, IOBase

# Constants
MOD = 10**9 + 7


# Math Utilities
def gcd(a, b):
    """Calculate greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Calculate least common multiple of a and b."""
    return a * b // gcd(a, b)


def simplify_fraction(num, den):
    """
    Simplify a fraction represented by numerator and denominator.
    Returns (simplified_num, simplified_den).
    """
    if den == 0:
        return (0, 1) if num == 0 else (1, 0)
    if num == 0:
        return (0, 1)
    
    g = gcd(abs(num), abs(den))
    num //= g
    den //= g
    
    if den < 0:
        num, den = -num, -den
    
    return num, den


def mod_pow(x, n, mod=MOD):
    """Calculate (x^n) % mod efficiently."""
    result = 1
    x %= mod
    while n > 0:
        if n % 2 == 1:
            result = (result * x) % mod
        x = (x * x) % mod
        n //= 2
    return result


def mod_inverse(x, mod=MOD):
    """Calculate modular multiplicative inverse of x under modulo mod."""
    return mod_pow(x, mod - 2, mod)


# Combinatorial Utilities
@lru_cache(maxsize=None)
def factorial(n, mod=None):
    """Calculate n! with optional modulo."""
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % mod if mod else result * i
    return result


@lru_cache(maxsize=None)
def factorial_mod(n, mod=MOD):
    """Calculate n! % mod efficiently."""
    return factorial(n, mod)


@lru_cache(maxsize=None)
def combination(n, k, mod=None):
    """Calculate C(n,k) = n! / (k! * (n-k)!) with optional modulo."""
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    
    if mod:
        # Use modular inverse
        return (factorial_mod(n, mod) * 
                mod_inverse(factorial_mod(k, mod), mod) * 
                mod_inverse(factorial_mod(n - k, mod), mod)) % mod
    else:
        # Direct calculation for small numbers
        return factorial(n) // (factorial(k) * factorial(n - k))


@lru_cache(maxsize=None)
def permutation(n, k, mod=None):
    """Calculate P(n,k) = n! / (n-k)! with optional modulo."""
    if k < 0 or k > n:
        return 0
    if k == 0:
        return 1
    
    if mod:
        return (factorial_mod(n, mod) * 
                mod_inverse(factorial_mod(n - k, mod), mod)) % mod
    else:
        return factorial(n) // factorial(n - k)


# Probability Utilities
def expected_value(probs, values):
    """Calculate expected value given probabilities and corresponding values."""
    return sum(p * v for p, v in zip(probs, values))


def format_probability(p, digits=6):
    """Format a probability with specified decimal places."""
    if abs(p - 1) < 1e-10:
        return f"1.{'0' * digits}"
    elif abs(p) < 1e-10:
        return f"0.{'0' * digits}"
    else:
        format_str = f"{{:.{digits}f}}"
        return format_str.format(p)


def probability_at_least_one(probs):
    """
    Calculate probability of at least one event occurring given individual probabilities.
    Using the formula: P(at least one) = 1 - P(none) = 1 - ∏(1-p_i)
    """
    prob_none = 1
    for p in probs:
        prob_none *= (1 - p)
    return 1 - prob_none


def dp_prob_memoize(func):
    """
    Memoization decorator specifically for probability DP functions.
    Handles caching for functions with state parameters.
    """
    cache = {}
    
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    
    return wrapper


# I/O Utilities
def read_int():
    """Read a single integer from input."""
    return int(input())


def read_ints():
    """Read multiple integers from a single line as a list."""
    return list(map(int, input().split()))


def read_floats():
    """Read multiple floats from a single line as a list."""
    return list(map(float, input().split()))


def read_matrix(n, m=None, converter=int):
    """Read n rows of m values as a matrix."""
    if m is None:  # Square matrix
        return [list(map(converter, input().split())) for _ in range(n)]
    return [list(map(converter, input().split())) for _ in range(n)]


def solve_multiple_cases(solve_func):
    """
    Decorator for solving multiple test cases.
    
    Example usage:
    @solve_multiple_cases
    def solve():
        n, m = read_ints()
        # rest of solution
        return answer
    """
    t = read_int()
    for _ in range(t):
        result = solve_func()
        if result is not None:
            print(result)


# Fast I/O
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


def enable_fast_io():
    """Enable fast I/O by replacing sys.stdin and sys.stdout."""
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    global input
    input = lambda: sys.stdin.readline().rstrip("\r\n")


# DP Template for Probability Problems
def memoize(func):
    """Simple memoization decorator for functions."""
    cache = {}
    
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    
    return wrapper


# Game Theory Utilities
def game_winner(n, first_player=True):
    """
    Determine the winner of a simple impartial game.
    Args:
        n: Integer state of the game
        first_player: Whether to determine if the first player wins (True) or second player wins (False)
    Returns:
        True if the player of interest wins, False otherwise
    """
    is_winning_position = n % 2 == 0  # Example rule - even positions are winning
    return is_winning_position if first_player else not is_winning_position


# Counting and Frequency Utilities
def count_frequencies(items):
    """Count frequency of each item in the list and return a dictionary."""
    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    return freq


def count_pairs(arr, condition_func):
    """
    Count pairs of elements in array that satisfy a condition.
    condition_func should take two elements and return True/False.
    """
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if condition_func(arr[i], arr[j]):
                count += 1
    return count


# Sequence-related utilities
def is_sorted(arr, reverse=False):
    """Check if an array is sorted (ascending by default)."""
    if reverse:
        return all(arr[i] >= arr[i+1] for i in range(len(arr)-1))
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))


def first_unsorted_index(arr):
    """Find the index of the first element that is out of order in a sorted array."""
    for i in range(len(arr) - 1, -1, -1):
        if i + 1 != arr[i]:
            return i
    return -1  # Array is already sorted