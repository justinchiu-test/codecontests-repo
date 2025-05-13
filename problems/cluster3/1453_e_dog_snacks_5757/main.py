#!/usr/bin/env python3

from library import read_int, read_int_tuple, enable_fast_io

def dog_snacks_min_k(graph, n):
    """
    Calculate the minimum k for Dog Snacks problem.
    
    Args:
        graph: Adjacency list
        n: Number of nodes
        
    Returns:
        Minimum possible value of k
    """
    # Track degree of each node
    degree = [0] * (n + 1)
    degree[1] = 1  # Root starts with degree 1
    
    # Track parent of each node
    parent = [0] * (n + 1)
    
    # DFS to build parent relationships and count degrees
    stack = [1]  # Start with root (node 1)
    leaf_nodes = []
    
    while stack:
        node = stack.pop()
        for child in graph[node]:
            if child != parent[node]:
                degree[node] += 1
                parent[child] = node
                stack.append(child)
        
        if degree[node] == 0:  # Leaf node
            leaf_nodes.append(node)
    
    # Tracks (distance_to_leaf, max_path)
    subtree_data = [[] for _ in range(n + 1)]
    
    # Bottom-up DP calculation
    while leaf_nodes:
        node = leaf_nodes.pop()
        p = parent[node]
        
        if not subtree_data[node]:  # Node is a leaf
            subtree_data[p].append((1, 0))
        elif len(subtree_data[node]) == 1:  # Node has one child
            d, k = subtree_data[node][0]
            subtree_data[p].append((d + 1, k))
        else:  # Node has multiple children
            d = min(data[0] for data in subtree_data[node]) + 1
            k = max(
                max(data[1] for data in subtree_data[node]),  # Max of child paths
                max(data[0] for data in subtree_data[node]) + 1  # Max dist + 1
            )
            subtree_data[p].append((d, k))
        
        degree[p] -= 1
        if degree[p] == 0:
            leaf_nodes.append(p)
    
    # Calculate result for root (node 1)
    root = 1
    if len(subtree_data[root]) == 1:
        return max(subtree_data[root][0])
    else:
        k = max(data[1] for data in subtree_data[root])
        distances = [data[0] for data in subtree_data[root]]
        m = max(distances)
        distances.remove(m)
        return max(max(distances)+1, m, k)

def main():
    enable_fast_io()
    t = read_int()  # Number of test cases
    
    for _ in range(t):
        n = read_int()  # Number of intersections
        
        # Build tree as adjacency list with 1-indexing
        graph = [[] for _ in range(n + 1)]
        
        # Read edges
        for _ in range(n - 1):
            u, v = read_int_tuple()
            graph[u].append(v)
            graph[v].append(u)
        
        # Solve the problem
        result = dog_snacks_min_k(graph, n)
        print(result)

if __name__ == "__main__":
    main()