#!/usr/bin/env python3

from library import setup_io, dfs_with_parent, get_children_array

# Set up fast I/O
input = setup_io()

# Read input
n = int(input())
MOD = 998244353

# Build adjacency list representation
adj = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1  # Convert to 0-indexed
    b -= 1
    adj[a].append(b)
    adj[b].append(a)

# Get DFS visit order and parent array
visit_order, parent = dfs_with_parent(adj, 0)
children = get_children_array(parent, 0)

# dp[node][state]
# state meanings:
# 0: Not in any independent set
# 1: In this independent set, but not in any subgraph that includes parent edge
# 2: Not in this independent set, but in at least one subgraph that includes parent edge
# 3: In this independent set and at least one subgraph that includes parent edge
# 4: Not in this independent set, not in any subgraph that includes parent edge
dp = [[1, 1, 0, 0, 1] for _ in range(n)]

# Process nodes in post-order (bottom-up)
for node in visit_order[::-1]:
    if not children[node]:  # Leaf node
        continue

    # Calculate values for internal nodes
    res = 1   # Product for states 0, 1, 4
    res2 = 1  # Product for state 2
    res3 = 1  # Product for state 3

    for child in children[node]:
        # For each child, calculate contributions to parent states
        res = (res * (dp[child][2] + dp[child][3] + dp[child][4])) % MOD
        res2 = (res2 * (dp[child][1] + dp[child][2] + 2*dp[child][3] + dp[child][4])) % MOD
        res3 = (res3 * (sum(dp[child]) + dp[child][2] + dp[child][3])) % MOD

    # Update dp values for the current node
    dp[node][0] = res
    dp[node][1] = res
    dp[node][2] = (res2 - res) % MOD
    dp[node][3] = (res3 - res) % MOD
    dp[node][4] = res

# Calculate the final answer: sum of states 2, 3, 4 minus 1
result = (dp[0][2] + dp[0][3] + dp[0][4] - 1) % MOD
print(result)