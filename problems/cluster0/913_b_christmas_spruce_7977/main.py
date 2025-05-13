#!/usr/bin/env python3

from library import read_int

def main():
    n = read_int()
    
    # Create arrays to represent the tree
    is_non_leaf = [False] * (n + 1)  # Track which nodes are non-leaves
    children = [[] for _ in range(n + 1)]  # Store children of each node
    leaf_children_count = [0] * (n + 1)  # Count of leaf children for each node
    
    # Read parent information and build the tree
    for i in range(2, n + 1):
        parent = read_int()
        children[parent].append(i)
        is_non_leaf[parent] = True
    
    # DFS to calculate leaf children counts
    def dfs(node):
        leaf_count = 0
        
        for child in children[node]:
            # If the child is a leaf node, increment leaf count
            if not is_non_leaf[child]:
                leaf_count += 1
            else:
                # Recursively process non-leaf child
                dfs(child)
        
        leaf_children_count[node] = leaf_count
    
    # Start DFS from the root
    dfs(1)
    
    # Check if the tree is a spruce
    for i in range(1, n + 1):
        # Check if each non-leaf node has at least 3 leaf children
        if is_non_leaf[i] and leaf_children_count[i] < 3:
            print("No")
            return
    
    print("Yes")

if __name__ == "__main__":
    main()