#!/usr/bin/env python3
from library import mi, connected_components

# read n, m
n, m = mi()
# A connected undirected graph with n>=3 nodes and n edges has exactly one simple cycle
if n >= 3 and m == n:
    # build adjacency list (1-indexed)
    e = [[] for _ in range(n+1)]
    for _ in range(m):
        x, y = mi()
        e[x].append(y)
        e[y].append(x)
    # check connectivity
    comps = connected_components(e[1:])
    print('FHTAGN!' if len(comps) == 1 else 'NO')
else:
    print('NO')
