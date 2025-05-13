#!/usr/bin/env python3
from sys import path
path.append("/home/justinchiu_cohere_com/codecontests-repo/problems/cluster3")
from library import read_int, read_ints, tree_dp_bottom_up

def main():
    n = read_int()
    values = read_ints()  # Values at each vertex
    
    # Read tree with weights
    adj = [[] for _ in range(n)]
    for _ in range(n-1):
        u, v, w = read_ints()
        u -= 1  # Convert to 0-indexed
        v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    max_sum = [0]  # Using list to allow modification in nested function
    
    # Process function for tree DP - calculate best path ending at this node
    def process_node(node, parent, child_results):
        # Calculate values for paths from children
        child_path_values = []
        child_idx = 0
        
        for neighbor_idx, neighbor in enumerate(adj[node]):
            child, weight = neighbor
            if child != parent:
                # Value gained by extending path to this child 
                # (child's best path - edge weight + child's value)
                path_value = child_results[child_idx] - weight + values[child]
                if path_value > 0:
                    child_path_values.append(path_value)
                child_idx += 1
        
        # Sort paths in descending order
        child_path_values.sort(reverse=True)
        
        # Calculate current node's value plus up to two best children paths
        current_sum = values[node]
        for i in range(min(2, len(child_path_values))):
            if child_path_values[i] > 0:
                current_sum += child_path_values[i]
        
        # Update global maximum
        max_sum[0] = max(max_sum[0], current_sum)
        
        # Return best path ending at this node (using at most one child)
        return child_path_values[0] if child_path_values else 0
    
    # Run bottom-up DP with weighted edges
    tree_dp_bottom_up(adj, process_node, 0, weighted=True)
    print(max_sum[0])

if __name__ == "__main__":
    main()