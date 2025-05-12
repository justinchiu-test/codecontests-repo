#!/usr/bin/env python3

import sys
sys.path.append('/home/justinchiu_cohere_com/codecontests-repo/problems/cluster2')
from library import read_ints, create_graph

def solve_forming_teams():
    n, m = read_ints()
    
    # Read edges
    edges = []
    for _ in range(m):
        a, b = read_ints()
        edges.append((a, b))
    
    # Create graph (vertices are 1-indexed)
    graph = create_graph(n+1, edges, directed=False, one_indexed=True)
    
    # Track visited nodes and cycle-related information
    visited = [0] * (n+1)
    cycle_count = 0
    
    def dfs_util(v, parent):
        nonlocal topology_sort, has_odd_cycle
        
        visited[v] = 1
        
        for neighbor in graph[v]:
            if visited[neighbor] == 0:
                dfs_util(neighbor, v)
                topology_sort += 1
            # Found a cycle (and not just going back to parent)
            elif neighbor != parent and v != parent:
                topology_sort += 1
                has_odd_cycle = True
    
    # Process each component
    for i in range(1, n+1):
        if visited[i] == 0:
            topology_sort = 0
            has_odd_cycle = False
            
            dfs_util(i, i)
            
            # If we found an odd-length cycle with at least 3 nodes, we need to exclude one student
            if topology_sort % 2 == 1 and topology_sort >= 3 and has_odd_cycle:
                cycle_count += 1
    
    # Final result: if total - excluded is odd, exclude one more
    return cycle_count + (1 if (n - cycle_count) % 2 == 1 else 0)

print(solve_forming_teams())