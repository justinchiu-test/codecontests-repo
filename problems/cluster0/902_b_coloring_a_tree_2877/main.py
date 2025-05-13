#!/usr/bin/env python3

from library import read_int, read_ints, bfs

n = read_int()
parent = [0] * (n + 1)
child = [[] for _ in range(n + 1)]

# Read parent-child relationships
parent_list = read_ints()
for i in range(2, n + 1):
    parent_idx = parent_list[i - 2]
    parent[i] = parent_idx
    child[parent_idx].append(i)

# Read colors
colors = read_ints()
node_colors = [0] * (n + 1)
for i in range(1, n + 1):
    node_colors[i] = colors[i - 1]

# BFS traversal starting from the root (node 1)
ans = 0
queue = [1]  # Start with root node
while queue:
    node = queue.pop(0)
    parent_color = 0 if node == 1 else node_colors[parent[node]]
    if parent_color != node_colors[node]:
        ans += 1
    # Add children to the queue
    for child_node in child[node]:
        queue.append(child_node)

print(ans)