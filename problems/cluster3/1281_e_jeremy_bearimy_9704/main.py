#!/usr/bin/env python3

from library import read_int

def solve_test_case():
    k = read_int()  # Number of pairs
    n = 2 * k  # Total number of houses/people
    
    # Build the tree with weighted edges
    adj = [[] for _ in range(n)]  # 0-indexed adjacency list
    
    for _ in range(n - 1):
        a, b, t = map(int, input().split())
        a -= 1  # Convert to 0-indexed
        b -= 1
        adj[a].append((b, t))
        adj[b].append((a, t))
    
    # BFS to determine parent relationships
    root = 0  # Arbitrary root
    parents = [None] * n
    queue = [root]  # Use list as queue for simplicity
    queue_index = 0
    
    while queue_index < len(queue):
        node = queue[queue_index]
        queue_index += 1
        
        for neighbor, _ in adj[node]:
            if neighbor != parents[node]:
                queue.append(neighbor)
                parents[neighbor] = node
    
    # DP arrays
    has_odd_subtree = [False] * n  # d1: Whether subtree has odd number of nodes
    subtree_size = [0] * n  # d2: Size of subtree
    
    min_sum = 0  # G - minimum sum
    max_sum = 0  # B - maximum sum
    
    # Process nodes in reverse BFS order (bottom-up)
    for node_index in range(len(queue) - 1, -1, -1):
        node = queue[node_index]
        parent = parents[node]
        
        # Initialize with current node
        parity_count = 1  # Count for parity check
        total_count = 1  # Total subtree size
        
        # Process all child subtrees
        for neighbor, weight in adj[node]:
            if neighbor != parent:
                # For minimum sum: If child subtree has odd size, one edge must cross
                if has_odd_subtree[neighbor]:
                    min_sum += weight
                    parity_count += 1  # Account for odd subtree
                
                # For maximum sum: Calculate contribution based on subtree sizes
                neighbor_size = subtree_size[neighbor]
                max_sum += weight * min(neighbor_size, n - neighbor_size)
                
                # Update total count with child subtree size
                total_count += neighbor_size
        
        # Update node's DP values
        has_odd_subtree[node] = parity_count % 2 == 1  # Odd number of odd subtrees means this subtree is odd
        subtree_size[node] = total_count
    
    return min_sum, max_sum

# Process all test cases
t = read_int()
for _ in range(t):
    min_sum, max_sum = solve_test_case()
    print(min_sum, max_sum)