#!/usr/bin/env python3

import sys
sys.path.append('/home/justinchiu_cohere_com/codecontests-repo/problems/cluster2')
from library import read_ints, UndirectedGraph

def has_cycle(graph, rows, cols, grid):
    """Check if the graph has a cycle of the same color."""
    visited = {}
    for vertex in graph.vertices():
        visited[vertex] = False
    
    def dfs_cycle(current, parent):
        visited[current] = True
        
        for neighbor in graph.neighbors(current):
            if not visited[neighbor]:
                if dfs_cycle(neighbor, current):
                    return True
            elif neighbor != parent:
                return True
        
        return False
    
    # Run DFS for each unvisited vertex
    for vertex in graph.vertices():
        if not visited[vertex]:
            if dfs_cycle(vertex, -1):
                return True
    
    return False

# Process input
rows, cols = read_ints()
grid = [input() for _ in range(rows)]

# Create the graph
graph = UndirectedGraph(rows * cols)

# Connect cells of the same color if they are adjacent
for i in range(rows):
    for j in range(cols):
        current = i * cols + j
        color = grid[i][j]
        
        # Connect to the right
        if j + 1 < cols and grid[i][j+1] == color:
            graph.add_edge(current, i * cols + j + 1)
        
        # Connect to the bottom
        if i + 1 < rows and grid[i+1][j] == color:
            graph.add_edge(current, (i+1) * cols + j)

# Check if there's a cycle
print("Yes" if graph.has_cycle() else "No")