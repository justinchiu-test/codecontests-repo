#!/usr/bin/env python3

from library import Graph

inp = input().split()
n = int(inp[0])
m = int(inp[1])

# A graph is a Cthulhu if it has exactly one cycle and is connected
# This means it should have n vertices and n edges (exactly one cycle)
# and all vertices should be reachable from any starting point

if n >= 3 and n == m:
    # Create a graph with n vertices
    graph = Graph(n)
    
    # Add edges
    for _ in range(m):
        x, y = map(int, input().split())
        graph.add_edge(x-1, y-1)  # Convert to 0-indexed
    
    # Check if all vertices are visited from vertex 0
    visited = graph.dfs(0)
    
    # All vertices should be reachable
    if all(visited):
        print('FHTAGN!')
    else:
        print('NO')
else:
    print('NO')