#!/usr/bin/env python3

from library import read_int, read_ints

# Read input
n = read_int()
w = read_ints()  # Available gasoline at each city
adj = [[] for _ in range(n)]  # Adjacency list

# Build the tree with edge weights
for _ in range(n-1):
    u, v, c = read_ints()
    u -= 1  # 0-indexed
    v -= 1
    adj[u].append((v, c))
    adj[v].append((u, c))

# DP array for best path from subtree
best = [0] * n
ans = 0  # Final answer

def dfs(start):
    global ans
    stack = [(start, -1)]  # (node, parent)
    visited = [False] * n
    
    while stack:
        node, parent = stack[-1]
        
        if not visited[node]:
            # First visit: mark visited and push children
            visited[node] = True
            all_children_visited = True
            
            for child, _ in adj[node]:
                if child != parent and not visited[child]:
                    stack.append((child, node))
                    all_children_visited = False
            
            # If all children already visited, process node
            if all_children_visited:
                process_node(node, parent)
                stack.pop()
        else:
            # Already visited, process and pop
            process_node(node, parent)
            stack.pop()

def process_node(node, parent):
    global ans
    
    # Collect best paths from children
    paths = []
    for child, cost in adj[node]:
        if child != parent:
            # Value of path = best path from child + gasoline at child - cost to reach
            path_value = best[child] + w[child] - cost
            if path_value > 0:  # Only consider positive contributions
                paths.append(path_value)
    
    # Sort paths in descending order
    paths.sort(reverse=True)
    
    # Current node's value (gasoline available at this node)
    current = w[node]
    
    # Add up to two best paths (for a diameter-like path through this node)
    for i in range(min(2, len(paths))):
        if paths[i] > 0:
            current += paths[i]
    
    # Update global answer
    ans = max(ans, current)
    
    # Update best path ending at current node (at most one child path)
    best[node] = paths[0] if paths and paths[0] > 0 else 0

# Start DFS from node 0
dfs(0)

# Handle the case of a single node
if n == 1:
    ans = w[0]

print(ans)