#!/usr/bin/env python3

from library import read_int, read_ints

def main():
    # Read input
    n = read_int()
    
    # Parents array (convert to 0-indexed)
    parents = [0] + [p - 1 for p in read_ints()]
    
    # Number of citizens on each square
    citizens = read_ints()
    
    # Determine leaf nodes (squares with no outgoing roads)
    is_leaf = [1] * n  # Initially mark all as leaves
    for i in range(1, n):
        is_leaf[parents[i]] = 0  # Parent nodes are not leaves
    
    # Calculate total citizens and number of leaves in each subtree
    # Process nodes from leaves up to the root (bottom-up)
    for i in range(n - 1, 0, -1):
        parent = parents[i]
        citizens[parent] += citizens[i]  # Add citizens from child to parent
        is_leaf[parent] += is_leaf[i]    # Add leaf count from child to parent
    
    # Calculate the minimum maximum number of citizens that will be caught
    # This is the ceiling of citizens/leaves for each subtree
    max_citizens = 0
    for i in range(n):
        # If is_leaf[i] is 0, this is not a leaf node or subtree
        if is_leaf[i] > 0:
            # Calculate ceiling division (a/b rounded up)
            if citizens[i] % is_leaf[i] == 0:
                max_citizens = max(max_citizens, citizens[i] // is_leaf[i])
            else:
                max_citizens = max(max_citizens, (citizens[i] // is_leaf[i]) + 1)
    
    return max_citizens

print(main())