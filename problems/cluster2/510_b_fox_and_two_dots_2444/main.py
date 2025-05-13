#!/usr/bin/env python3

from sys import setrecursionlimit
setrecursionlimit(10**6)

# Process the input
row, col = map(int, input().split())
grid = []

for _ in range(row):
    grid.append(input())

# Directions for adjacent cells (right, down, left, up)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# Function to check if coordinates are valid
def is_valid(r, c):
    return 0 <= r < row and 0 <= c < col

# Function to check if there's a cycle starting from (start_r, start_c) of length >= 4
def has_cycle():
    visited = [[False for _ in range(col)] for _ in range(row)]
    
    # DFS to detect cycle
    def dfs(r, c, prev_r, prev_c, color, length):
        visited[r][c] = True
        
        for i in range(4):
            next_r, next_c = r + dx[i], c + dy[i]
            
            # Skip parent
            if next_r == prev_r and next_c == prev_c:
                continue
                
            # If valid and same color
            if is_valid(next_r, next_c) and grid[next_r][next_c] == color:
                # If already visited and we've moved at least 4 steps (making a cycle)
                if visited[next_r][next_c] and length >= 3:
                    return True
                
                # Continue DFS if not visited
                if not visited[next_r][next_c]:
                    if dfs(next_r, next_c, r, c, color, length + 1):
                        return True
        
        # Backtracking - mark as not visited
        visited[r][c] = False
        return False
    
    # Try starting from each cell
    for r in range(row):
        for c in range(col):
            visited = [[False for _ in range(col)] for _ in range(row)]
            if dfs(r, c, -1, -1, grid[r][c], 0):
                return True
    
    return False

# Check if there's a cycle in the grid
if has_cycle():
    print("Yes")
else:
    print("No")