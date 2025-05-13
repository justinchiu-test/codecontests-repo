"""
Library file for cluster7.
This contains shared code that can be imported by problems in this cluster.
"""

import sys
from typing import List, Tuple, Set, Dict, Optional, Any, Union, Iterator, Callable
import math
import random
from collections import defaultdict, Counter, deque

# =============== I/O Utilities ===============

def read_int() -> int:
    """Read a single integer from stdin."""
    return int(input())

def read_ints() -> List[int]:
    """Read multiple integers from a single line."""
    return list(map(int, input().split()))

def read_array() -> List[int]:
    """Read an array of integers (alias for read_ints)."""
    return read_ints()

def read_matrix(rows: int) -> List[List[int]]:
    """Read a matrix of integers with the specified number of rows."""
    return [read_ints() for _ in range(rows)]

def read_test_cases(reader_func=None):
    """Process multiple test cases.
    
    Args:
        reader_func: Function to read each test case. If None, returns the test case count.
    
    Returns:
        If reader_func is provided, yields the result of reader_func for each test case.
        Otherwise, returns the number of test cases.
    """
    t = read_int()
    if reader_func is None:
        return t
    
    for _ in range(t):
        yield reader_func()

def setup_fast_io():
    """Set up faster I/O handling for competitive programming."""
    import os
    import sys
    from io import BytesIO, IOBase

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

    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    return lambda: sys.stdin.readline().rstrip("\r\n")

# =============== Bit Operations ===============

def xor_range(n: int) -> int:
    """Calculate XOR of all numbers from 0 to n inclusive.
    
    This uses the pattern that XOR of ranges [0, n] follows:
    n, 1, n+1, 0 for n % 4 = 0, 1, 2, 3 respectively.
    """
    return [n, 1, n+1, 0][n % 4]

def xor_prefix_array(arr: List[int]) -> List[int]:
    """Calculate prefix XOR array."""
    prefix = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix[i+1] = prefix[i] ^ arr[i]
    return prefix

def xor_sum(arr: List[int]) -> int:
    """XOR sum of all elements in array."""
    result = 0
    for x in arr:
        result ^= x
    return result

def find_xor_pairs(arr: List[int], target_xor: int) -> List[Tuple[int, int]]:
    """Find all pairs in array with XOR equal to target_xor."""
    seen = set()
    pairs = []
    
    for num in arr:
        if num ^ target_xor in seen:
            pairs.append((num, num ^ target_xor))
        seen.add(num)
    
    return pairs

def find_nonzero_xor_combination(matrix: List[List[int]]) -> Optional[List[int]]:
    """Find combination of elements (one from each row) with non-zero XOR."""
    n = len(matrix)
    
    # Check if taking first element from each row gives non-zero XOR
    xor_val = 0
    for i in range(n):
        xor_val ^= matrix[i][0]
    
    if xor_val != 0:
        return [1] * n  # All first elements (1-indexed)
    
    # Look for a row where some element differs from the first element
    for i in range(n):
        for j in range(1, len(matrix[i])):
            if matrix[i][j] != matrix[i][0]:
                # Found a different element, construct the solution
                result = [1] * n  # Start with all first elements
                result[i] = j + 1  # Use the different element (1-indexed)
                return result
    
    return None  # No solution found

def count_bits(n: int) -> int:
    """Count the number of set bits in an integer."""
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def get_bit(n: int, i: int) -> int:
    """Get the ith bit of n (0-indexed)."""
    return (n >> i) & 1

def set_bit(n: int, i: int) -> int:
    """Set the ith bit of n (0-indexed)."""
    return n | (1 << i)

def clear_bit(n: int, i: int) -> int:
    """Clear the ith bit of n (0-indexed)."""
    return n & ~(1 << i)

def toggle_bit(n: int, i: int) -> int:
    """Toggle the ith bit of n (0-indexed)."""
    return n ^ (1 << i)

def min_cogrowing_sequence(arr: List[int]) -> List[int]:
    """
    Find minimum values to make a co-growing sequence with given array.
    
    A co-growing sequence satisfies: (x₁⊕y₁, x₂⊕y₂, ..., xₙ⊕yₙ) is a strictly increasing sequence,
    where y values are computed to satisfy this property.
    """
    sequence = []
    prev_value = 0
    
    for value in arr:
        new_value = prev_value & (prev_value ^ value)
        prev_value = value ^ new_value
        sequence.append(new_value)
    
    return sequence

def xor_of_sequence(start: int, length: int) -> int:
    """Calculate XOR of sequence [start, start+1, ..., start+length-1]."""
    # Calculate XOR of [0, start-1] and XOR of [0, start+length-1]
    # Then XOR them to get the range
    if start == 0:
        return xor_range(start + length - 1)
    return xor_range(start - 1) ^ xor_range(start + length - 1)

def xor_parity(arr: List[int]) -> int:
    """Check if the XOR of all elements in the array is 0 (even parity) or 1 (odd parity)."""
    return 1 if xor_sum(arr) > 0 else 0

def binary_to_int(binary_list: List[int]) -> int:
    """Convert a list of binary digits to integer."""
    result = 0
    for bit in binary_list:
        result = (result << 1) | bit
    return result

def int_to_binary(n: int, bits: int = None) -> List[int]:
    """Convert an integer to a list of binary digits.
    
    Args:
        n: The integer to convert
        bits: The number of bits to include (default: minimum required)
    
    Returns:
        A list of 0s and 1s representing the binary digits of n
    """
    if n == 0:
        return [0] if bits is None else [0] * bits
    
    binary = []
    while n > 0:
        binary.append(n & 1)
        n >>= 1
    
    binary.reverse()
    
    if bits is not None:
        if len(binary) < bits:
            binary = [0] * (bits - len(binary)) + binary
        elif len(binary) > bits:
            binary = binary[-bits:]
    
    return binary

def bit_count_array(arr: List[int]) -> List[int]:
    """Count the number of set bits at each position across all numbers in the array."""
    max_bits = max(arr).bit_length() if arr else 0
    counts = [0] * max_bits
    
    for num in arr:
        for i in range(max_bits):
            if (num >> i) & 1:
                counts[i] += 1
    
    return counts

def xor_pairs_count(arr: List[int], target_xor: int) -> int:
    """Count pairs in array with XOR equal to target_xor."""
    count = 0
    seen = defaultdict(int)
    
    for num in arr:
        count += seen[num ^ target_xor]
        seen[num] += 1
    
    return count

def xor_subsequence_count(arr: List[int], target_xor: int, mod: int = None) -> int:
    """Count subsequences with XOR equal to target_xor."""
    count = {0: 1}  # XOR of empty subsequence is 0
    current_xor = 0
    total = 0
    
    for num in arr:
        current_xor ^= num
        if current_xor ^ target_xor in count:
            total += count[current_xor ^ target_xor]
        
        if current_xor in count:
            count[current_xor] += 1
        else:
            count[current_xor] = 1
            
        if mod:
            total %= mod
    
    return total

def is_triple_flippable(arr: List[int]) -> List[List[int]]:
    """Check if an array can be transformed to all zeros using triple flips and returns the flips."""
    n = len(arr)
    operations = []
    
    # Create a copy so we don't modify the original
    a = arr.copy()
    
    # Try to reduce the array to all zeros using triple flips
    for i in range(n - 2):
        if a[i] == 1:
            # Flip the current position and the next two
            a[i] ^= 1
            a[i+1] ^= 1
            a[i+2] ^= 1
            operations.append([i+1, i+2, i+3])  # 1-indexed positions
    
    # Check if the last two elements are zeros
    if a[-2:] == [0, 0]:
        return operations
    
    return None  # Not possible

def bit_mask_possibilities(arr: List[int], target_xor: int = None) -> List[int]:
    """Generate all valid bitmasks for an array, optionally with a target XOR."""
    n = len(arr)
    valid_masks = []
    
    for mask in range(1 << n):
        xor_val = 0
        for i in range(n):
            if (mask >> i) & 1:
                xor_val ^= arr[i]
                
        if target_xor is None or xor_val == target_xor:
            valid_masks.append(mask)
    
    return valid_masks

def xor_basis(arr: List[int], bits: int = 30) -> List[int]:
    """Compute a basis for the vector space spanned by the array under XOR."""
    basis = []
    for num in arr:
        for basis_vector in basis:
            num = min(num, num ^ basis_vector)
        
        if num > 0:
            # Ensure this basis vector has the highest bit set
            for i in range(len(basis)):
                if (basis[i] ^ num) < basis[i]:
                    basis[i] ^= num
            basis.append(num)
            basis.sort(reverse=True)
    
    return basis

# =============== Data Structures for XOR Operations ===============

class XORTrie:
    """Trie data structure optimized for XOR operations."""
    
    def __init__(self):
        """Initialize an empty XOR trie."""
        # Each node is [left_child, right_child, count]
        self.tree = [[0, 0, 0]]
    
    def add(self, x: int, bits: int = 30) -> None:
        """Add a number to the trie."""
        now = 0
        self.tree[now][2] += 1  # Increment count at root
        
        for i in range(bits-1, -1, -1):
            bit = (x >> i) & 1
            if self.tree[now][bit] == 0:
                self.tree[now][bit] = len(self.tree)
                self.tree.append([0, 0, 0])
            now = self.tree[now][bit]
            self.tree[now][2] += 1
    
    def find_max_xor(self, x: int, bits: int = 30) -> int:
        """Find the number in the trie that gives maximum XOR with x."""
        if not self.tree[0][2]:  # Empty trie
            return 0
        
        now = 0
        result = 0
        
        for i in range(bits-1, -1, -1):
            bit = (x >> i) & 1
            # Try to go opposite way to maximize XOR
            if self.tree[now][bit ^ 1] and self.tree[self.tree[now][bit ^ 1]][2]:
                now = self.tree[now][bit ^ 1]
                result |= (1 << i)
            else:
                now = self.tree[now][bit]
        
        return result
    
    def find_min_xor(self, x: int, bits: int = 30) -> int:
        """Find the number in the trie that gives minimum XOR with x."""
        if not self.tree[0][2]:  # Empty trie
            return 0
        
        now = 0
        result = 0
        
        for i in range(bits-1, -1, -1):
            bit = (x >> i) & 1
            # Try to go same way to minimize XOR
            if self.tree[now][bit] and self.tree[self.tree[now][bit]][2]:
                now = self.tree[now][bit]
            else:
                now = self.tree[now][bit ^ 1]
                result |= (1 << i)
        
        return result
    
    def remove(self, x: int, bits: int = 30) -> None:
        """Remove one occurrence of x from the trie."""
        # If trie is empty or x doesn't exist, do nothing
        if not self.tree[0][2]:
            return
        
        now = 0
        nodes = [now]
        
        # Check if x exists in the trie
        for i in range(bits-1, -1, -1):
            bit = (x >> i) & 1
            if not self.tree[now][bit] or not self.tree[self.tree[now][bit]][2]:
                return  # x doesn't exist in the trie
            now = self.tree[now][bit]
            nodes.append(now)
        
        # Decrement counts along the path
        for node in nodes:
            self.tree[node][2] -= 1

class BinaryIndexedTree:
    """Binary Indexed Tree (Fenwick Tree) for range queries and point updates."""
    
    def __init__(self, size: int):
        """Initialize a BIT with given size."""
        self.size = size + 1  # 1-indexed
        self.tree = [0] * self.size
    
    def update(self, i: int, val: int) -> None:
        """Add val to the element at index i."""
        i += 1  # Convert to 1-indexed
        while i < self.size:
            self.tree[i] += val
            i += i & -i  # Move to the next node in the tree
    
    def query(self, i: int) -> int:
        """Get the sum of elements from 0 to i (inclusive)."""
        i += 1  # Convert to 1-indexed
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & -i  # Move to the parent node
        return total
    
    def range_query(self, left: int, right: int) -> int:
        """Get the sum of elements from left to right (inclusive)."""
        return self.query(right) - self.query(left - 1)

# =============== Number Theory Utilities ===============

def gcd(a: int, b: int) -> int:
    """Calculate the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    """Calculate the least common multiple of a and b."""
    return a * b // gcd(a, b)

def mod_inverse(a: int, m: int) -> int:
    """Calculate the modular multiplicative inverse of a modulo m."""
    g = gcd(a, m)
    if g != 1:
        raise ValueError("Modular inverse does not exist")
    return pow(a, m - 2, m)

def prime_factors(n: int) -> Set[int]:
    """Find all prime factors of n."""
    factors = set()
    factors.add(n)
    
    # Check for divisibility by 2
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    
    # Check for divisibility by odd numbers
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.add(i)
            n //= i
    
    # If n > 1, it's a prime factor
    if n > 1:
        factors.add(n)
    
    return factors

def sieve_of_eratosthenes(n: int) -> List[bool]:
    """Generate a sieve of Eratosthenes up to n."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    
    p = 2
    while p * p <= n:
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
        p += 1
    
    return sieve

# =============== Graph Operations ===============

def create_graph(edges: List[Tuple[int, int]], n: int, directed: bool = False) -> List[List[int]]:
    """Create an adjacency list from a list of edges."""
    graph = [[] for _ in range(n)]
    
    for u, v in edges:
        graph[u].append(v)
        if not directed:
            graph[v].append(u)
    
    return graph

def topological_sort(graph: List[List[int]]) -> List[int]:
    """Perform a topological sort on a directed acyclic graph."""
    n = len(graph)
    visited = [False] * n
    result = []
    
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        result.append(node)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
    
    result.reverse()
    return result

def get_connected_components(graph: List[List[int]]) -> List[List[int]]:
    """Find all connected components in an undirected graph."""
    n = len(graph)
    visited = [False] * n
    components = []
    
    def dfs(node, component):
        visited[node] = True
        component.append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, component)
    
    for i in range(n):
        if not visited[i]:
            component = []
            dfs(i, component)
            components.append(component)
    
    return components

# =============== Random Utilities ===============

def zobrist_hash(n: int, limit: int = (1 << 31) - 1) -> List[int]:
    """Generate n random Zobrist hash values."""
    return [random.randint(0, limit) for _ in range(n)]