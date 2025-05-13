#!/usr/bin/env python3

from collections import defaultdict

def has_cycle(graph, start, visited, rec_stack):
    visited[start] = True
    rec_stack[start] = True
    
    for neighbor in graph[start]:
        if not visited[neighbor]:
            if has_cycle(graph, neighbor, visited, rec_stack):
                return True
        elif rec_stack[neighbor]:
            return True
    
    rec_stack[start] = False
    return False

# Read input
n, m = map(int, input().split())
graph = defaultdict(list)
edges = []

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    edges.append((u, v))

# Check if the graph has any cycle
visited = [False] * (n + 1)
rec_stack = [False] * (n + 1)
has_cycle_in_graph = False

for i in range(1, n + 1):
    if not visited[i]:
        if has_cycle(graph, i, visited, rec_stack):
            has_cycle_in_graph = True
            break

if has_cycle_in_graph:
    # For 2 coloring, use the fact that edge from smaller to larger number is color 1
    # Edge from larger to smaller number is color 2
    colors = [str(1 if u < v else 2) for u, v in edges]
    print(2)
    print(' '.join(colors))
else:
    # No cycle means we can use one color
    print(1)
    print(' '.join(['1'] * m))