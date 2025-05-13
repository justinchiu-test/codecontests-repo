#!/usr/bin/env python3

from library import Graph
from collections import deque

n, m = map(int, input().split())

# Store the non-existing edges (complements of the graph)
non_edges = [set() for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1  # Convert to 0-indexed
    v -= 1
    non_edges[u].add(v)
    non_edges[v].add(u)

# Find connected components
components = []
remaining_vertices = set(range(n))

while remaining_vertices:
    # Start a new component
    start = next(iter(remaining_vertices))
    component = []
    
    # BFS to find all nodes in this component
    queue = deque([start])
    component.append(start)
    remaining_vertices.remove(start)
    
    while queue:
        node = queue.popleft()
        
        # Neighbors are all vertices except those in non_edges[node]
        # and those already visited (not in remaining_vertices)
        neighbors = remaining_vertices - non_edges[node]
        
        for neighbor in neighbors:
            queue.append(neighbor)
            component.append(neighbor)
            remaining_vertices.remove(neighbor)
    
    components.append(len(component))

# Sort components by size and print
components.sort()
print(len(components))
print(" ".join(map(str, components)))