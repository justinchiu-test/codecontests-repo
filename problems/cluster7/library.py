"""
Shared library for cluster7 code compression benchmark.
Provides reusable utilities for I/O, math, bitwise ops, data structures, and graph algorithms.
"""
import sys

# Fast I/O
input = sys.stdin.readline
def ri(): return int(input())
def rints(): return list(map(int, input().split()))
def rmap(): return map(int, input().split())
def rs(): return input().strip()

# Math utilities
from math import gcd as _gcd
def gcd(a, b): return _gcd(a, b)
def lcm(a, b): return a // gcd(a, b) * b
def C2(n): return n * (n - 1) // 2
def modpow(a, b, mod): return pow(a, b, mod)
def modinv(a, mod): return pow(a, mod - 2, mod)

# Bitwise utilities
def xor_sum(arr):
    res = 0
    for x in arr:
        res ^= x
    return res
def prefix_xor(arr):
    pre = [0]
    for x in arr:
        pre.append(pre[-1] ^ x)
    return pre

# Data structures
class DSU:
    def __init__(self, n): self.p = list(range(n))
    def find(self, a):
        if self.p[a] != a:
            self.p[a] = self.find(self.p[a])
        return self.p[a]
    def union(self, a, b):
        a = self.find(a); b = self.find(b)
        if a != b: self.p[b] = a

class FenwickTree:
    def __init__(self, n): self.n, self.fw = n, [0] * (n + 1)
    def update(self, i, v):
        while i <= self.n:
            self.fw[i] += v; i += i & -i
    def query(self, i):
        s = 0
        while i > 0:
            s += self.fw[i]; i -= i & -i
        return s
    def range_query(self, l, r): return self.query(r) - self.query(l - 1)

# Graph utilities
def build_adj(n, edges, directed=False):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        if not directed:
            g[v].append(u)
    return g

from collections import deque
def bfs(start, adj):
    n = len(adj)
    dist = [-1] * n
    q = deque([start])
    dist[start] = 0
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] < 0:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist

def dfs_stack(start, adj):
    visited = [False] * len(adj)
    order = []
    stack = [start]
    while stack:
        u = stack.pop()
        if visited[u]: continue
        visited[u] = True
        order.append(u)
        for v in adj[u]:
            if not visited[v]: stack.append(v)
    return order
