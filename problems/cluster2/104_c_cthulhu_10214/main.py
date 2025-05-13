#!/usr/bin/env python3

from library import Graph

n, m = map(int, input().split())
graph = Graph(n + 1)  # 1-indexed

# Read edges
for _ in range(m):
    x, y = map(int, input().split())
    graph.add_edge(x, y)

# For a graph to be Cthulhu:
# 1. It must be connected (all vertices must be reachable from any vertex)
# 2. It must have exactly one cycle
# 3. It should have at least 3 vertices (from problem description)

# DFS to check connectivity and count cycles
visited = {}
parent = {}
cycle_count = 0

def dfs(node, parent_node=-1):
    global cycle_count
    visited[node] = True
    
    for neighbor in graph.neighbors(node):
        if neighbor not in visited:
            parent[neighbor] = node
            dfs(neighbor, node)
        elif neighbor != parent_node:
            # Found a back edge (cycle)
            cycle_count += 1

# Start DFS from vertex 1
dfs(1)

# Check if all vertices are visited (connected graph)
is_connected = all(i in visited for i in range(1, n + 1))

# For an undirected graph, each cycle is counted twice
# So we need to check if cycle_count / 2 == 1
if is_connected and cycle_count / 2 == 1:
    print("FHTAGN!")
else:
    print("NO")