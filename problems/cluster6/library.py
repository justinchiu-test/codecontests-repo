"""
Library file for cluster6.
This contains shared code that can be imported by problems in this cluster.
"""
import sys
import math
import os
from collections import defaultdict, Counter, deque
from fractions import Fraction
from functools import lru_cache, reduce
from itertools import combinations, permutations
from bisect import bisect_left, bisect_right

# Constants
MOD = 10**9 + 7

# Ensure parent directory is in path for importing this library
def ensure_library_path():
    """Add parent directory to path to ensure library can be imported."""
    current_file = os.path.abspath(__file__)
    parent_dir = os.path.dirname(current_file)
    if parent_dir not in sys.path:
        sys.path.append(parent_dir)

# Input/Output Utilities
def read_int():
    """Read a single integer from input."""
    return int(input())

def read_ints():
    """Read multiple integers from input."""
    return list(map(int, input().split()))

def read_float():
    """Read a single float from input."""
    return float(input())

def read_floats():
    """Read multiple floats from input."""
    return list(map(float, input().split()))

def read_str():
    """Read a single string from input."""
    return input().strip()

def read_strs():
    """Read multiple strings from input."""
    return input().split()

def read_line():
    """Read a line from system input."""
    return sys.stdin.readline().strip()

def read_matrix(n, value_type=int):
    """Read an n×m matrix from input."""
    return [list(map(value_type, input().split())) for _ in range(n)]

def print_float_exact(value, precision=12):
    """Print a float with exact precision to match expected output format."""
    print(f"{value:.{precision}f}")

def print_list(lst, sep=" "):
    """Print a list with specified separator."""
    print(sep.join(map(str, lst)))

# Number Theory Utilities
def gcd(a, b):
    """Compute the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Compute the least common multiple of a and b."""
    return a * b // gcd(a, b)

def mod_pow(x, y, m=MOD):
    """Compute (x^y) % m efficiently."""
    if y == 0:
        return 1
    p = mod_pow(x, y // 2, m) % m
    p = (p * p) % m
    return p if y % 2 == 0 else (x * p) % m

def mod_inverse(x, m=MOD):
    """Compute the modular multiplicative inverse of x modulo m."""
    return mod_pow(x, m - 2, m)

def chinese_remainder(remainders, moduli):
    """Solve the Chinese Remainder Theorem for the given remainders and moduli."""
    if len(remainders) != len(moduli):
        raise ValueError("Number of remainders must equal number of moduli")
    
    total = 0
    prod = reduce(lambda a, b: a * b, moduli)
    
    for r_i, m_i in zip(remainders, moduli):
        p = prod // m_i
        total += r_i * p * mod_inverse(p, m_i)
    
    return total % prod

def prime_factors(n):
    """Find all prime factors of n."""
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def sieve_of_eratosthenes(n):
    """Generate all primes up to n using the Sieve of Eratosthenes."""
    primes = []
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    
    for p in range(2, n + 1):
        if prime[p]:
            primes.append(p)
    
    return primes

# Combinatorics Utilities
@lru_cache(maxsize=None)
def factorial(n, m=MOD):
    """Compute n! % m efficiently."""
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % m
    return result

def combination(n, k, m=MOD):
    """Compute nCk % m efficiently."""
    if k < 0 or k > n:
        return 0
    return (factorial(n) * mod_inverse(factorial(k) * factorial(n - k) % m, m)) % m

def permutation(n, k, m=MOD):
    """Compute nPk % m efficiently."""
    if k < 0 or k > n:
        return 0
    return (factorial(n) * mod_inverse(factorial(n - k), m)) % m

def multinomial(counts, m=MOD):
    """Compute multinomial coefficient % m efficiently."""
    n = sum(counts)
    result = factorial(n, m)
    for count in counts:
        result = (result * mod_inverse(factorial(count, m), m)) % m
    return result

# Fractions and Probability Utilities
def fraction_to_str(numerator, denominator):
    """Convert a fraction to a simplified string representation."""
    g = gcd(numerator, denominator)
    return f"{numerator//g}/{denominator//g}"

def simplify_fraction(numerator, denominator):
    """Simplify a fraction and return numerator and denominator."""
    g = gcd(numerator, denominator)
    return numerator // g, denominator // g

# Dynamic Programming Utilities
def memoize(f):
    """Simple memoization decorator."""
    memo = {}
    def helper(*args):
        if args not in memo:
            memo[args] = f(*args)
        return memo[args]
    return helper

# Probability DP utilities
def expected_value(probabilities, values):
    """Compute the expected value given probabilities and values."""
    return sum(p * v for p, v in zip(probabilities, values))

# Matrix operations
def matrix_multiply(A, B, mod=None):
    """Multiply two matrices A and B."""
    n, m1 = len(A), len(A[0])
    m2, p = len(B), len(B[0])
    assert m1 == m2, "Matrix dimensions don't match for multiplication"
    
    C = [[0 for _ in range(p)] for _ in range(n)]
    for i in range(n):
        for j in range(p):
            for k in range(m1):
                C[i][j] += A[i][k] * B[k][j]
                if mod:
                    C[i][j] %= mod
    return C

def matrix_power(A, n, mod=None):
    """Compute A^n using binary exponentiation."""
    size = len(A)
    result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    
    while n > 0:
        if n % 2 == 1:
            result = matrix_multiply(result, A, mod)
        A = matrix_multiply(A, A, mod)
        n //= 2
    
    return result

# Game theory utilities
def mex(s):
    """Find the minimum excluded value in a set of non-negative integers."""
    i = 0
    while i in s:
        i += 1
    return i

def grundy_number(position, transition_function, memo=None):
    """Compute the Grundy number for a game position."""
    if memo is None:
        memo = {}
    
    if position in memo:
        return memo[position]
    
    next_positions = transition_function(position)
    next_grundies = {grundy_number(pos, transition_function, memo) for pos in next_positions}
    
    result = mex(next_grundies)
    memo[position] = result
    return result

# Multi-dimensional dynamic programming utilities
def dp_array_1d(size, default=0):
    """Create a 1D array for dynamic programming with a default value."""
    return [default] * size

def dp_array_2d(rows, cols, default=0):
    """Create a 2D array for dynamic programming with a default value."""
    return [[default for _ in range(cols)] for _ in range(rows)]

def dp_array_3d(dim1, dim2, dim3, default=0):
    """Create a 3D array for dynamic programming with a default value."""
    return [[[default for _ in range(dim3)] for _ in range(dim2)] for _ in range(dim1)]

# Custom data structures
class DisjointSet:
    """Disjoint Set Union-Find data structure."""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1
    
    def are_connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def count_sets(self):
        """Count the number of disjoint sets."""
        return sum(1 for i in range(len(self.parent)) if self.parent[i] == i)

class SegmentTree:
    """Segment Tree data structure for range queries and updates."""
    def __init__(self, arr, operation=min, identity_element=float('inf')):
        self.n = len(arr)
        self.operation = operation
        self.identity_element = identity_element
        self.tree = [identity_element] * (4 * self.n)
        self._build(arr, 0, 0, self.n - 1)
    
    def _build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
            return
        
        mid = (start + end) // 2
        self._build(arr, 2 * node + 1, start, mid)
        self._build(arr, 2 * node + 2, mid + 1, end)
        self.tree[node] = self.operation(self.tree[2 * node + 1], self.tree[2 * node + 2])
    
    def query(self, left, right):
        """Query the operation result in the range [left, right]."""
        return self._query(0, 0, self.n - 1, left, right)
    
    def _query(self, node, start, end, left, right):
        if right < start or left > end:
            return self.identity_element
        
        if left <= start and end <= right:
            return self.tree[node]
        
        mid = (start + end) // 2
        left_val = self._query(2 * node + 1, start, mid, left, right)
        right_val = self._query(2 * node + 2, mid + 1, end, left, right)
        return self.operation(left_val, right_val)
    
    def update(self, index, value):
        """Update the value at index."""
        self._update(0, 0, self.n - 1, index, value)
    
    def _update(self, node, start, end, index, value):
        if start == end:
            self.tree[node] = value
            return
        
        mid = (start + end) // 2
        if index <= mid:
            self._update(2 * node + 1, start, mid, index, value)
        else:
            self._update(2 * node + 2, mid + 1, end, index, value)
        
        self.tree[node] = self.operation(self.tree[2 * node + 1], self.tree[2 * node + 2])