#!/usr/bin/env python3

from library import Graph

n, m = map(int, input().split())
graph = Graph(n + 1)  # 1-indexed

# Build the graph from input
for _ in range(m):
    a, b = map(int, input().split())
    graph.add_edge(a, b)

# Check each connected component
components = graph.find_connected_components()

# Filter out the 0th vertex component (since it's 1-indexed)
components = [comp for comp in components if 0 not in comp]

# Check if each component is a complete graph
for component in components:
    vertex_count = len(component)
    edge_count = 0
    
    # Count edges in this component
    for vertex in component:
        edge_count += len(graph.adj[vertex])
    
    # Each edge is counted twice (once from each end)
    edge_count //= 2
    
    # Check if it's a complete graph
    expected_edges = (vertex_count * (vertex_count - 1)) // 2
    
    if edge_count != expected_edges:
        print("No")
        exit()

print("Yes")