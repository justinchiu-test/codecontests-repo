#!/usr/bin/env python3

from library import get_ints, detect_cycle

n, m = get_ints()
graph = [[] for _ in range(n+1)]

# Build graph
for _ in range(m):
    x, y = get_ints()
    graph[x].append(y)
    graph[y].append(x)

# Check if all vertices are connected
visited = set()
dfs_count = 0

def dfs(u):
    visited.add(u)
    for v in graph[u]:
        if v not in visited:
            dfs(v)

# Start DFS from vertex 1
dfs(1)
is_connected = len(visited) == n

# Check for exactly one cycle
has_cycle = detect_cycle(graph, 1, True)

# Cthulhu has exactly one cycle and all vertices are connected
if is_connected and has_cycle and n == m:
    print('FHTAGN!')
else:
    print('NO')