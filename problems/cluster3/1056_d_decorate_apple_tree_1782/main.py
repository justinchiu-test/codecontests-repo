#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import count_subtree_leaves, read_int, setup_io

input = setup_io()

# Read input
n = read_int()
if n == 1:
    print("1")
    exit()

# Create adjacency list
graph = [[] for _ in range(n+1)]
parents = list(map(int, input().split()))
for i in range(2, n+1):
    graph[i].append(parents[i-2])
    graph[parents[i-2]].append(i)

# Count leaves in each subtree
colors = count_subtree_leaves(graph, 1)[1:]  # Remove node 0
colors.sort()  # Sort colors needed

print(*colors)