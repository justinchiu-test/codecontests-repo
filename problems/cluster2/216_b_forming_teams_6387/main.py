#!/usr/bin/env python3

from library import Graph

n, m = map(int, input().split())
graph = Graph(n + 1)  # 1-indexed

for _ in range(m):
    a, b = map(int, input().split())
    graph.add_edge(a, b)

# Count the number of students to bench
# We need to find odd-length cycles and bench one student from each such cycle
visited = {}
odd_cycles = 0

def dfs_cycle(node, parent, colors, depth=0):
    """
    DFS to detect cycles
    colors: 0 = not visited, 1 = being visited, 2 = completely visited
    """
    colors[node] = 1  # Mark as being visited
    
    for neighbor in graph.neighbors(node):
        if neighbor == parent:
            continue
            
        if colors[neighbor] == 0:  # Not visited
            if dfs_cycle(neighbor, node, colors, depth + 1):
                return True
        elif colors[neighbor] == 1:  # Being visited - found a cycle
            # Check if cycle has odd length
            if (depth + 1) % 2 == 1:
                return True
    
    colors[node] = 2  # Mark as completely visited
    return False

def count_odd_cycles():
    colors = {}
    count = 0
    
    for i in range(1, n + 1):
        if i not in colors:
            colors[i] = 0
            
    for i in range(1, n + 1):
        if colors[i] == 0:
            if dfs_cycle(i, -1, colors):
                count += 1
    
    return count

# First approach: Find cycles of odd length
odd_cycles = 0
visited = {}

def dfs(node, parent=-1, depth=0, start=None):
    global odd_cycles
    
    if node in visited:
        # Found a cycle, check if it has odd length
        if start == node and depth % 2 == 1:
            odd_cycles += 1
        return
    
    visited[node] = True
    
    for neighbor in graph.neighbors(node):
        if neighbor != parent:
            dfs(neighbor, node, depth + 1, start if start is not None else node)

for i in range(1, n + 1):
    if i not in visited:
        dfs(i)

# Students to bench = odd cycles + adjust for odd total
students_to_bench = odd_cycles
if (n - students_to_bench) % 2 == 1:
    students_to_bench += 1

print(students_to_bench)