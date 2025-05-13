#!/usr/bin/env python3

from library import tree_painting_rerooting

# Read input
n = int(input())

# Build tree from edges (0-indexed)
adj = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1  # Convert to 0-indexed
    b -= 1
    adj[a].append(b)
    adj[b].append(a)

# Calculate max score using our library function
max_score = tree_painting_rerooting(adj)
print(max_score)