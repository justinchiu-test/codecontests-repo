#!/usr/bin/env python3

import sys
sys.path.append('/home/justinchiu_cohere_com/codecontests-repo/problems/cluster2')
from library import read_ints, create_graph, count_connected_components

def is_cthulhu(n, m, graph):
    """
    Check if the graph is Cthulhu (single connected component with exactly one cycle).
    
    For Cthulhu, we need:
    1. n vertices and n edges (for exactly one cycle)
    2. All vertices must be in a single connected component
    """
    if n < 3 or n != m:
        return False
    
    # Need exactly one connected component
    return count_connected_components(graph) == 1

# Read input
n, m = read_ints()
edges = [read_ints() for _ in range(m)]

# Create graph (vertices are 1-indexed in the input)
graph = create_graph(n, edges, directed=False, one_indexed=True)

# Check if the graph is Cthulhu and print result
if is_cthulhu(n, m, graph):
    print("FHTAGN!")
else:
    print("NO")