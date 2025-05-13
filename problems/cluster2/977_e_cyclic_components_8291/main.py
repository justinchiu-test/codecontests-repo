#!/usr/bin/env python3

from library import Graph
from collections import deque

n, m = map(int, input().split())
graph = Graph(n)

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1  # Convert to 0-indexed
    v -= 1
    graph.add_edge(u, v)

def is_cycle(start, visited):
    # BFS to check if all nodes in the component have degree 2
    component = []
    queue = deque([start])
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        component.append(node)
        
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                visited[neighbor] = True
                queue.append(neighbor)
    
    # Check if each node in the component has degree 2
    for node in component:
        if len(graph.neighbors(node)) != 2:
            return False
    
    return True

visited = {}
count = 0

for i in range(n):
    if i not in visited:
        if is_cycle(i, visited):
            count += 1

print(count)