#!/usr/bin/env python3

from library import read_int

def calculate_max_depth(tree, roots):
    """Calculate maximum tree depth starting from any root node"""
    def find_depth(node):
        if not tree[node]:  # Leaf node
            return 1
        
        return 1 + max(find_depth(child) for child in tree[node])
    
    return max(find_depth(root) for root in roots)

def main():
    n = read_int()
    
    # Initialize tree
    tree = [[] for _ in range(n)]
    roots = []
    
    # Read employee relations
    for i in range(n):
        manager = read_int()
        
        if manager > 0:
            # This employee has a manager
            tree[manager-1].append(i)
        else:
            # This is a root employee (no manager)
            roots.append(i)
    
    # Calculate and print the maximum depth
    print(calculate_max_depth(tree, roots))

if __name__ == "__main__":
    main()