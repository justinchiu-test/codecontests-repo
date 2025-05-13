"""
Library file for cluster3.
This contains shared code that can be imported by problems in this cluster.
"""
import sys
sys.setrecursionlimit(10**7)
from types import GeneratorType
data = sys.stdin.read().split()
it = iter(data)
def read_int():
    return int(next(it))
def read_ints(k=None):
    if k is None:
        return [int(x) for x in it]
    return [int(next(it)) for _ in range(k)]
def read_str():
    return next(it)
def read_strs(k):
    return [next(it) for _ in range(k)]

def bootstrap(f):
    """Decorator to support deep recursion via generator trampoline."""
    stack = []
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
def graph(n, edges, directed=False):
    g = [[] for _ in range(n)]
    if directed:
        for u, v in edges:
            g[u].append(v)
    else:
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
    return g
def tree(n, edges, root=0):
    adj = graph(n, edges)
    parent = [-1]*n
    depth = [0]*n
    tin = [0]*n
    tout = [0]*n
    order = []
    t = 0
    def dfs(u, p):
        nonlocal t
        parent[u] = p
        tin[u] = t
        order.append(u)
        t += 1
        for v in adj[u]:
            if v == p: continue
            depth[v] = depth[u] + 1
            dfs(v, u)
        tout[u] = t
    dfs(root, -1)
    return adj, parent, depth, tin, tout, order
class LCA:
    def __init__(self, parent, depth, root=0):
        n = len(parent)
        LOG = (n-1).bit_length() + 1
        up0 = parent.copy()
        up0[root] = root
        up = [up0]
        for j in range(1, LOG):
            prev = up[j-1]
            up.append([prev[prev[v]] for v in range(n)])
        self.up = up
        self.depth = depth
        self.LOG = LOG
    def lca(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        diff = self.depth[u] - self.depth[v]
        for k in range(self.LOG):
            if diff >> k & 1:
                u = self.up[k][u]
        if u == v:
            return u
        for k in range(self.LOG-1, -1, -1):
            if self.up[k][u] != self.up[k][v]:
                u = self.up[k][u]
                v = self.up[k][v]
        return self.up[0][u]
    def dist(self, u, v):
        w = self.lca(u, v)
        return self.depth[u] + self.depth[v] - 2*self.depth[w]
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.f = [0]*(n+1)
    def add(self, i, v):
        i += 1
        while i <= self.n:
            self.f[i] += v
            i += i & -i
    def sum(self, i):
        i += 1
        s = 0
        while i:
            s += self.f[i]
            i -= i & -i
        return s
    def range_sum(self, l, r):
        return self.sum(r) - (self.sum(l-1) if l else 0)
class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0]*n
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x
    def union(self, a, b):
        a = self.find(a); b = self.find(b)
        if a == b: return False
        if self.r[a] < self.r[b]: a, b = b, a
        self.p[b] = a
        if self.r[a] == self.r[b]: self.r[a] += 1
        return True
def pow_mod(x, y, mod):
    return pow(x, y, mod)
def inv_mod(x, mod):
    return pow(x, mod-2, mod)
def nCr(n, r, mod):
    if r < 0 or r > n: return 0
    num = den = 1
    for i in range(r):
        num = num*(n-i) % mod
        den = den*(i+1) % mod
    return num * inv_mod(den, mod) % mod
