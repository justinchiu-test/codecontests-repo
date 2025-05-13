"""
Library file for cluster3.
This contains shared code that can be imported by problems in this cluster.
"""
import sys
from collections import deque, defaultdict
from types import GeneratorType

# Fast I/O override
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def read_int():
    """Read a single integer."""
    return int(input())

def read_ints():
    """Read a list of integers."""
    return list(map(int, input().split()))

def read_strs():
    """Read a list of strings."""
    return input().split()

def read_tree(n, base=1, directed=False):
    """
    Read n-1 edges from input and build an adjacency list.
    base=1 for 1-indexed nodes [1..n], base=0 for 0-indexed [0..n-1].
    directed=False for undirected trees.
    """
    if base == 1:
        adj = [[] for _ in range(n+1)]
        for _ in range(n-1):
            u, v = map(int, input().split())
            adj[u].append(v)
            if not directed:
                adj[v].append(u)
    else:
        adj = [[] for _ in range(n)]
        for _ in range(n-1):
            u, v = map(int, input().split())
            u -= 1; v -= 1
            adj[u].append(v)
            if not directed:
                adj[v].append(u)
    return adj

def read_graph(n, m, base=1, directed=False, weighted=False):
    """
    Read m edges from input and build an adjacency list for a graph.
    If weighted is False, each edge line has two ints u v.
    If weighted is True, each edge line has three ints u v w.
    base=1 for 1-indexed nodes, base=0 for 0-indexed.
    directed=False for undirected graphs.
    Returns list of neighbors (or (neighbor, weight) tuples if weighted).
    """
    if base == 1:
        adj = [[] for _ in range(n+1)]
    else:
        adj = [[] for _ in range(n)]
    for _ in range(m):
        data = list(map(int, input().split()))
        if weighted:
            u, v, w = data
        else:
            u, v = data
            w = None
        if base != 1:
            u -= 1; v -= 1
        if weighted:
            adj[u].append((v, w))
            if not directed:
                adj[v].append((u, w))
        else:
            adj[u].append(v)
            if not directed:
                adj[v].append(u)
    return adj

def bfs(adj, src=0):
    """
    Perform BFS from src.
    Return (parent, order, dist) lists.
    parent[src] == src, dist[src] == 0.
    """
    n = len(adj)
    parent = [-1] * n
    dist = [-1] * n
    order = []
    dq = deque([src])
    parent[src] = src
    dist[src] = 0
    while dq:
        v = dq.popleft()
        order.append(v)
        for to in adj[v]:
            if dist[to] == -1:
                dist[to] = dist[v] + 1
                parent[to] = v
                dq.append(to)
    return parent, order, dist

def par_order(adj, root=0):
    """
    Simple DFS order builder.
    Return (parent, dfs_order) starting from root.
    parent[root] is -1.
    """
    n = len(adj)
    parent = [-1] * n
    order = []
    stack = [root]
    parent[root] = -1
    while stack:
        v = stack.pop()
        order.append(v)
        for to in adj[v]:
            if to != parent[v]:
                parent[to] = v
                stack.append(to)
    return parent, order

def get_children(parent):
    """
    Build a children list from parent list.
    """
    n = len(parent)
    children = [[] for _ in range(n)]
    for i, p in enumerate(parent):
        if p >= 0 and i != p:
            children[p].append(i)
    return children

def bootstrap(f, stack=[]):
    """
    Decorator to convert recursive generators into iterative calls.
    Allows deep recursion without increasing Python call stack.
    """
    def wrapped(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if isinstance(to, GeneratorType):
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack:
                    break
                to = stack[-1].send(to)
        return to
    return wrapped

def lca_init(adj, root=0):
    """
    Prepare LCA binary lifting tables.
    Return (lca, dist, depth, parent0), where:
      - lca(u,v) gives lowest common ancestor
      - dist(u,v) gives distance between nodes
      - depth[i] is depth of node i
      - parent0[i] is immediate parent of i (parent0[root] == root)
    Nodes indexed 0..n-1 or 1..n depending on adj length.
    """
    n = len(adj)
    LOG = max(1, (n-1).bit_length())
    parent0 = [-1] * n
    depth = [0] * n
    dq = deque([root])
    parent0[root] = root
    while dq:
        v = dq.popleft()
        for to in adj[v]:
            if parent0[to] == -1:
                parent0[to] = v
                depth[to] = depth[v] + 1
                dq.append(to)
    up = [parent0]
    for k in range(1, LOG):
        prev = up[k-1]
        curr = [prev[prev[i]] for i in range(n)]
        up.append(curr)
    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        diff = depth[u] - depth[v]
        for k in range(LOG):
            if diff >> k & 1:
                u = up[k][u]
        if u == v:
            return u
        for k in range(LOG-1, -1, -1):
            if up[k][u] != up[k][v]:
                u = up[k][u]
                v = up[k][v]
        return up[0][u]
    def dist(u, v):
        w = lca(u, v)
        return depth[u] + depth[v] - 2 * depth[w]
    return lca, dist, depth, parent0
