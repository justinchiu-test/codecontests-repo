#!/usr/bin/env python3

from library import enable_fast_io, read_int_tuple

# Enable fast IO
enable_fast_io()

def dfs(node, depth):
    """
    DFS to calculate depth and subtree size.
    Returns the size of the subtree rooted at node.
    """
    visited[node] = True
    depths[node] = depth
    subtree_size = 0
    
    for neighbor in adj[node]:
        if not visited[neighbor]:
            subtree_size += dfs(neighbor, depth + 1) + 1
    
    # Store subtree size
    subtree_sizes[node] = subtree_size
    return subtree_size

# Read input
n, k = read_int_tuple()

# Initialize arrays
visited = [False] * (n + 1)
subtree_sizes = [0] * (n + 1)  # Number of nodes in subtree
depths = [0] * (n + 1)  # Depth of each node from root
adj = [[] for _ in range(n + 1)]  # Adjacency list

# Build the tree
for _ in range(n - 1):
    u, v = read_int_tuple()
    adj[u].append(v)
    adj[v].append(u)

# Run DFS from the capital (node 1)
dfs(1, 0)

# Calculate the "score" for each node
# score = subtree_size - depth
# Higher score means better to be a tourism city
scores = []
for i in range(1, n + 1):
    scores.append(subtree_sizes[i] - depths[i])

# Sort scores in descending order
scores.sort(reverse=True)

# The best strategy is to select n-k cities with highest scores as tourism cities
# The rest k cities will be industrial cities
# The answer is the sum of happiness for all industrial city envoys
print(sum(scores[:n - k]))