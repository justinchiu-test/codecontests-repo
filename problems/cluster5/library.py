"""
Library file for cluster5.
This contains shared code that can be imported by problems in this cluster.
"""

import os
import sys
from io import BytesIO, IOBase
from functools import lru_cache, wraps
from collections import defaultdict, Counter, deque
from typing import List, Tuple, Dict, Set, Optional, Callable, Any, Union

# Constants
MOD = 10**9 + 7

# ===== Input/Output Utilities =====

def read_int():
    """Read a single integer from input"""
    return int(input())

def read_ints():
    """Read a list of integers from input"""
    return list(map(int, input().split()))

def read_int_tuple():
    """Read integers as a tuple"""
    return tuple(map(int, input().split()))

def read_strings():
    """Read space-separated strings"""
    return input().split()

def read_matrix(n: int, m: Optional[int] = None, dtype=int):
    """
    Read an n×m matrix from input
    
    Args:
        n: Number of rows
        m: Number of columns (if None, determined from first row)
        dtype: Type to convert elements to
    
    Returns:
        2D list representing the matrix
    """
    matrix = []
    for _ in range(n):
        row = list(map(dtype, input().split()))
        if m is None:
            m = len(row)
        elif len(row) != m:
            raise ValueError(f"Expected {m} elements in row, got {len(row)}")
        matrix.append(row)
    return matrix

class FastIO(IOBase):
    """Fast IO implementation for competitive programming"""
    newlines = 0
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
    
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, 8192))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
    
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, 8192))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
    
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)

def setup_fast_io():
    """Setup fast IO for competitive programming"""
    class IOWrapper(IOBase):
        def __init__(self, file):
            self.buffer = FastIO(file)
            self.flush = self.buffer.flush
            self.writable = self.buffer.writable
            self.write = lambda s: self.buffer.write(s.encode("ascii"))
            self.read = lambda: self.buffer.read().decode("ascii")
            self.readline = lambda: self.buffer.readline().decode("ascii")
    
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    return lambda: sys.stdin.readline().rstrip("\r\n")

# ===== String Algorithms =====

def build_next_occurrence(s, alphabet_size=26, offset=97):
    """
    Build next occurrence array for string s.
    nxt[c][i] is the next position of character c after position i.
    
    Args:
        s: String to process (1-indexed with sentinel character at s[0])
        alphabet_size: Size of the alphabet (default: 26 for lowercase English)
        offset: ASCII offset for the alphabet (default: 97 for 'a')
    
    Returns:
        nxt: 2D array where nxt[c][i] is the next position of character c after position i
    """
    n = len(s) - 1  # Skip sentinel character
    nxt = [[n + 1] * (n + 2) for _ in range(alphabet_size)]
    
    for i in range(n - 1, -1, -1):
        c = ord(s[i + 1]) - offset
        for j in range(alphabet_size):
            nxt[j][i] = nxt[j][i + 1]
        nxt[c][i] = i + 1
    
    return nxt

def build_prev_occurrence(s, alphabet_size=26, offset=97):
    """
    Build previous occurrence array for string s.
    prev[c][i] is the previous position of character c before position i.
    
    Args:
        s: String to process (0-indexed)
        alphabet_size: Size of the alphabet (default: 26 for lowercase English)
        offset: ASCII offset for the alphabet (default: 97 for 'a')
    
    Returns:
        prev: 2D array where prev[c][i] is the previous position of character c before position i
    """
    n = len(s)
    prev = [[-1] * (n + 1) for _ in range(alphabet_size)]
    
    for i in range(1, n + 1):
        c = ord(s[i - 1]) - offset
        for j in range(alphabet_size):
            prev[j][i] = prev[j][i - 1]
        prev[c][i] = i - 1
    
    return prev

def z_algorithm(s):
    """
    Compute Z-function for string s or sequence.
    Z[i] is the length of the longest substring/subsequence starting at i
    which is also a prefix of s.
    
    Args:
        s: String or sequence to process
    
    Returns:
        z: Array where z[i] is the length of the longest common prefix of s and s[i:]
    """
    n = len(s)
    z = [0] * n
    # For strings, z[0] is typically n, but for general sequences 
    # we compute it explicitly for consistency
    l, r = 0, 0
    
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    
    return z

def is_subsequence(a, b):
    """
    Check if string a is a subsequence of string b.
    
    Args:
        a: String to check if it's a subsequence
        b: String to check in
    
    Returns:
        bool: True if a is a subsequence of b, False otherwise
    """
    it = iter(b)
    return all(c in it for c in a)

def kmp_prefix_function(s):
    """
    Compute the Knuth-Morris-Pratt prefix function.
    
    Args:
        s: String to compute prefix function for
    
    Returns:
        pi: Array where pi[i] is the length of the longest proper prefix 
            which is also a suffix of s[0:i+1]
    """
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

# ===== Dynamic Programming Utilities =====

def memoize(f):
    """Memoization decorator for functions"""
    cache = {}
    
    @wraps(f)
    def decorator(*args):
        if args in cache:
            return cache[args]
        result = f(*args)
        cache[args] = result
        return result
    
    return decorator

def initialize_dp_table(dimensions, default_value=0):
    """
    Initialize a multi-dimensional DP table.
    
    Args:
        dimensions: List of dimensions
        default_value: Default value for the DP table
    
    Returns:
        dp: Initialized DP table
    """
    if not dimensions:
        return default_value
    
    return [initialize_dp_table(dimensions[1:], default_value) for _ in range(dimensions[0])]

def reset_dp_table(dp, default_value=0):
    """
    Reset a DP table to a default value.
    
    Args:
        dp: DP table to reset
        default_value: Value to reset to
    
    Returns:
        dp: Reset DP table
    """
    if not isinstance(dp, list):
        return default_value
    
    for i in range(len(dp)):
        dp[i] = reset_dp_table(dp[i], default_value)
    
    return dp

# ===== Data Structures =====

def get_segment_tree_size(n):
    """
    Calculate the size needed for a segment tree.
    
    Args:
        n: Number of elements
    
    Returns:
        int: Size needed for the segment tree
    """
    return 1 << (n.bit_length() + (0 if n & (n - 1) == 0 else 1))

def create_segment_tree(n):
    """
    Create a segment tree of size n.
    
    Args:
        n: Number of elements
    
    Returns:
        tree: Empty segment tree
    """
    size = get_segment_tree_size(n)
    return [0] * (2 * size)

def update_segment_tree(tree, pos, diff, size):
    """
    Update a segment tree at position pos with difference diff.
    
    Args:
        tree: Segment tree
        pos: Position to update (1-indexed)
        diff: Value to add
        size: Size of the segment tree
    """
    pos += size - 1
    while pos > 0:
        tree[pos] += diff
        pos >>= 1

def query_segment_tree(tree, l, r, size):
    """
    Query a segment tree for the sum between positions l and r (inclusive, 1-indexed).
    
    Args:
        tree: Segment tree
        l: Left bound (1-indexed)
        r: Right bound (1-indexed)
        size: Size of the segment tree
    
    Returns:
        int: Sum of the elements in the range [l, r]
    """
    ans, l, r = 0, l + size - 1, r + size - 1
    
    while l <= r:
        if l & 1:
            ans += tree[l]
            l += 1
        if not r & 1:
            ans += tree[r]
            r -= 1
        l, r = l >> 1, r >> 1
    
    return ans

class MultiColumnSegmentTree:
    """
    Segment tree that maintains multiple columns of values.
    Used for efficiently counting inversions in multiple dimensions.
    """
    def __init__(self, n, columns=2):
        """
        Initialize a segment tree with multiple columns.
        
        Args:
            n: Size of the array
            columns: Number of columns to maintain
        """
        self.n = n
        self.tree = [[0] * columns for _ in range(n << 1)]
    
    def query(self, r, col):
        """
        Query the sum of values in range [n, r) for the given column.
        
        Args:
            r: Right bound (exclusive)
            col: Column index to query
            
        Returns:
            int: Sum of values in the range [n, r) for the specified column
        """
        res = 0
        l = self.n  # Start from the beginning of the array
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
    
    def update(self, idx, val, col):
        """
        Update the value at position idx by adding val for the given column.
        
        Args:
            idx: Position to update
            val: Value to add
            col: Column index to update
        """
        idx += self.n
        
        # Update the leaf node
        self.tree[idx][col] += val
        
        # Update parent nodes
        while idx > 1:
            self.tree[idx >> 1][col] = self.tree[idx][col] + self.tree[idx ^ 1][col]
            idx >>= 1

def build_fenwick_tree(arr):
    """
    Build a Fenwick tree (Binary Indexed Tree) from an array.
    
    Args:
        arr: Input array (0-indexed)
    
    Returns:
        ft: Fenwick tree
    """
    n = len(arr)
    ft = [0] * (n + 1)
    
    for i in range(n):
        update_fenwick_tree(ft, i + 1, arr[i])
    
    return ft

def update_fenwick_tree(ft, idx, val):
    """
    Update a Fenwick tree at position idx by adding val.
    
    Args:
        ft: Fenwick tree
        idx: Position to update (1-indexed)
        val: Value to add
    """
    while idx < len(ft):
        ft[idx] += val
        idx += idx & -idx

def query_fenwick_tree(ft, idx):
    """
    Query a Fenwick tree for the sum of elements from 1 to idx.
    
    Args:
        ft: Fenwick tree
        idx: Right bound (1-indexed)
    
    Returns:
        int: Sum of the elements in the range [1, idx]
    """
    ans = 0
    while idx > 0:
        ans += ft[idx]
        idx -= idx & -idx
    return ans

def query_fenwick_range(ft, l, r):
    """
    Query a Fenwick tree for the sum of elements from l to r.
    
    Args:
        ft: Fenwick tree
        l: Left bound (1-indexed)
        r: Right bound (1-indexed)
    
    Returns:
        int: Sum of the elements in the range [l, r]
    """
    return query_fenwick_tree(ft, r) - query_fenwick_tree(ft, l - 1)

# ===== Mathematical Utilities =====

def mod_add(a, b, mod=MOD):
    """Modular addition"""
    return (a + b) % mod

def mod_sub(a, b, mod=MOD):
    """Modular subtraction"""
    return (a - b) % mod

def mod_mult(a, b, mod=MOD):
    """Modular multiplication"""
    return (a * b) % mod

def mod_pow(base, exp, mod=MOD):
    """Modular exponentiation"""
    result = 1
    base %= mod
    
    while exp > 0:
        if exp & 1:
            result = mod_mult(result, base, mod)
        exp >>= 1
        base = mod_mult(base, base, mod)
    
    return result

def mod_inverse(a, mod=MOD):
    """
    Calculate the modular multiplicative inverse of a number.
    
    Args:
        a: Number to find the inverse of
        mod: Modulus
    
    Returns:
        int: Modular multiplicative inverse of a
    """
    return mod_pow(a, mod - 2, mod) if is_prime(mod) else extended_gcd(a, mod)[0] % mod

def extended_gcd(a, b):
    """
    Extended Euclidean Algorithm to find the Bézout coefficients.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        tuple: (x, y, gcd) where a*x + b*y = gcd(a, b)
    """
    if a == 0:
        return 0, 1, b
    
    x1, y1, gcd = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    
    return x, y, gcd

def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n: Number to check
    
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

def factorial_mod(n, mod=MOD):
    """
    Calculate n! % mod.
    
    Args:
        n: Number to calculate factorial of
        mod: Modulus
    
    Returns:
        int: n! % mod
    """
    result = 1
    for i in range(2, n + 1):
        result = mod_mult(result, i, mod)
    return result

def binomial_coefficient(n, k, mod=MOD):
    """
    Calculate binomial coefficient C(n, k) % mod.
    
    Args:
        n: Upper parameter
        k: Lower parameter
        mod: Modulus
    
    Returns:
        int: C(n, k) % mod
    """
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    
    # Optimize for small values or when k is close to n
    k = min(k, n - k)
    
    numerator = 1
    denominator = 1
    
    for i in range(k):
        numerator = mod_mult(numerator, n - i, mod)
        denominator = mod_mult(denominator, i + 1, mod)
    
    return mod_mult(numerator, mod_inverse(denominator, mod), mod)