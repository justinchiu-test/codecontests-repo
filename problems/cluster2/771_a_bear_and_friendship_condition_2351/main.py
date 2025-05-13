#!/usr/bin/env python3

from library import DSU
from collections import Counter

n, m = map(int, input().split())
dsu = DSU(n + 1)  # 1-indexed
edges = []  # Store edges for validation

# Process all edges
for _ in range(m):
    p1, p2 = map(int, input().split())
    edges.append(p1)  # Track the first endpoint for each edge
    dsu.union(p1, p2)

# For each connected component, check if it forms a complete graph
# In a complete graph with k vertices, there should be k*(k-1)/2 edges

# Count vertices in each component
component_sizes = Counter()
for i in range(1, n + 1):
    component_sizes[dsu.find(i)] += 1

# Count edges in each component - only count one endpoint for each edge
edge_counts = Counter([dsu.find(i) for i in edges])

# Check friendship condition: each component must form a complete graph
def check_friendship_condition():
    for component in component_sizes:
        vertices = component_sizes[component]
        expected_edges = (vertices * (vertices - 1)) // 2
        actual_edges = edge_counts[component]
        
        if actual_edges != expected_edges:
            return False
    return True

if check_friendship_condition():
    print("YES")
else:
    print("NO")