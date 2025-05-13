"""
Shared utility library for problem solutions.
Provides common I/O functions, DSU, and graph connectivity helpers.
"""
import sys
from collections import deque

# Fast input
input = sys.stdin.readline

def ii():
    """Read and return a single integer."""
    return int(input())

def li():
    """Read a line of space-separated integers and return as a list."""
    return list(map(int, input().split()))

def mi():
    """Read a line of space-separated integers and return as a map iterator."""
    return map(int, input().split())

class DSU:
    """Disjoint Set Union (Union-Find) with path compression and union by size."""
    __slots__ = ('parent', 'size')

    def __init__(self, n):
        # initialize n elements 0..n-1
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        # find representative with path compression
        p = self.parent
        while x != p[x]:
            p[x] = p[p[x]]
            x = p[x]
        return x

    def union(self, a, b):
        """Union sets containing a and b."""
        p = self.parent
        sz = self.size
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return ra
        # attach smaller tree to larger
        if sz[ra] < sz[rb]:
            ra, rb = rb, ra
        p[rb] = ra
        sz[ra] += sz[rb]
        return ra

    def get_size(self, x):
        """Return size of set containing x."""
        return self.size[self.find(x)]

def connected_components(adj):
    """
    Given an undirected graph as adjacency list, return list of sizes of its connected components.
    Example:
        adj = [[1], [0,2], [1], []]  # graph with 2 components
        connected_components(adj) -> [3,1]
    """
    n = len(adj)
    vis = [False] * n
    comps = []
    for i in range(n):
        if not vis[i]:
            cnt = 0
            dq = deque([i])
            vis[i] = True
            while dq:
                u = dq.popleft()
                cnt += 1
                for v in adj[u]:
                    if not vis[v]:
                        vis[v] = True
                        dq.append(v)
            comps.append(cnt)
    return comps

def bfs(adj, start):
    """
    Breadth-first search on unweighted graph.
    Returns list of distances from start to each node (or -1 if unreachable).
    """
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

def diameter(adj):
    """
    Compute the diameter (longest shortest path) of a tree or connected graph.
    Returns the maximum distance between any two nodes.
    """
    if not adj:
        return 0
    # first BFS to find furthest from 0
    dist0 = bfs(adj, 0)
    # pick a valid start (in case node 0 is isolated)
    try:
        u = max((i for i, d in enumerate(dist0) if d >= 0), key=lambda i: dist0[i])
    except ValueError:
        return 0
    # BFS from u to find diameter
    dist_u = bfs(adj, u)
    return max(dist_u) if dist_u else 0

def complement_cc_count(nodes, neighbors):
    """
    Count connected components in the complement of a graph.
    'nodes' is an iterable of node identifiers; 'neighbors' maps each node to a set of adjacent nodes.
    Returns the number of connected components in the graph where edges exist between non-adjacent nodes.
    """
    unused = set(nodes)
    comps = 0
    while unused:
        comps += 1
        seed = unused.pop()
        stack = [seed]
        # explore component in complement graph
        while stack:
            u = stack.pop()
            # find nodes not adjacent to u
            to_visit = [v for v in list(unused) if v not in neighbors[u]]
            for v in to_visit:
                unused.remove(v)
            stack.extend(to_visit)
    return comps
