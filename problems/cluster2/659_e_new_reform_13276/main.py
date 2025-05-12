#!/usr/bin/env python3

import sys
sys.path.append('/home/justinchiu_cohere_com/codecontests-repo/problems/cluster2')
from library import read_ints, create_graph, find_connected_components

def count_acyclic_components(graph):
    """Count the number of acyclic connected components in a graph."""
    components = find_connected_components(graph)
    acyclic_count = 0
    
    for component in components:
        # Check if this component is acyclic (has |V| - 1 edges)
        edge_count = 0
        for vertex in component:
            edge_count += len(graph[vertex])
        
        # In an undirected graph, each edge is counted twice
        edge_count //= 2
        
        # A tree has exactly n-1 edges
        if edge_count == len(component) - 1:
            acyclic_count += 1
    
    return acyclic_count

# Read input
n, m = read_ints()
edges = []

for _ in range(m):
    u, v = read_ints()
    edges.append((u, v))

# Create graph
graph = create_graph(n, edges, directed=False, one_indexed=True)

# Count acyclic components
print(count_acyclic_components(graph))