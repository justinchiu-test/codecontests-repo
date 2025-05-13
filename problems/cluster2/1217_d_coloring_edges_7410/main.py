#!/usr/bin/env python3

from library import Graph
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = Graph(n + 1, directed=True)

# Store the edge list for later coloring
edges = []
for i in range(m):
    x1, x2 = map(int, input().split())
    graph.add_edge(x1, x2)
    edges.append((x1, x2, i))  # Store edge index for coloring

# Prepare for cycle detection
visited = [False] * (n + 1)
rec_stack = [False] * (n + 1)
has_cycle = False

# DFS to detect cycles
def dfs(v):
    global has_cycle
    visited[v] = True
    rec_stack[v] = True
    
    for u in graph.adj[v]:
        if not visited[u]:
            if dfs(u):
                return True
        elif rec_stack[u]:
            has_cycle = True
            return True
    
    rec_stack[v] = False
    return False

# Run DFS from each unvisited vertex
for i in range(1, n + 1):
    if not visited[i]:
        if dfs(i):
            break

# Simple coloring based on the directed property
ans2 = []
for i in range(m):
    x1, x2 = edges[i][0], edges[i][1]
    ans2.append(str((x1 < x2) + 1))  # Forward edges: color 1, backward: color 2

# Output
if has_cycle:
    print(2)
    print(' '.join(ans2))
else:
    print(1)
    print(' '.join(['1'] * m))