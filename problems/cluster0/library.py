"""
Library file for cluster0.
This contains shared code that can be imported by problems in this cluster.
"""
import sys
from collections import deque
import heapq

# Fast IO: read all tokens at once
_data = sys.stdin.buffer.read().split()
_it = iter(_data)

def read_int():
    """Read and return the next token as integer."""
    return int(next(_it))

def read_str():
    """Read and return the next token as string."""
    return next(_it).decode()

def read_list(n):
    """Read and return a list of n integers."""
    return [read_int() for _ in range(n)]

def read_ints():
    """Read remaining tokens as integers (map)."""
    return map(int, _it)

def read_tree(n):
    """Read n-1 edges of an undirected tree; nodes are 1-indexed."""
    adj = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u = read_int(); v = read_int()
        adj[u].append(v)
        adj[v].append(u)
    return adj

def read_graph(n, m, directed=False, weighted=False):
    """Read m edges into adjacency list.
    For unweighted: adj[u] contains neighbors v.
    For weighted: adj[u] contains (v, w).
    Nodes are 1-indexed if u,v in input are 1-indexed."""
    adj = [[] for _ in range(n+1)]
    if weighted:
        for _ in range(m):
            u = read_int(); v = read_int(); w = read_int()
            adj[u].append((v, w))
            if not directed:
                adj[v].append((u, w))
    else:
        for _ in range(m):
            u = read_int(); v = read_int()
            adj[u].append(v)
            if not directed:
                adj[v].append(u)
    return adj

def bfs(adj, start):
    """Return list of distances from start in an unweighted graph (1-indexed)."""
    n = len(adj)
    dist = [-1] * n
    dq = deque([start])
    dist[start] = 0
    while dq:
        u = dq.popleft()
        for v in adj[u]:
            # handle weighted entries
            if isinstance(v, tuple):
                v = v[0]
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                dq.append(v)
    return dist

def dijkstra(adj, start):
    """Return list of min distances from start in a weighted graph."""
    n = len(adj)
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d != dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist

class DSU:
    """Disjoint Set Union (Union-Find) data structure."""
    __slots__ = ('parent', 'rank')

    def __init__(self, n):
        # Initialize n elements (0-indexed or 1-indexed if n = size+1)
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        # Path compression
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        # Union by rank; returns True if merged, False if already same set
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.rank[a] < self.rank[b]:
            a, b = b, a
        self.parent[b] = a
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1
        return True
