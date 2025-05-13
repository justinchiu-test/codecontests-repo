#!/usr/bin/env python3

from library import read_int
from collections import deque

def solve_test_case():
    k = read_int()  # Number of pairs
    n = 2 * k  # Total number of houses/people
    
    # Build the tree with weighted edges
    adj = [[] for _ in range(n + 1)]  # 1-indexed adjacency list
    
    for _ in range(n - 1):
        a, b, weight = map(int, input().split())
        adj[a].append((b, weight))
        adj[b].append((a, weight))
    
    # BFS to determine parent relationships and edge weights
    root = 1  # Arbitrary root
    parents = [0] * (n + 1)
    edge_weights = [0] * (n + 1)  # Weight of edge connecting node to its parent
    parents[root] = root  # Mark root as processed
    
    queue = deque([root])
    bfs_order = []  # Store BFS order for bottom-up processing
    
    while queue:
        node = queue.popleft()
        bfs_order.append(node)
        
        for child, weight in adj[node]:
            if parents[child] == 0:  # Not visited yet
                parents[child] = node
                edge_weights[child] = weight
                queue.append(child)
    
    # Calculate subtree sizes
    subtree_sizes = [1] * (n + 1)  # Initialize all subtree sizes to 1 (just the node itself)
    
    # Process nodes in reverse BFS order (bottom-up)
    minimum = 0  # G - minimum sum
    maximum = 0  # B - maximum sum
    
    for node in reversed(bfs_order):
        if node == root:
            continue  # Skip the root node
            
        parent = parents[node]
        subtree_sizes[parent] += subtree_sizes[node]
        
        # For minimum sum: 
        # If subtree size is odd, it means one person must be separated from their soulmate
        if subtree_sizes[node] % 2 == 1:
            minimum += edge_weights[node]
        
        # For maximum sum:
        # The maximum distance contribution of this edge is:
        # weight * min(subtree_size, total_size - subtree_size)
        edge_contribution = edge_weights[node] * min(subtree_sizes[node], n - subtree_sizes[node])
        maximum += edge_contribution
    
    return minimum, maximum

# Process all test cases
t = read_int()
for _ in range(t):
    min_sum, max_sum = solve_test_case()
    print(min_sum, max_sum)