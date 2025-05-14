"""
Shared library for common utilities across problem solutions.
Provides input parsing, DSU, graph traversal, and other helpers.
"""
import sys
from collections import deque

sys.setrecursionlimit(10**7)
# Buffer all input tokens for fast parsing
_data = sys.stdin.read().split()
_it = iter(_data)

def readint():
    """Read next token as int."""
    return int(next(_it))

def readints(n=None):
    """Read n tokens as ints (all remaining if n is None)."""
    if n is None:
        return list(map(int, _it))
    return [int(next(_it)) for _ in range(n)]

def readstr():
    """Read next token as str."""
    return next(_it)

def readstrs(n=None):
    """Read n tokens as str (all remaining if n is None)."""
    if n is None:
        return list(_it)
    return [next(_it) for _ in range(n)]

class DSU:
    """Disjoint Set Union (Union-Find) data structure."""
    __slots__ = ('p', 'sz')
    def __init__(self, n):
        self.p = list(range(n))
        self.sz = [1] * n
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x
    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.sz[ra] < self.sz[rb]:
            ra, rb = rb, ra
        self.p[rb] = ra
        self.sz[ra] += self.sz[rb]
        return True
    def size(self, x):
        """Return size of the set containing x."""
        return self.sz[self.find(x)]

def read_graph(n, m, zero_index=True, directed=False):
    """
    Read m edges and build adjacency list of size n.
    zero_index: subtract 1 from nodes if True.
    directed: if False, add edges both ways.
    """
    g = [[] for _ in range(n)]
    for _ in range(m):
        u = readint(); v = readint()
        if zero_index:
            u -= 1; v -= 1
        g[u].append(v)
        if not directed:
            g[v].append(u)
    return g

def read_edges(m, zero_index=True):
    """
    Read m edges as list of (u, v) tuples.
    zero_index: subtract 1 from nodes if True.
    """
    edges = []
    for _ in range(m):
        u = readint(); v = readint()
        if zero_index:
            u -= 1; v -= 1
        edges.append((u, v))
    return edges

def read_weighted_edges(m, zero_index=True):
    """
    Read m weighted edges as list of (u, v, w) tuples.
    zero_index: subtract 1 from nodes if True.
    """
    edges = []
    for _ in range(m):
        u = readint(); v = readint(); w = readint()
        if zero_index:
            u -= 1; v -= 1
        edges.append((u, v, w))
    return edges

def bfs_dist(start, graph):
    """Compute shortest-path distances from start in unweighted graph."""
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

def dfs_iter(start, graph, visited=None):
    """Iterative DFS: return set of visited nodes starting from start."""
    if visited is None:
        visited = set()
    stack = [start]
    while stack:
        u = stack.pop()
        if u in visited:
            continue
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                stack.append(v)
    return visited

def tree_diameter(graph):
    """Return diameter length of a tree using two-phase BFS."""
    d1 = bfs_dist(0, graph)
    u = max(range(len(graph)), key=lambda i: d1[i])
    d2 = bfs_dist(u, graph)
    return max(d2)

def complement_components(n, edges):
    """Compute sizes of connected components in complement graph."""
    g = [set(adj) for adj in edges]
    unused = set(range(n))
    comps = []
    while unused:
        q = deque([unused.pop()])
        cnt = 1
        while q:
            v = q.popleft()
            nxt = [x for x in unused if x not in g[v]]
            for x in nxt:
                q.append(x)
            cnt += len(nxt)
            unused -= set(nxt)
        comps.append(cnt)
    return comps
