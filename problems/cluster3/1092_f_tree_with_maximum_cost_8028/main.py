#!/usr/bin/env python3

from library import read_int, read_ints, bootstrap, enable_fast_io
from collections import deque

# Enable fast I/O
enable_fast_io()

# Read input
n = read_int()
weights = read_ints()  # Values assigned to each vertex
tree = [[] for _ in range(n + 1)]  # 1-indexed adjacency list

# Build the tree
for _ in range(n - 1):
    u, v = read_ints()
    tree[u].append(v)
    tree[v].append(u)

# DP arrays
dp = [0] * (n + 1)  # dp[node] = sum of dist(node, i) * a_i for all i in subtree of node
subtree_sum = [0] * (n + 1)  # subtree_sum[node] = sum of weights in subtree of node
ans = [0] * (n + 1)  # ans[node] = cost of tree with node as root

@bootstrap
def dfs1(node, dist, parent):
    """First DFS to calculate DP values and subtree sums."""
    for child in tree[node]:
        if child == parent:
            continue
        yield dfs1(child, dist + 1, node)
        dp[node] += dp[child]
        subtree_sum[node] += subtree_sum[child]
    
    dp[node] += weights[node - 1] * dist  # Add current node's contribution
    subtree_sum[node] += weights[node - 1]  # Add current node's weight to subtree sum
    yield dp[node]

# Run first DFS from root node 1
dfs1(1, 0, 1)
ans[1] = dp[1]  # Answer for root node

# BFS to reroot the tree and calculate all answers
queue = deque()
for child in tree[1]:
    queue.append((child, 1))  # (node, parent)

while queue:
    node, parent = queue.popleft()
    
    # Calculate cost when rerooted at node
    # Formula: ans[node] = ans[parent] - (contribution of node's subtree to parent) + (contribution of parent's subtree to node)
    # Contribution of node's subtree to parent: dp[node] + subtree_sum[node]
    # Contribution of parent's subtree to node: (total_sum - subtree_sum[node]) + dp[parent]
    
    # Calculate answer for current node
    node_subtree_contribution = dp[node] + subtree_sum[node]
    remaining_tree_sum = subtree_sum[1] - subtree_sum[node]
    ans[node] = ans[parent] - node_subtree_contribution + remaining_tree_sum + dp[node]
    
    # Add node's children to queue
    for child in tree[node]:
        if child != parent:
            queue.append((child, node))

# Print maximum possible cost
print(max(ans[1:]))  # Skip ans[0] as we're 1-indexed