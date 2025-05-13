#!/usr/bin/env python3
from sys import path
path.append("/home/justinchiu_cohere_com/codecontests-repo/problems/cluster3")
from library import read_int, read_ints, tree_dp_bottom_up

def main():
    n = read_int()
    
    # Read node operations (0 = min, 1 = max)
    operations = [0] + read_ints()
    
    # Read parent nodes (1-indexed)
    parents = [0, 0] + read_ints()
    
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for i in range(2, n + 1):
        adj[parents[i]].append(i)
    
    # Identify leaf nodes
    is_leaf = [1] * (n + 1)
    for i in range(2, n + 1):
        is_leaf[parents[i]] = 0
    
    # Count leaves in the tree
    leaf_count = sum(is_leaf) - 1  # Exclude node 0
    
    # Process function for tree DP - find minimum path count
    def process_node(node, parent, child_results):
        # If it's a leaf node, we need 1 path
        if is_leaf[node]:
            return 1
        
        if not child_results:  # Empty node (should not happen in this problem)
            return 0
        
        # If operation is MIN, sum the paths of all children
        if operations[node] == 0:
            return sum(child_results)
        # If operation is MAX, take the minimum path among children
        else:
            return min(child_results)
    
    # Calculate minimum paths to leaves from each node
    min_paths = tree_dp_bottom_up(adj, process_node, 1)
    
    # Calculate the maximum number of leaves that can be reached
    print(leaf_count - min_paths[1] + 1)

if __name__ == "__main__":
    main()