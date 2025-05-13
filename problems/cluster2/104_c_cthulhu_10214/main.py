#!/usr/bin/env python3

from library import Graph

n, m = map(int, input().split())

# For a graph to be a Cthulhu, it must have exactly one cycle and all vertices must be connected
# This means for n vertices, we must have exactly n edges (one more than needed for a tree)

if n >= 3 and n == m:
    graph = Graph(n)
    
    # Read edges and build graph
    for _ in range(m):
        x, y = map(int, input().split())
        graph.add_edge(x-1, y-1)  # Convert to 0-indexed
    
    # Check if the graph is connected and has exactly one cycle
    visited = [False] * n
    parent = [-1] * n
    cycle_count = [0]  # Use a list to track cycle count to avoid nonlocal
    
    # Custom visit function to check for back edges (indicates cycles)
    def dfs_cycle_check(u):
        visited[u] = True
        
        for v in graph.adj[u]:
            if not visited[v]:
                parent[v] = u
                dfs_cycle_check(v)
            elif v != parent[u]:
                cycle_count[0] += 1
    
    # Run DFS to check for cycles
    dfs_cycle_check(0)
    
    # Check if all vertices are reachable
    all_connected = all(visited)
    
    # Since each cycle is counted twice (once from each direction), divide by 2
    cycle_count[0] //= 2
    
    if all_connected and cycle_count[0] == 1:
        print('FHTAGN!')
    else:
        print('NO')
else:
    print('NO')