#!/usr/bin/env python3

import sys
sys.path.append('/home/justinchiu_cohere_com/codecontests-repo/problems/cluster2')
from library import create_graph, read_ints, find_connected_components

def count_cyclic_components(graph):
    """Count components where each vertex has exactly 2 neighbors."""
    components = find_connected_components(graph)
    count = 0
    
    for component in components:
        is_cyclic = True
        
        # Check if all vertices in this component have exactly 2 neighbors
        for vertex in component:
            if len(graph[vertex]) != 2:
                is_cyclic = False
                break
        
        if is_cyclic:
            count += 1
    
    return count

n, m = read_ints()
edges = [read_ints() for _ in range(m)]

graph = create_graph(n, edges, directed=False, one_indexed=True)
print(count_cyclic_components(graph))