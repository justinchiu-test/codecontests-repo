#!/usr/bin/env python3

from library import build_bridge_tree, get_tree_diameter, readline

# Read input
n, m = map(int, readline().split())

# Create graph representation using adjacency lists
adj = [[] for _ in range(n)]
edge_index = [[] for _ in range(n)]

for ei in range(m):
    u, v = map(int, readline().split())
    u -= 1  # Convert to 0-indexed
    v -= 1
    adj[u].append(v)
    adj[v].append(u)
    edge_index[u].append(ei)
    edge_index[v].append(ei)

# Build the bridge tree
bridge_tree = build_bridge_tree(n, m, adj, edge_index)

# Get the diameter of the bridge tree
diameter = get_tree_diameter(bridge_tree)

print(diameter)
