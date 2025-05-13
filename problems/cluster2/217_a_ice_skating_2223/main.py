#!/usr/bin/env python3

from library import Graph

n = int(input())
points = []

# Read all coordinates
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

# Create a graph where points are connected if they share an x or y coordinate
graph = Graph(n)

# Connect points with same x or y coordinate
for i in range(n):
    for j in range(i + 1, n):
        if points[i][0] == points[j][0] or points[i][1] == points[j][1]:
            graph.add_edge(i, j)

# Count connected components - 1 (we need number of bridges to connect all)
components = graph.find_connected_components()
print(len(components) - 1)