#!/usr/bin/env python3

import sys
sys.path.append('/home/justinchiu_cohere_com/codecontests-repo/problems/cluster2')
from library import read_ints

def find_components_in_complement_graph(n, non_edges):
    """
    Find connected components in the complement graph.
    
    Args:
        n: Number of vertices
        non_edges: List of non-adjacent vertices for each vertex
        
    Returns:
        List of component sizes
    """
    vertex_set = set(range(n))
    components = []
    
    while vertex_set:
        # Pick a starting vertex
        start = next(iter(vertex_set))
        vertex_set.remove(start)
        
        # DFS with stack
        stack = [start]
        component_size = 1
        
        while stack:
            current = stack.pop()
            
            # Get neighbors in the complement graph (vertices that are not non-edges)
            neighbors = vertex_set - non_edges[current]
            component_size += len(neighbors)
            
            # Add neighbors to stack and remove from unvisited set
            stack.extend(neighbors)
            vertex_set &= non_edges[current]  # Keep only non-neighbors in vertex_set
        
        components.append(component_size)
    
    return sorted(components)

# Read input
n, m = read_ints()

# Initialize non-edges (vertices that are NOT connected)
# In a complement graph, we track vertices that are NOT connected
non_edges = [{i} for i in range(n)]  # Initially, each vertex is not connected to itself

# Read edges and mark them as non-edges in the complement graph
for _ in range(m):
    u, v = read_ints()
    u -= 1  # Convert to 0-indexed
    v -= 1
    non_edges[u].add(v)
    non_edges[v].add(u)

# Find connected components in the complement graph
result = find_components_in_complement_graph(n, non_edges)

# Print result
print(len(result))
print(" ".join(map(str, result)))