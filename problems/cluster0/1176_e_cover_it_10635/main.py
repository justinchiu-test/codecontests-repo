#!/usr/bin/env python3

from library import read_ints, read_edges, adj_list

# Read input and build undirected graph
n, m = read_ints()
g = adj_list(n, read_edges(m))

start = max(range(n), key=lambda i: len(g[i]))
vis = [False] * n
vis[start] = True
# Initialize spanning tree edge list
edges = []
queue = [start]
for u in queue:
    for v in g[u]:
        if not vis[v]:
            vis[v] = True
            edges.append((u, v))
            queue.append(v)

for u, v in edges:
    print(u+1, v+1)
