#!/usr/bin/env python3

from library import DSU
from collections import Counter, defaultdict

n, m = map(int, input().split())
dsu = DSU(n)
edges = []

# Process all edges and perform union operations
for _ in range(m):
    p1, p2 = map(int, input().split())
    p1 -= 1  # Convert to 0-indexed
    p2 -= 1
    edges.append(p1)  # Store a source vertex for each edge
    dsu.union(p1, p2)

# Count the number of edges in each component
component_edges = defaultdict(int)
for p1 in edges:
    component_edges[dsu.find(p1)] += 1

# Count the number of nodes in each component
component_nodes = Counter()
for i in range(n):
    component_nodes[dsu.find(i)] += 1

# Check friendship condition: each component must be a complete graph
# For a complete graph with k nodes, there should be k*(k-1)/2 edges
for component, node_count in component_nodes.items():
    expected_edges = (node_count * (node_count - 1)) // 2
    if component_edges[component] != expected_edges:
        print("NO")
        exit()

print("YES")