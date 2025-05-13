#!/usr/bin/env python3

from library import read_grid, Graph, has_cycle_undirected

# Read input
row, col = map(int, input().split())
grid = read_grid(row)

# Create a graph where nodes are grid cells 
# and edges connect cells of the same color
graph = Graph(row * col, directed=False)

# Helper function to convert (row, col) to node index
def cell_to_node(r, c):
    return r * col + c

# Connect adjacent cells of the same color
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

for r in range(row):
    for c in range(col):
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < row and 0 <= nc < col and grid[r][c] == grid[nr][nc]:
                graph.add_edge(cell_to_node(r, c), cell_to_node(nr, nc))

# Check if the graph has a cycle (cyclic component)
# We need to use a custom cycle detection for undirected graphs
has_cycle = False
visited = {}

def dfs_cycle(node, parent):
    global has_cycle
    if has_cycle:
        return
    
    visited[node] = True
    
    for neighbor in graph.neighbors(node):
        if neighbor != parent:
            if neighbor in visited:
                has_cycle = True
                return
            dfs_cycle(neighbor, node)

# Check each connected component for cycles
for node in range(row * col):
    if node not in visited and not has_cycle:
        dfs_cycle(node, -1)

print("Yes" if has_cycle else "No")