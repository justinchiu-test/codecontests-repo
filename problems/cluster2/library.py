"""
Library file for cluster2.
This contains shared code that can be imported by problems in this cluster.
"""
import sys
from collections import deque

def input():
    """Fast input: read a line without trailing newline."""
    return sys.stdin.readline().rstrip("\n")

def readint():
    """Read and return a single integer."""
    return int(input())

def readints():
    """Read a line and return a map of integers."""
    return map(int, input().split())

def readlist():
    """Read a line and return a list of integers."""
    return list(readints())

class DSU:
    """Disjoint Set Union (Union-Find) data structure."""
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0] * n
        self.s = [1] * n
        self.count = n

    def find(self, x):
        """Find with path compression."""
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        """Union by rank; return True if merged."""
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        self.count -= 1
        if self.r[a] < self.r[b]:
            self.p[a] = b
            self.s[b] += self.s[a]
        else:
            self.p[b] = a
            self.s[a] += self.s[b]
            if self.r[a] == self.r[b]:
                self.r[a] += 1
        return True

    def size(self, x):
        """Return size of set containing x."""
        return self.s[self.find(x)]

    def count_sets(self):
        """Return number of disjoint sets."""
        return self.count

def dfs(adj, start, visited=None):
    """Iterative DFS; return or update visited set starting from start."""
    if visited is None:
        visited = set()
    stack = [start]
    while stack:
        u = stack.pop()
        if u not in visited:
            visited.add(u)
            for v in adj[u]:
                if v not in visited:
                    stack.append(v)
    return visited

def bfs(adj, start, visited=None):
    """Iterative BFS; return or update visited set starting from start."""
    if visited is None:
        visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                queue.append(v)
    return visited

def graph(n, edges, directed=False, one_indexed=False):
    """Build adjacency list for n nodes from edge list.
    edges: iterable of (u, v) pairs.
    directed: if False, add both directions.
    one_indexed: if True, assumes u and v in edges are 1-based.
    Returns list of lists adj[0..n-1]."""
    adj = [[] for _ in range(n)]
    for u, v in edges:
        if one_indexed:
            u -= 1; v -= 1
        adj[u].append(v)
        if not directed:
            adj[v].append(u)
    return adj
