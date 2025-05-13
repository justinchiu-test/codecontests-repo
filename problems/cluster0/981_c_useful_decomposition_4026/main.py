#!/usr/bin/env python3

from library import read_int, read_ints

def main():
    # Read number of nodes
    n = read_int()
    
    # Initialize variables
    is_valid = True
    degrees = [0] * n  # Track degree of each node
    
    # Read edges
    for _ in range(n - 1):
        u, v = read_ints()
        degrees[u - 1] += 1  # Convert to 0-indexed
        degrees[v - 1] += 1
    
    # Find leaf nodes (degree 1) and central node (degree > 2)
    leaf_nodes = []
    central_node = 0
    
    for i in range(n):
        if degrees[i] == 1:
            leaf_nodes.append(i + 1)  # Convert back to 1-indexed
        elif degrees[i] > 2:
            if central_node == 0:
                central_node = i + 1  # Convert back to 1-indexed
            else:
                # More than one node with degree > 2, not a star-like tree
                print("No")
                is_valid = False
                break
    
    # Output the result
    if is_valid:
        print("Yes")
        if central_node != 0:
            # Star-like tree with a central node
            print(len(leaf_nodes))
            for leaf in leaf_nodes:
                if leaf != central_node:
                    print(central_node, leaf)
        else:
            # Simple path (only two leaf nodes)
            print(1)
            print(leaf_nodes[0], leaf_nodes[1])

if __name__ == "__main__":
    main()