#!/usr/bin/env python3

from library import read_int, make_graph, create_child_array, find_leaf_nodes

def main():
    n = read_int()

    # Read parent-child relationships
    parent = [-1] * (n + 1)  # 1-indexed
    for i in range(2, n + 1):
        parent_node = read_int()
        parent[i] = parent_node

    # Create children array from parent array
    children = [[] for _ in range(n + 1)]
    for i in range(2, n + 1):
        children[parent[i]].append(i)

    # Check spruce property: each non-leaf node must have at least 3 leaf children
    for i in range(1, n + 1):
        # If this is a non-leaf node
        if children[i]:
            # Count leaf children
            leaf_children = 0
            for child in children[i]:
                if not children[child]:  # Child is a leaf if it has no children
                    leaf_children += 1

            # Check if it has at least 3 leaf children
            if leaf_children < 3:
                print("No")
                return

    print("Yes")

if __name__ == "__main__":
    main()