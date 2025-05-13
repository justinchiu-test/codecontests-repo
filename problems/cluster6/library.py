"""
Library file for cluster6.
This contains shared code that can be imported by problems in this cluster.
"""
import sys
import math
import heapq
from collections import deque
import bisect

def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def read_str():
    return sys.stdin.readline().strip()

def read_strs():
    return sys.stdin.readline().split()

def read_matrix(n, m, typ=int):
    return [list(map(typ, sys.stdin.readline().split())) for _ in range(n)]

def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return a // gcd(a, b) * b

def frac(a, b):
    g = gcd(a, b)
    return a // g, b // g

def frac_str(a, b):
    num, den = frac(a, b)
    return f"{num}/{den}"

def fact(n):
    return math.factorial(n)

def comb(n, k):
    if hasattr(math, 'comb'):
        return math.comb(n, k)
    return fact(n) // (fact(k) * fact(n - k))

def modinv(a, m):
    return pow(a, m - 2, m)

def bfs(adj, start):
    n = len(adj)
    dist = [-1] * n
    dq = deque([start])
    dist[start] = 0
    while dq:
        u = dq.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                dq.append(v)
    return dist

def dfs(adj, start):
    n = len(adj)
    visited = [False] * n
    order = []
    def _dfs(u):
        visited[u] = True
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                _dfs(v)
    _dfs(start)
    return order

def dijkstra(adj, start):
    n = len(adj)
    dist = [float('inf')] * n
    dist[start] = 0
    hq = [(0, start)]
    while hq:
        d, u = heapq.heappop(hq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(hq, (nd, v))
    return dist

class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.r[a] < self.r[b]:
            a, b = b, a
        self.p[b] = a
        if self.r[a] == self.r[b]:
            self.r[a] += 1
        return True

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.f = [0] * (n + 1)

    def update(self, i, v):
        while i <= self.n:
            self.f[i] += v
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.f[i]
            i -= i & -i
        return s

def prefix_sum(a):
    ps = [0]
    for x in a:
        ps.append(ps[-1] + x)
    return ps

def bisect_left(a, x):
    return bisect.bisect_left(a, x)

def bisect_right(a, x):
    return bisect.bisect_right(a, x)
