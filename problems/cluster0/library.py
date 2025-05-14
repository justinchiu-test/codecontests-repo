"""
Library file for cluster0.
This contains shared code that can be imported by problems in this cluster.
"""
import sys
from collections import deque
import heapq

# Input parsing
_data = sys.stdin.read().split()
_it = iter(_data)
def next_str():
    """Read next token as string."""
    return next(_it)

def next_int():
    """Read next token as integer."""
    return int(next(_it))

def next_ints(n):
    """Read next n tokens as integers."""
    return [int(next(_it)) for _ in range(n)]

def read_graph(n, m, directed=False, weighted=False, one_indexed=True):
    """Build adjacency list for graph."""
    g = [[] for _ in range(n)]
    for _ in range(m):
        if weighted:
            u = next_int(); v = next_int(); w = next_int()
        else:
            u = next_int(); v = next_int(); w = None
        if one_indexed:
            u -= 1; v -= 1
        if weighted:
            g[u].append((v, w))
            if not directed:
                g[v].append((u, w))
        else:
            g[u].append(v)
            if not directed:
                g[v].append(u)
    return g

def read_tree(n, weighted=False, one_indexed=True):
    """Build adjacency list for a tree with n nodes (n-1 edges)."""
    return read_graph(n, n-1, directed=False, weighted=weighted, one_indexed=one_indexed)

def dfs(graph, start, visited=None):
    """Iterative DFS, returns visit order."""
    if visited is None:
        visited = set()
    stack = [start]
    order = []
    while stack:
        v = stack.pop()
        if v in visited:
            continue
        visited.add(v)
        order.append(v)
        for u in graph[v]:
            nei = u[0] if isinstance(u, tuple) else u
            if nei not in visited:
                stack.append(nei)
    return order

def bfs(graph, start):
    """Iterative BFS, returns visit order."""
    visited = {start}
    q = deque([start])
    order = [start]
    while q:
        v = q.popleft()
        for u in graph[v]:
            nei = u[0] if isinstance(u, tuple) else u
            if nei not in visited:
                visited.add(nei)
                q.append(nei)
                order.append(nei)
    return order

def dijkstra(graph, source=0):
    """Shortest paths in weighted graph."""
    n = len(graph)
    dist = [float('inf')] * n
    prev = [-1] * n
    dist[source] = 0
    pq = [(0, source)]
    while pq:
        d, v = heapq.heappop(pq)
        if d > dist[v]:
            continue
        for u in graph[v]:
            nei, w = (u if isinstance(u, tuple) else (u, 1))
            nd = d + w
            if nd < dist[nei]:
                dist[nei] = nd
                prev[nei] = v
                heapq.heappush(pq, (nd, nei))
    return dist, prev

class DSU:
    """Disjoint Set Union with path compression and rank."""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True
