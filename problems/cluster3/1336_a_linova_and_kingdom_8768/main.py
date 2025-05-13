#!/usr/bin/env python3

from library import setup_io, max_kingdom_happiness

# Fast I/O
input = setup_io()

# Read input
n, k = map(int, input().split())

# Build tree
adj = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = map(int, input().split())
    u -= 1  # Convert to 0-indexed
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

# Calculate maximum happiness
result = max_kingdom_happiness(adj, n, k, root=0, one_indexed=False)
print(result)