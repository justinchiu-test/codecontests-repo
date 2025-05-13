"""
Library file for cluster5.
This contains shared code that can be imported by problems in this cluster.
"""

import sys
from typing import List, Tuple, Dict, Set, Optional, Any, Union, Callable
from collections import defaultdict, deque, Counter

# Common constants
MOD_1 = 10**9 + 7
MOD_2 = 998244353

# ================= Input/Output Utilities =================

def read_int() -> int:
    """Read a single integer from stdin."""
    return int(input())

def read_ints() -> List[int]:
    """Read a list of integers from stdin."""
    return list(map(int, input().split()))

def read_int_tuple() -> Tuple[int, ...]:
    """Read a tuple of integers from stdin."""
    return tuple(map(int, input().split()))

def read_str() -> str:
    """Read a string from stdin."""
    return input().strip()

def read_strs() -> List[str]:
    """Read a list of strings from stdin."""
    return input().split()

def setup_fast_io():
    """Setup fast I/O by replacing input with sys.stdin.readline."""
    global input
    input = sys.stdin.readline
    sys.setrecursionlimit(10**5)

# ================= String Algorithms =================

def z_algorithm(s: str) -> List[int]:
    """
    Z-algorithm for string pattern matching.
    Returns an array z where z[i] is the length of the longest substring starting at i
    which is also a prefix of the string.
    """
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(z[i - l], r - i + 1)
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z

def longest_common_prefix(s: str, t: str) -> int:
    """Find length of longest common prefix between two strings."""
    min_len = min(len(s), len(t))
    for i in range(min_len):
        if s[i] != t[i]:
            return i
    return min_len

def is_subsequence(s: str, t: str) -> bool:
    """Check if s is a subsequence of t."""
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)

def count_subsequences(s: str, t: str, mod: int = MOD_2) -> int:
    """Count number of occurrences of t as a subsequence in s."""
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Empty string is a subsequence of any string once
    for i in range(n + 1):
        dp[i][0] = 1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % mod
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[n][m]

def build_next_char_positions(s: str) -> List[List[int]]:
    """
    Build a table of next positions for each character.
    nxt[c][i] = next position of character c after position i in string s.
    """
    n = len(s)
    nxt = [[n + 1] * (n + 2) for _ in range(26)]
    
    for i in range(n - 1, -1, -1):
        # Skip the first character ('!') for 1-indexed strings
        if i < n and i >= 0:
            c = ord(s[i]) - ord('a') if 'a' <= s[i] <= 'z' else -1
            for j in range(26):
                nxt[j][i] = nxt[j][i + 1]
            if 0 <= c < 26:
                nxt[c][i] = i
    
    return nxt

def precompute_equal_words(words: List[str]) -> List[List[bool]]:
    """
    Precompute whether words[i] == words[j] for all pairs i, j.
    Returns a 2D boolean matrix.
    """
    n = len(words)
    eq = [[False] * n for _ in range(n)]
    for i in range(n):
        eq[i][i] = True
        for j in range(i):
            eq[i][j] = eq[j][i] = words[i] == words[j]
    return eq

# ================= Dynamic Programming Utilities =================

def init_dp_1d(size: int, default: Any = 0) -> List[Any]:
    """Initialize a 1D DP array with a default value."""
    return [default] * size

def init_dp_2d(rows: int, cols: int, default: Any = 0) -> List[List[Any]]:
    """Initialize a 2D DP array with a default value."""
    return [[default] * cols for _ in range(rows)]

def init_dp_3d(dim1: int, dim2: int, dim3: int, default: Any = 0) -> List[List[List[Any]]]:
    """Initialize a 3D DP array with a default value."""
    return [[[default] * dim3 for _ in range(dim2)] for _ in range(dim1)]

# ================= Modular Arithmetic =================

def mod_add(a: int, b: int, mod: int = MOD_2) -> int:
    """Modular addition."""
    return (a + b) % mod

def mod_sub(a: int, b: int, mod: int = MOD_2) -> int:
    """Modular subtraction."""
    return (a - b) % mod

def mod_mul(a: int, b: int, mod: int = MOD_2) -> int:
    """Modular multiplication."""
    return (a * b) % mod

def mod_pow(base: int, exponent: int, mod: int = MOD_2) -> int:
    """Modular exponentiation."""
    result = 1
    base %= mod
    while exponent > 0:
        if exponent & 1:
            result = (result * base) % mod
        exponent >>= 1
        base = (base * base) % mod
    return result

def mod_inv(a: int, mod: int = MOD_2) -> int:
    """Modular multiplicative inverse using Fermat's little theorem."""
    return mod_pow(a, mod - 2, mod)

# ================= Data Structures =================

class SegmentTree:
    """
    Segment tree with point updates and range queries.
    Supports multiple columns of data per node.
    """
    def __init__(self, n, columns=1):
        self.tree = [[0] * columns for _ in range(n << 1)]  # columns per node
        self.n = n

    def query(self, r, col=0):
        """Query the sum in range [0, r) for column col"""
        res = 0
        l = self.n
        r += self.n

        while l < r:
            if l & 1:
                res += self.tree[l][col]
                l += 1

            if r & 1:
                r -= 1
                res += self.tree[r][col]

            l >>= 1
            r >>= 1

        return res
    
    def query_range(self, l, r, col=0):
        """Query the sum in range [l, r) for column col"""
        res = 0
        l += self.n
        r += self.n

        while l < r:
            if l & 1:
                res += self.tree[l][col]
                l += 1

            if r & 1:
                r -= 1
                res += self.tree[r][col]

            l >>= 1
            r >>= 1

        return res

    def update(self, ix, val, col=0):
        """Add val to position ix in column col"""
        ix += self.n

        # Update value
        self.tree[ix][col] += val

        # Propagate changes upward
        while ix > 1:
            self.tree[ix >> 1][col] = self.tree[ix][col] + self.tree[ix ^ 1][col]
            ix >>= 1

class FenwickTree:
    """
    Binary Indexed Tree (BIT) for efficient range sum queries and point updates.
    """
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def update(self, i, val):
        """Add val to position i"""
        while i <= self.n:
            self.tree[i] += val
            i += i & -i
    
    def query(self, i):
        """Get sum of elements from 1 to i"""
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res
    
    def range_query(self, l, r):
        """Get sum of elements from l to r inclusive"""
        return self.query(r) - self.query(l - 1)

# ================= Utility Functions =================

def generate_matrix_indices(rows: int, cols: int) -> List[Tuple[int, int]]:
    """Generate all (i, j) indices for a matrix of size rows x cols."""
    return [(i, j) for i in range(rows) for j in range(cols)]

def idx_3d(i: int, j: int, k: int, dim2: int = 256, dim3: int = 256) -> int:
    """Convert 3D indices to 1D for compact DP."""
    return i * dim2 * dim3 + j * dim3 + k

def flatten_array(arr: List[List[Any]]) -> List[Any]:
    """Flatten a 2D array to 1D."""
    return [item for sublist in arr for item in sublist]