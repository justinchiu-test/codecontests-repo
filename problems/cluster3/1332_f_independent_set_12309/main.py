#!/usr/bin/env python3

from library import read_int

def get_post_order_traversal(graph, root):
    """
    Get post-order traversal of the tree and parent array.
    
    Returns:
    - parent: Array where parent[i] is the parent of node i
    - order: Post-order traversal of the tree
    """
    n = len(graph)
    parent = [0] * n
    parent[root] = -1  # Mark root
    
    stack = [root]
    order = []
    visited = set([root])
    
    while stack:
        node = stack.pop()
        order.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                stack.append(neighbor)
    
    return parent, order

def get_children_lists(parent):
    """
    Convert parent array to children lists.
    
    Returns:
    - children: Array where children[i] is a list of children of node i
    """
    n = len(parent)
    children = [[] for _ in range(n)]
    
    for child, par in enumerate(parent[1:], 1):
        if par != -1:
            children[par].append(child)
    
    return children

# Constants
MOD = 998244353

# Read input
n = read_int()
graph = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1  # Convert to 0-indexed
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

# Get tree structure
parent, post_order = get_post_order_traversal(graph, 0)
children = get_children_lists(parent)

# Define DP states:
# dp[node][0] = Number of independent sets when node is not in the set and all its incident edges are not chosen
# dp[node][1] = Number of independent sets when node is in the set and all its incident edges are not chosen
# dp[node][2] = Number of independent sets when node is not in the set and at least one of its incident edges is chosen
# dp[node][3] = Number of independent sets when node is in the set and at least one of its incident edges is chosen
# dp[node][4] = Number of independent sets when node is not in the set and all its incident edges are chosen
dp = [[1, 1, 0, 0, 1] for _ in range(n)]

# Process nodes in reverse post-order (bottom-up)
for node in reversed(post_order):
    if not children[node]:  # Leaf node
        continue
    
    res = 1  # Accumulates product for states 0, 1, 4
    res2 = 1  # Accumulates product for state 2
    res3 = 1  # Accumulates product for state 3
    
    for child in children[node]:
        # For states 0, 1, 4: child must be in state 2, 3, or 4
        res = (res * (dp[child][2] + dp[child][3] + dp[child][4])) % MOD
        
        # For state 2: child can be in states 1, 2, 3 (twice), or 4
        res2 = (res2 * (dp[child][1] + dp[child][2] + 2 * dp[child][3] + dp[child][4])) % MOD
        
        # For state 3: child can be in any state, plus additional from states 2 and 3
        res3 = (res3 * (sum(dp[child]) + dp[child][2] + dp[child][3])) % MOD
    
    # Update DP values for the current node
    dp[node][0] = res
    dp[node][1] = res
    dp[node][2] = (res2 - res) % MOD
    dp[node][3] = (res3 - res) % MOD
    dp[node][4] = res

# Final answer: sum of states 2, 3, 4 for the root minus 1 (exclude empty subgraph)
answer = (dp[0][2] + dp[0][3] + dp[0][4] - 1) % MOD
print(answer)