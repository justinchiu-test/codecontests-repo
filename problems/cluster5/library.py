"""
Library file for cluster5.
This contains shared code that can be imported by problems in this cluster.
"""

from typing import List, Tuple, Any, Dict, Set, Optional
import math
from collections import defaultdict, Counter, deque

# ------------------ Input/Output Utilities ------------------

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

# ------------------ Math Utilities ------------------

def mod_add(a: int, b: int, mod: int) -> int:
    """
    Add two numbers under modulo.
    
    Args:
        a: First number
        b: Second number
        mod: Modulo value
        
    Returns:
        (a + b) % mod
    """
    return (a + b) % mod

def mod_sub(a: int, b: int, mod: int) -> int:
    """
    Subtract b from a under modulo, ensuring positive result.
    
    Args:
        a: First number
        b: Second number
        mod: Modulo value
        
    Returns:
        (a - b) % mod, ensuring result is positive
    """
    return ((a - b) % mod + mod) % mod

def mod_mul(a: int, b: int, mod: int) -> int:
    """
    Multiply two numbers under modulo.
    
    Args:
        a: First number
        b: Second number
        mod: Modulo value
        
    Returns:
        (a * b) % mod
    """
    return (a * b) % mod

def mod_pow(base: int, exp: int, mod: int) -> int:
    """
    Calculate (base ^ exp) % mod efficiently.
    
    Args:
        base: Base number
        exp: Exponent
        mod: Modulo value
        
    Returns:
        (base ^ exp) % mod
    """
    if mod == 1:
        return 0
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

# Common modulos used in competitive programming
MOD_10_9_PLUS_7 = 10**9 + 7
MOD_998_244_353 = 998_244_353

# ------------------ String Algorithms ------------------

def z_function(s: List[Any]) -> List[int]:
    """
    Z-function algorithm for lists.
    For each position i, calculate z[i] = the length of the longest sublist
    starting from position i that is also a prefix of the list.
    
    Time complexity: O(n)
    Space complexity: O(n)
    
    Args:
        s: The input list (can be a string or list of any elements)
        
    Returns:
        A list z where z[i] is the length of the longest common
        prefix between s and the suffix of s starting at i.
    """
    n = len(s)
    z = [0] * n
    if n == 0:
        return z
    z[0] = n
    
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    
    return z

def calc_prefix(s: str) -> List[int]:
    """
    Calculate the prefix function (KMP algorithm).
    For each position i, calculate longest proper prefix of s[0...i]
    that is also a suffix of s[0...i].
    
    Time complexity: O(n)
    Space complexity: O(n)
    
    Args:
        s: The input string
        
    Returns:
        A list p where p[i] is the length of the longest proper prefix of s[0...i]
        that is also a suffix of s[0...i].
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

# String hashing functions
class StringHash:
    """
    String hashing utility for efficient string comparison and substring checking.
    Uses polynomial rolling hash with two different bases and moduli for
    reduced collision probability.
    """
    def __init__(self, s: str, base1=31, mod1=10**9+7, base2=37, mod2=10**9+9):
        """
        Initialize the hash object with the given string.
        
        Args:
            s: The input string
            base1: First base for polynomial hashing (default: 31)
            mod1: First modulus for polynomial hashing (default: 10^9+7)
            base2: Second base for polynomial hashing (default: 37)
            mod2: Second modulus for polynomial hashing (default: 10^9+9)
        """
        self.s = s
        self.n = len(s)
        self.base1, self.mod1 = base1, mod1
        self.base2, self.mod2 = base2, mod2
        
        # Precompute powers
        self.pow1 = [1] * (self.n + 1)
        self.pow2 = [1] * (self.n + 1)
        for i in range(1, self.n + 1):
            self.pow1[i] = (self.pow1[i-1] * base1) % mod1
            self.pow2[i] = (self.pow2[i-1] * base2) % mod2
        
        # Precompute hashes
        self.h1 = [0] * (self.n + 1)
        self.h2 = [0] * (self.n + 1)
        for i in range(self.n):
            self.h1[i+1] = (self.h1[i] * base1 + ord(s[i])) % mod1
            self.h2[i+1] = (self.h2[i] * base2 + ord(s[i])) % mod2
    
    def get_hash(self, l: int, r: int) -> Tuple[int, int]:
        """
        Get hash for substring s[l:r] (0-indexed, inclusive l, exclusive r).
        
        Args:
            l: Start index (inclusive)
            r: End index (exclusive)
            
        Returns:
            Tuple of two hash values
        """
        hash1 = (self.h1[r] - self.h1[l] * self.pow1[r-l]) % self.mod1
        hash2 = (self.h2[r] - self.h2[l] * self.pow2[r-l]) % self.mod2
        return (hash1, hash2)

    def equals(self, l1: int, r1: int, l2: int, r2: int) -> bool:
        """
        Check if substring s[l1:r1] equals substring s[l2:r2].
        
        Args:
            l1, r1: First substring range
            l2, r2: Second substring range
            
        Returns:
            True if substrings are equal, False otherwise
        """
        if r1 - l1 != r2 - l2:
            return False
        return self.get_hash(l1, r1) == self.get_hash(l2, r2)

# ------------------ Dynamic Programming Utilities ------------------

def create_dp_table(rows: int, cols: int, default_value: Any = 0) -> List[List[Any]]:
    """
    Create a 2D dynamic programming table.
    
    Args:
        rows: Number of rows
        cols: Number of columns
        default_value: Initial value for all cells
        
    Returns:
        A 2D list initialized with the default value
    """
    return [[default_value for _ in range(cols)] for _ in range(rows)]

def create_dp_table_3d(dim1: int, dim2: int, dim3: int, default_value: Any = 0) -> List[List[List[Any]]]:
    """
    Create a 3D dynamic programming table.
    
    Args:
        dim1: First dimension size
        dim2: Second dimension size
        dim3: Third dimension size
        default_value: Initial value for all cells
        
    Returns:
        A 3D list initialized with the default value
    """
    return [[[default_value for _ in range(dim3)] for _ in range(dim2)] for _ in range(dim1)]

def create_bool_table(rows: int, cols: int) -> List[List[bool]]:
    """
    Create a 2D boolean table initialized to False.
    
    Args:
        rows: Number of rows
        cols: Number of columns
        
    Returns:
        A 2D list of booleans initialized to False
    """
    return [[False for _ in range(cols)] for _ in range(rows)]

def create_array(size: int, default_value: Any = 0) -> List[Any]:
    """
    Create a 1D array with given size and default value.
    
    Args:
        size: Size of the array
        default_value: Initial value for all elements
        
    Returns:
        A list initialized with the default value
    """
    return [default_value for _ in range(size)]

# ------------------ Data Structures ------------------

def update(tree: List[int], pos: int, diff: int, si: int):
    """Update a value in a segment tree."""
    pos += si - 1
    while pos:
        tree[pos] += diff
        pos >>= 1

def query(tree: List[int], l: int, r: int, si: int) -> int:
    """Query a segment tree for a sum in range [l, r]."""
    ans, l, r = 0, l + si - 1, r + si - 1
    while l < r:
        if l & 1:
            ans += tree[l]
            l += 1
        if not r & 1:
            ans += tree[r]
            r -= 1
        l, r = l >> 1, r >> 1
    return ans + (0 if l != r else tree[l])