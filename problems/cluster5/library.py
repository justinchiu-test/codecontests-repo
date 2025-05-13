"""
Shared library for cluster5 problems.
Provides common I/O routines and string algorithms.
"""
import sys
import math
import bisect

def read():
    """Read a line from stdin and strip trailing newline."""
    return sys.stdin.readline().rstrip("\n")

def readint():
    """Read a single integer from a line."""
    return int(read())

def readints():
    """Read a line of space-separated integers."""
    return list(map(int, read().split()))

def read_all_ints():
    """Read all integers from stdin (splitting on whitespace)."""
    data = sys.stdin.read().split()
    return list(map(int, data))

MOD = 10**9 + 7

def z_function(s):
    """Compute Z-function of list or string s."""
    n = len(s)
    z = [0] * n
    l = r = 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z

zfunc = z_function

def prefix_function(s):
    """Compute prefix (failure) function of string or list s."""
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi

def lower_bound(a, x):
    """First index in sorted list a where a[idx] >= x."""
    return bisect.bisect_left(a, x)

def upper_bound(a, x):
    """First index in sorted list a where a[idx] > x."""
    return bisect.bisect_right(a, x)

def gcd(a, b):
    """Greatest common divisor."""
    return math.gcd(a, b)

def lcm(a, b):
    """Least common multiple."""
    return a // math.gcd(a, b) * b

class BIT:
    """Fenwick Tree / Binary Indexed Tree for prefix sums."""
    def __init__(self, n):
        self.n = n
        self.fw = [0] * (n + 1)

    def update(self, i, v):
        """Add v at index i (1-based)."""
        while i <= self.n:
            self.fw[i] += v
            i += i & -i

    def query(self, i):
        """Sum of prefix [1..i]."""
        s = 0
        while i > 0:
            s += self.fw[i]
            i -= i & -i
        return s

    def range_query(self, l, r):
        """Sum of range [l..r]."""
        return self.query(r) - self.query(l - 1)

# Modular arithmetic utilities
def addmod(a, b):
    return (a + b) % MOD

def submod(a, b):
    return (a - b) % MOD

def mulmod(a, b):
    return (a * b) % MOD

def powmod(a, e, mod=MOD):
    return pow(a, e, mod)

# Combinatorics utilities
_fact = [1]
_inv_fact = [1]
_fact_n = 0

def init_fact(n):
    """Initialize factorial and inverse factorial up to n."""
    global _fact, _inv_fact, _fact_n
    if n <= _fact_n:
        return
    _fact = [1] * (n + 1)
    for i in range(1, n + 1):
        _fact[i] = _fact[i - 1] * i % MOD
    _inv_fact = [1] * (n + 1)
    _inv_fact[n] = pow(_fact[n], MOD - 2, MOD)
    for i in range(n, 0, -1):
        _inv_fact[i - 1] = _inv_fact[i] * i % MOD
    _fact_n = n

def comb(n, k):
    """Compute C(n, k) modulo MOD."""
    if k < 0 or k > n:
        return 0
    init_fact(n)
    return _fact[n] * _inv_fact[k] % MOD * _inv_fact[n - k] % MOD
