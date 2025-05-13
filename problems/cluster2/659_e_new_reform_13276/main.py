#!/usr/bin/env python3

from library import Graph, has_cycle_undirected, count_connected_components

n, m = map(int, input().split())
graph = Graph(n)

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1  # Convert to 0-indexed
    y -= 1
    graph.add_edge(x, y)

# We need to count the number of connected components without cycles
# For each connected component with no cycle, we need to add a lamp
acyclic_components = 0
visited = {}

def has_cycle(start, visited, parent=-1):
    visited[start] = True
    
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            if has_cycle(neighbor, visited, start):
                return True
        elif neighbor != parent:
            return True
    
    return False

# Check each component for cycles
for i in range(n):
    if i not in visited:
        component_visited = {}
        has_cycle_result = has_cycle(i, component_visited)
        if not has_cycle_result:
            acyclic_components += 1
        visited.update(component_visited)

print(acyclic_components)