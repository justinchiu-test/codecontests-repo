#!/usr/bin/env python3

from collections import defaultdict
from library import read_ints, read_int_list

# Read input
n, m = read_ints()
colors = read_int_list()

# Build graph of color connections
color_graph = defaultdict(set)

for _ in range(m):
    a, b = read_ints()
    a -= 1  # Convert to 0-based indexing
    b -= 1
    
    # Skip same color connections
    if colors[a] == colors[b]:
        continue
    
    # Add bidirectional color connections
    color_graph[colors[a]].add(colors[b])
    color_graph[colors[b]].add(colors[a])

# Find color with maximum neighbor diversity
max_diversity = 0
best_color = min(colors)  # Default to minimum color

for color in sorted(color_graph):
    diversity = len(color_graph[color])
    if diversity > max_diversity:
        max_diversity = diversity
        best_color = color

print(best_color)