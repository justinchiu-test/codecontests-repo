#!/usr/bin/env python3

from library import Graph, has_cycle_undirected, count_connected_components

n, m = map(int, input().split())
graph = Graph(n + 1)  # 1-indexed

for _ in range(m):
    a, b = map(int, input().split())
    graph.add_edge(a, b)

# A valid brain network must:
# 1. Be connected (all brains can communicate)
# 2. Have no redundant connectors (no cycles - it should be a tree)

# Check if the graph is connected
if count_connected_components(graph) > 2:  # >2 because we have an extra vertex 0
    print("no")
    exit()

# Check that there are no cycles
if has_cycle_undirected(graph):
    print("no")
    exit()

# Check if there are the right number of edges for a tree (n-1)
# We need to account for vertices that are actually used
active_vertices = 0
for i in range(1, n + 1):
    if graph.neighbors(i):  # If the vertex has any neighbors
        active_vertices += 1

if m != active_vertices - 1:
    print("no")
    exit()

print("yes")