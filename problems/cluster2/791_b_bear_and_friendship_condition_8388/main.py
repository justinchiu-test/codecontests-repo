#!/usr/bin/env python3

import sys
sys.path.append('/home/justinchiu_cohere_com/codecontests-repo/problems/cluster2')
from library import read_ints, create_graph, find_connected_components, yes_no

def check_friendship_condition(graph):
    """
    Check if each connected component forms a complete graph.
    
    Args:
        graph: Adjacency list representation
        
    Returns:
        True if condition is satisfied, False otherwise
    """
    # Find connected components
    components = find_connected_components(graph)
    
    for component in components:
        vertices = len(component)
        edges = sum(len(graph[v]) for v in component) // 2  # Each edge is counted twice
        
        # Check if number of edges equals n*(n-1)/2 (complete graph)
        if edges != (vertices * (vertices - 1)) // 2:
            return False
    
    return True

# Read input
n, m = read_ints()
edges = []

for _ in range(m):
    u, v = read_ints()
    edges.append((u, v))

# Create graph
graph = create_graph(n, edges, directed=False, one_indexed=True)

# Check friendship condition
print(yes_no(check_friendship_condition(graph), uppercase=False))