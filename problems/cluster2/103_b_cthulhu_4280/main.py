#!/usr/bin/env python3

from library import Graph

n, m = map(int, input().split())

# For a graph to be Cthulhu:
# 1. It must have exactly n edges (to form a single cycle with trees)
# 2. It must be connected (all vertices must be reachable from any vertex)
# 3. It must have at least 3 vertices

if n < 3 or n != m:
    print("NO")
    exit()

# Build the graph
graph = Graph(n + 1)  # 1-indexed

for _ in range(m):
    x, y = map(int, input().split())
    graph.add_edge(x, y)

# Check if the graph is connected
visited = {}

def dfs(node):
    visited[node] = True
    for neighbor in graph.neighbors(node):
        if neighbor not in visited:
            dfs(neighbor)

# Start DFS from vertex 1
dfs(1)

# If all vertices are visited, the graph is connected
if len(visited) == n:
    print("FHTAGN!")
else:
    print("NO")