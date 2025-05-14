"""
Shared library for CF cluster6 solutions.
Provides common I/O routines, math utilities, data structures, and graph algorithms.
"""
import sys
import math

# Fast input
input = sys.stdin.readline

# I/O utilities
def ri():
    """Read and return a single integer."""
    return int(input())

def ria():
    """Read a line and return a list of integers."""
    return list(map(int, input().split()))

def rs():
    """Read and return a stripped string."""
    return input().strip()

def rst():
    """Read a line and return a list of tokens (strings)."""
    return input().split()

# Math utilities
from math import gcd, comb, factorial

def lcm(a, b):
    """Return least common multiple of a and b."""
    return a // gcd(a, b) * b

def inv(a, mod):
    """Modular inverse of a under modulo mod."""
    return pow(a, mod - 2, mod)

def nCr(n, k, mod=None):
    """Return binomial coefficient C(n, k), optionally modulo mod."""
    if k < 0 or k > n:
        return 0
    if mod is None:
        return comb(n, k)
    return comb(n, k) % mod

def fact(n, mod=None):
    """Return n! (factorial), optionally modulo mod."""
    if mod is None:
        return factorial(n)
    return factorial(n) % mod

# Data structures
from collections import deque, Counter, defaultdict

class Fenwick:
    """Fenwick Tree (Binary Indexed Tree) for prefix sums."""
    def __init__(self, n):
        self.n = n
        self.f = [0] * (n + 1)

    def add(self, i, v):
        """Add value v at position i (1-indexed)."""
        while i <= self.n:
            self.f[i] += v
            i += i & -i

    def sum(self, i):
        """Return prefix sum up to index i (1-indexed)."""
        s = 0
        while i > 0:
            s += self.f[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        """Return sum in range [l, r] (1-indexed)."""
        return self.sum(r) - self.sum(l - 1)

class DSU:
    """Disjoint Set Union (Union-Find) data structure."""
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        """Find representative of set containing x."""
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        """Merge sets containing a and b."""
        ra = self.find(a)
        rb = self.find(b)
        if ra != rb:
            self.p[ra] = rb

# Graph algorithms
def bfs(start, graph):
    """Breadth-first search from start; returns list of distances."""
    n = len(graph)
    dist = [-1] * n
    dq = deque([start])
    dist[start] = 0
    while dq:
        u = dq.popleft()
        for v in graph[u]:
            if dist[v] < 0:
                dist[v] = dist[u] + 1
                dq.append(v)
    return dist

def apsp(graph):
    """All-pairs shortest paths for small graphs via BFS."""
    return [bfs(i, graph) for i in range(len(graph))]

# Utilities
def prefix_sums(arr):
    """Build and return prefix sums array: [0, a0, a0+a1, ...]."""
    ps = [0]
    for x in arr:
        ps.append(ps[-1] + x)
    return ps

def sliding_window(arr, k):
    """Generate sums of each sliding window of size k over arr."""
    n = len(arr)
    if k > n:
        return
    s = sum(arr[:k])
    yield s
    for i in range(k, n):
        s += arr[i] - arr[i - k]
        yield s
