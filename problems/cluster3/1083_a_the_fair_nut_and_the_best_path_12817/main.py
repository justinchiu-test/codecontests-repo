#!/usr/bin/env python3

from library import read_int, read_ints

# Read input
n = read_int()
a = read_ints()  # Maximum amount of gasoline available at each city
adj = [[] for _ in range(n)]

# Build weighted tree
for _ in range(n-1):
    u, v, w = read_ints()
    u -= 1  # Convert to 0-indexed
    v -= 1
    adj[u].append((v, w))
    adj[v].append((u, w))

# DP arrays
best = [0] * n  # Best path ending at node i
ans = 0  # Global answer

# DFS to find the best path
def dfs(start):
    global ans
    stack = []
    visited = [False] * n
    stack.append((start, -1))  # (node, parent)
    
    while stack:
        u, parent = stack[-1]
        
        if not visited[u]:
            # First visit to node: push all children onto stack
            visited[u] = True
            for v, _ in adj[u]:
                if v != parent:
                    stack.append((v, u))
        else:
            # Post-order processing (when returning from children)
            candidates = []  # Paths from children to current node
            
            # Collect best paths from each child
            for v, weight in adj[u]:
                if v != parent:
                    # For each child, consider its best path minus the cost to reach it
                    path_value = best[v] + a[v] - weight
                    if path_value > 0:
                        candidates.append(path_value)
            
            # Sort candidates in descending order
            candidates.sort(reverse=True)
            
            # Current node's value
            current_value = a[u]
            
            # Take up to 2 best child paths (for a diameter-like path)
            for i in range(min(2, len(candidates))):
                if candidates[i] > 0:
                    current_value += candidates[i]
            
            # Update global answer
            ans = max(ans, current_value)
            
            # Update best path ending at current node (take at most 1 child)
            best[u] = candidates[0] if candidates and candidates[0] > 0 else 0
            
            # Pop processed node
            stack.pop()

# Start DFS from node 0
dfs(0)
print(ans)