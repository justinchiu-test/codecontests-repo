"""
Shared library for tree-based problems (cluster3).
Provides common utilities for input parsing, tree construction, and traversal.
"""
import sys
from collections import deque

# Increase recursion limit for deep trees
sys.setrecursionlimit(10**7)
from types import GeneratorType
import os

def read_int():
    """Read a single integer from stdin."""
    return int(sys.stdin.readline())

def read_ints():
    """Read a list of integers from stdin."""
    return list(map(int, sys.stdin.readline().split()))

def read_int_pair():
    """Read two integers from stdin and return as a tuple."""
    return map(int, sys.stdin.readline().split())

def build_adj(n, edges, directed=False):
    """
    Build an adjacency list for n nodes (0-indexed) from an iterable of edges.
    If directed is False, edges are bidirectional.
    """
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        if not directed:
            g[v].append(u)
    return g

def build_weighted_adj(n, edges, directed=False):
    """
    Build an adjacency list for n nodes (0-indexed) with weighted edges.
    edges is an iterable of (u, v, w).
    """
    g = [[] for _ in range(n)]
    for u, v, w in edges:
        g[u].append((v, w))
        if not directed:
            g[v].append((u, w))
    return g

def read_tree(n):
    """
    Read a rooted tree of n nodes given parents for nodes 2..n (1-indexed input).
    Returns undirected adjacency list (0-indexed nodes).
    """
    data = read_ints()
    # data[i-2] is parent of node i (1-indexed)
    g = [[] for _ in range(n)]
    for i, p in enumerate(data, start=2):
        u = p - 1
        v = i - 1
        g[u].append(v)
        g[v].append(u)
    return g

def read_edges(n):
    """
    Read n-1 undirected edges (1-indexed) and build adjacency list (0-indexed).
    """
    g = [[] for _ in range(n)]
    for _ in range(n-1):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1; v -= 1
        g[u].append(v)
        g[v].append(u)
    return g

def read_weighted_edges(n, m=None, directed=False):
    """
    Read m weighted edges (u, v, w) from stdin (1-indexed) and build a weighted adj list.
    If m is None, read n-1 edges.
    """
    total = m if m is not None else n-1
    edges = []
    for _ in range(total):
        u, v, w = map(int, sys.stdin.readline().split())
        u -= 1; v -= 1
        edges.append((u, v, w))
    return build_weighted_adj(n, edges, directed)

def dfs_info(adj, root=0):
    """
    Perform a DFS from root on undirected tree represented by adj.
    Returns (parent, depth, subtree_size, order), where
      parent[i] is parent of node i (root has parent -1),
      depth[i] is depth from root,
      subtree_size[i] is size of subtree rooted at i,
      order is list of nodes in visitation order (pre-order).
    """
    n = len(adj)
    parent = [-1] * n
    depth = [0] * n
    size = [1] * n
    order = [root]
    # build parent and depth via stack-like BFS over list
    for u in order:
        for v in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            depth[v] = depth[u] + 1
            order.append(v)
    # accumulate subtree sizes in reverse order
    for u in reversed(order):
        for v in adj[u]:
            if v == parent[u]:
                continue
            size[u] += size[v]
    return parent, depth, size, order

def dfs(adj, root=0):
    """Simple iterative DFS that returns visit order of nodes starting from root."""
    n = len(adj)
    visited = [False] * n
    order = []
    stack = [root]
    visited[root] = True
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            # handle weighted adj entries
            w = None
            if isinstance(v, tuple):
                v, w = v
            if not visited[v]:
                visited[v] = True
                stack.append(v)
    return order

def bfs_info(adj, root=0):
    """
    Perform a BFS from root on undirected graph adj.
    Returns (parent, distance, order), where
      parent[i] is parent of node i (root has parent -1),
      distance[i] is distance from root,
      order is list of nodes in BFS visitation order.
    """
    n = len(adj)
    parent = [-1] * n
    dist = [-1] * n
    dist[root] = 0
    order = []
    dq = deque([root])
    while dq:
        u = dq.popleft()
        order.append(u)
        for v in adj[u]:
            if dist[v] != -1:
                continue
            parent[v] = u
            dist[v] = dist[u] + 1
            dq.append(v)
    return parent, dist, order

def bfs(adj, root=0):
    """Simple BFS that returns visit order of nodes starting from root."""
    n = len(adj)
    visited = [False] * n
    order = []
    dq = deque([root])
    visited[root] = True
    while dq:
        u = dq.popleft()
        order.append(u)
        for v in adj[u]:
            # handle weighted adj entries
            if isinstance(v, tuple):
                v, _ = v
            if not visited[v]:
                visited[v] = True
                dq.append(v)
    return order

def count_leaves(adj, root=0):
    """
    Count number of leaf nodes in each subtree of a tree.
    Returns list leaf_count where leaf_count[i] is the count of leaves in subtree rooted at i.
    """
    parent, _, _, order = dfs_info(adj, root)
    n = len(adj)
    leaf_count = [0] * n
    # process nodes bottom-up
    for u in reversed(order):
        # if no children besides parent, it's a leaf
        cnt = 0
        has_child = False
        for v in adj[u]:
            if v == parent[u]:
                continue
            has_child = True
            cnt += leaf_count[v]
        leaf_count[u] = 1 if not has_child else cnt
    return leaf_count

def euler_tour(adj, root=0):
    """Perform Euler tour to compute entry/exit times and tour list."""
    n = len(adj)
    tin = [0] * n
    tout = [0] * n
    tour = []
    t = 0
    def _dfs(u, p=-1):
        nonlocal t
        tin[u] = t; tour.append(u); t += 1
        for v in adj[u]:
            # skip parent and handle weighted edges
            vv = v[0] if isinstance(v, tuple) else v
            if vv == p: continue
            _dfs(vv, u)
        tout[u] = t-1
    _dfs(root)
    return tin, tout, tour

class BIT:
    """Fenwick Tree for range sum queries and point updates."""
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)
    def update(self, i, v):
        i += 1
        while i <= self.n:
            self.bit[i] += v
            i += i & -i
    def query(self, i):
        s = 0
        i += 1
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s
    def range_query(self, l, r):
        return self.query(r) - (self.query(l-1) if l > 0 else 0)
