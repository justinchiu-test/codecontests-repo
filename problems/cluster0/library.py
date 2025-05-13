"""
Shared library for cluster0 problems.
Provides fast I/O and common graph utilities.
"""
import sys
import builtins

# Override built-in input for fast reading
builtins.input = sys.stdin.readline

def read_int():
    """Read a single integer from input."""
    return int(input())

def read_ints():
    """Read space-separated integers from input and return as list."""
    return list(map(int, input().split()))

def read_edges(m, weighted=False, one_indexed=True):
    """
    Read m edges from input.
    If weighted, each edge has three integers u, v, w.
    Returns list of tuples. Converts to 0-indexed if one_indexed.
    """
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    if one_indexed:
        if weighted:
            edges = [(u - 1, v - 1, w) for u, v, w in edges]
        else:
            edges = [(u - 1, v - 1) for u, v in edges]
    return edges

def adj_list(n, edges, directed=False):
    """
    Build an adjacency list for n nodes from edge list.
    edges: list of (u, v) or (u, v, w).
    If directed is False, adds reverse edges for undirected graph.
    """
    g = [[] for _ in range(n)]
    if not edges:
        return g
    # detect weighted by tuple length
    if len(edges[0]) == 3:
        for u, v, w in edges:
            g[u].append((v, w))
            if not directed:
                g[v].append((u, w))
    else:
        for u, v in edges:
            g[u].append(v)
            if not directed:
                g[v].append(u)
    return g

# Constant for infinity
INF = 10**18

# Deque for BFS/DFS
from collections import deque

def bfs(graph, start=0):
    """
    Breadth-first search on (un)weighted graph.
    Returns list of distances from start to each node (-1 if unreachable).
    """
    n = len(graph)
    dist = [-1] * n
    dq = deque([start])
    dist[start] = 0
    while dq:
        u = dq.popleft()
        for e in graph[u]:
            # handle weighted edges
            v = e[0] if isinstance(e, tuple) else e
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                dq.append(v)
    return dist

def dfs(graph, start=0, visited=None):
    """
    Depth-first search (iterative) on graph.
    Returns list of visited booleans after exploring from start.
    """
    n = len(graph)
    if visited is None:
        visited = [False] * n
    stack = [start]
    while stack:
        u = stack.pop()
        if visited[u]:
            continue
        visited[u] = True
        for e in graph[u]:
            v = e[0] if isinstance(e, tuple) else e
            if not visited[v]:
                stack.append(v)
    return visited
