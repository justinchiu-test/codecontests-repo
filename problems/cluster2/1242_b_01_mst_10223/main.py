#!/usr/bin/env python3

from library import DSU
import sys

input = sys.stdin.readline

# Read input
n, m = map(int, input().split())

# If m = 0, all vertices form a single component in the complement graph
if m == 0:
    print(0)
    sys.exit(0)

# If m = n*(n-1)/2, the graph is complete and the complement has n components
if m == n * (n - 1) // 2:
    print(n - 1)
    sys.exit(0)

# Create adjacency sets for the original graph
graph = [set() for _ in range(n + 1)]

# Read edges
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].add(y)
    graph[y].add(x)

# Find connected components in the complement graph
visited = [False] * (n + 1)
component_count = 0

# DFS for the complement graph with optimizations
def dfs(start):
    visited[start] = True
    stack = [start]
    
    while stack:
        node = stack.pop()
        
        # For each node, its neighbors in the complement graph are:
        # all nodes except itself and its neighbors in the original graph
        for next_node in range(1, n + 1):
            if next_node != node and not visited[next_node] and next_node not in graph[node]:
                visited[next_node] = True
                stack.append(next_node)

# Process nodes with fewer edges first (optimization)
nodes = sorted(range(1, n + 1), key=lambda x: len(graph[x]))

for node in nodes:
    if not visited[node]:
        component_count += 1
        dfs(node)

print(component_count - 1)