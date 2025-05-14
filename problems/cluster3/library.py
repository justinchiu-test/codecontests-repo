"""
Shared utility library for tree and graph problems.
Provides fast IO, graph builders, and common data structures.
"""
import sys

# Fast IO tokenization
sys.setrecursionlimit(10**7)
_data = sys.stdin.buffer.read().split()
_it = iter(_data)

def ni():
    """Read next integer."""
    return int(next(_it))

def ns():
    """Read next token as string."""
    return next(_it).decode()

def read_int():
    """Alias for ni()."""
    return ni()

def read_str():
    """Alias for ns()."""
    return ns()

def read_ints(n):
    """Read n integers as a list."""
    return [ni() for _ in range(n)]

def read_strs(n):
    """Read n tokens as strings."""
    return [ns() for _ in range(n)]

def read_tree(n, directed=False):
    """Read n-1 edges, return adjacency list (1-indexed)."""
    adj = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u = ni(); v = ni()
        adj[u].append(v)
        if not directed:
            adj[v].append(u)
    return adj

def read_weighted_tree(n, directed=False):
    """Read n-1 weighted edges, return adj list of (node, weight)."""
    adj = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u = ni(); v = ni(); w = ni()
        adj[u].append((v, w))
        if not directed:
            adj[v].append((u, w))
    return adj

def read_graph(n, m, directed=False):
    """Read m edges, return adjacency list (1-indexed)."""
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = ni(); v = ni()
        adj[u].append(v)
        if not directed:
            adj[v].append(u)
    return adj

def read_weighted_graph(n, m, directed=False):
    """Read m weighted edges, return adj list of (node, weight)."""
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = ni(); v = ni(); w = ni()
        adj[u].append((v, w))
        if not directed:
            adj[v].append((u, w))
    return adj

# 0-indexed variants for convenience in solutions using 0-based node indices
def read_tree0(n, directed=False):
    """Read n-1 edges (1-based input), return 0-indexed adjacency list of size n."""
    adj = [[] for _ in range(n)]
    for _ in range(n-1):
        u = ni() - 1; v = ni() - 1
        adj[u].append(v)
        if not directed:
            adj[v].append(u)
    return adj

def read_graph0(n, m, directed=False):
    """Read m edges (1-based input), return 0-indexed adjacency list of size n."""
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = ni() - 1; v = ni() - 1
        adj[u].append(v)
        if not directed:
            adj[v].append(u)
    return adj

def read_weighted_tree0(n, directed=False):
    """Read n-1 weighted edges (1-based input), return 0-indexed adjacency list of (node, weight)."""
    adj = [[] for _ in range(n)]
    for _ in range(n-1):
        u = ni() - 1; v = ni() - 1; w = ni()
        adj[u].append((v, w))
        if not directed:
            adj[v].append((u, w))
    return adj

def read_weighted_graph0(n, m, directed=False):
    """Read m weighted edges (1-based input), return 0-indexed adjacency list of (node, weight)."""
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = ni() - 1; v = ni() - 1; w = ni()
        adj[u].append((v, w))
        if not directed:
            adj[v].append((u, w))
    return adj

# Common data structures
from collections import deque, defaultdict, Counter
from types import GeneratorType

def bootstrap(f, stack=[]):
    """Decorator to convert recursive generator-based functions into stack-safe recursion."""
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
