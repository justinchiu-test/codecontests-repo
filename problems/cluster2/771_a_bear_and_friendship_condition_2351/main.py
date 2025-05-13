#!/usr/bin/env python3

from library import mi, DSU
from collections import Counter

# Read number of vertices and edges
n, m = mi()
# Initialize DSU for vertices labeled 1..n
dsu = DSU(n+1)
edges = []
for _ in range(m):
    u, v = mi()
    edges.append((u, v))
    dsu.union(u, v)

# Count edges per connected component
edge_count = Counter()
for u, v in edges:
    root = dsu.find(u)
    edge_count[root] += 1

# Verify each component is a clique: edges = size*(size-1)/2
ok = True
for root, en in edge_count.items():
    sz = dsu.get_size(root)
    if en != sz*(sz-1)//2:
        ok = False
        break
print("YES" if ok else "NO")
