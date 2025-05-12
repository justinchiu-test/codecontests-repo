#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import setup_io, read_tree, get_subtree_size, read_int, tree_rerooting

input = setup_io()

n = read_int()
graph = read_tree(n, indexed_from=0)

# Calculate subtree sizes
subtree_sizes = get_subtree_size(graph, root=0, parent=None)

# Initial DP value for the root
dp = [0] * n
dp[0] = sum(subtree_sizes)

# Get parent pointers
parents = [0] * n
visited = [False] * n
visited[0] = True  # Mark root as visited
stack = [0]
while stack:
    node = stack.pop()
    for neighbor in graph[node]:
        if not visited[neighbor]:
            parents[neighbor] = node
            visited[neighbor] = True
            stack.append(neighbor)

# Re-root to find optimal value
max_score = dp[0]
stack = [0]

while stack:
    node = stack.pop()
    for child in graph[node]:
        if parents[child] == node:  # Only process children
            # Re-root DP calculation
            dp[child] = dp[node] + n - 2 * subtree_sizes[child]
            max_score = max(max_score, dp[child])
            stack.append(child)

print(max_score)