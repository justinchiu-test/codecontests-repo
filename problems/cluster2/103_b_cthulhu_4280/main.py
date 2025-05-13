#!/usr/bin/env python3

from library import get_ints, dfs

n, m = get_ints()

# Cthulhu is a cycle with n vertices and n edges
# So we need n vertices, n edges, and all vertices should be connected
if n >= 3 and n == m:
    # Build the graph
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        x, y = get_ints()
        graph[x].append(y)
        graph[y].append(x)

    # Check if all vertices are connected
    visited = dfs(graph, 1)
    
    # Subtract 1 from visited count since we're using 1-indexed vertices
    print('FHTAGN!' if len(visited) == n else 'NO')
else:
    print('NO')