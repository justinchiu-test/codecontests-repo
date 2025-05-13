"""
Library file for cluster6.
This contains shared code that can be imported by problems in this cluster.
"""
import sys

# Input/Output Utilities
def read_int():
    """Read a single integer from stdin."""
    return int(sys.stdin.readline())

def read_ints():
    """Read multiple integers from a single line."""
    return list(map(int, sys.stdin.readline().split()))

def read_float():
    """Read a single float from stdin."""
    return float(sys.stdin.readline())

def read_floats():
    """Read multiple floats from a single line."""
    return list(map(float, sys.stdin.readline().split()))

def read_str():
    """Read a stripped string from stdin."""
    return sys.stdin.readline().strip()

# Mathematical Utilities
MOD = 10**9 + 7

def gcd(a, b):
    """Greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Least common multiple of a and b."""
    return a * b // gcd(a, b)

def mod_pow(x, y, m=MOD):
    """Fast modular exponentiation: x^y % m."""
    res = 1
    x %= m
    while y > 0:
        if y & 1:
            res = (res * x) % m
        x = (x * x) % m
        y >>= 1
    return res

def mod_inverse(x, m=MOD):
    """Modular multiplicative inverse of x under mod m."""
    return mod_pow(x, m - 2, m)

def factorial(n, m=MOD):
    """Compute n! % m."""
    res = 1
    for i in range(1, n + 1):
        res = res * i % m
    return res

def combination(n, k, m=MOD):
    """Compute C(n, k) % m."""
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    num = 1
    den = 1
    for i in range(1, k + 1):
        num = num * (n - i + 1) % m
        den = den * i % m
    return num * mod_inverse(den, m) % m

def simplify_fraction(n, d):  # noqa: E741
    """Simplify fraction n/d to lowest terms."""
    g = gcd(n, d)
    return n // g, d // g

# Probability Utilities
def expected_value(probs, vals):
    """Expected value given probabilities and values."""
    return sum(p * v for p, v in zip(probs, vals))

def conditional_probability(p_and, p_cond):
    """Compute P(A|B) = P(A∩B) / P(B)."""
    return p_and / p_cond if p_cond else 0

# Dynamic Programming Utilities
def memoize(func):
    """Decorator to memoize function results."""
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        res = func(*args)
        cache[args] = res
        return res
    return wrapper

# Specific Utilities
def probability_transition(states, transitions, initial=None):
    """Compute new distribution after one transition step."""
    if initial is None:
        initial = {s: 1.0 / len(states) for s in states}
    result = {s: 0.0 for s in states}
    for s, p in initial.items():
        for t, tp in transitions.get(s, {}).items():
            result[t] = result.get(t, 0.0) + p * tp
    return result

def matrix_multiply(A, B, mod=MOD):
    """Multiply matrices A and B under modulo."""
    n, m = len(A), len(B[0])
    p = len(B)
    C = [[0] * m for _ in range(n)]
    for i in range(n):
        for k in range(p):
            aik = A[i][k]
            for j in range(m):
                C[i][j] = (C[i][j] + aik * B[k][j]) % mod
    return C

def matrix_power(A, exp, mod=MOD):
    """Compute matrix A to the power exp under modulo."""
    n = len(A)
    # identity matrix
    R = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    while exp > 0:
        if exp & 1:
            R = matrix_multiply(R, A, mod)
        A = matrix_multiply(A, A, mod)
        exp >>= 1
    return R
