#!/usr/bin/env python3

from library import read_graph, find_cyclic_components

# Read input
n, m = map(int, input().split())
graph = read_graph(n, m, directed=False, one_indexed=True)

# Find all cyclic components where each vertex has degree 2
cyclic_count = 0
for component in graph.find_connected_components():
    if graph.is_cyclic_component(component):
        cyclic_count += 1

print(cyclic_count)