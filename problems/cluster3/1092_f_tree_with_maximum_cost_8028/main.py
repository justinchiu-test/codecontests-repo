#!/usr/bin/env python3

from library import setup_io, bootstrap
from collections import deque

# Set up fast I/O
input = setup_io()

# Read input
n = int(input())
values = list(map(int, input().split()))
total_value = sum(values)

# Build tree (1-indexed)
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

# Calculate initial cost with node 1 as root
# dp[node] = cost of subtree rooted at node
# sum_values[node] = sum of values in subtree rooted at node
dp = [0] * (n + 1)
sum_values = [0] * (n + 1)
costs = [0] * (n + 1)  # Final costs for each possible root

@bootstrap
def dfs1(node, depth, parent):
    """First DFS to calculate subtree costs with node 1 as root."""
    for child in adj[node]:
        if child == parent:
            continue
        yield dfs1(child, depth + 1, node)
        dp[node] += dp[child]
        sum_values[node] += sum_values[child]

    # Add the contribution of the current node
    dp[node] += values[node - 1] * depth
    sum_values[node] += values[node - 1]
    yield

# Run first DFS starting from node 1
dfs1(1, 0, -1)
costs[1] = dp[1]

# Re-rooting technique: recompute costs for each node as root
# BFS to propagate costs
queue = deque()
for child in adj[1]:
    queue.append((child, 1))

while queue:
    node, parent = queue.popleft()

    # Calculate cost when node is the root:
    # 1. Take parent's cost
    # 2. Subtract contribution of node's subtree
    # 3. Add new contribution from parent's subtree
    parent_subtree = costs[parent] - (dp[node] + sum_values[node])

    # When we reroot, distances to nodes in parent's subtree increase by 1
    new_contribution = total_value - sum_values[node]

    # Combine costs: parent's subtree + node's subtree with node as root
    costs[node] = parent_subtree + new_contribution + dp[node]

    # Add node's children to queue
    for child in adj[node]:
        if child != parent:
            queue.append((child, node))

# Result is the maximum cost among all possible roots
print(max(costs[1:]))
