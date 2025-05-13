#!/usr/bin/env python3

from library import best_path_max_gasoline

# Read input
n = int(input())
values = list(map(int, input().split()))

# Build weighted adjacency list
adj = [[] for _ in range(n)]
for _ in range(n-1):
    u, v, w = map(int, input().split())
    u -= 1  # Convert to 0-indexed
    v -= 1
    adj[u].append((v, w))
    adj[v].append((u, w))

# Calculate maximum gasoline
max_gasoline = best_path_max_gasoline(adj, values)
print(max_gasoline)