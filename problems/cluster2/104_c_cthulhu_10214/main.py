#!/usr/bin/env python3
adj = [[] for i in range(n+1)]
dfs(1)
from library import mi, DSU

# read n, m
n, m = mi()
# A connected undirected graph with exactly one cycle has n edges and one cycle
dsu = DSU(n+1)
cycle = 0
for _ in range(m):
    u, v = mi()
    if dsu.find(u) == dsu.find(v):
        cycle += 1
    else:
        dsu.union(u, v)
# check connectivity
connected = len({dsu.find(i) for i in range(1, n+1)}) == 1
print('FHTAGN!' if connected and cycle == 1 else 'NO')
