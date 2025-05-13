#!/usr/bin/env python3

from collections import Counter
from library import read_int, read_int_list

def main():
    n = read_int()
    
    # Calculate depth for each node in the tree
    depths = [0]  # Root node (node 1) has depth 0
    
    # Read parent information and calculate depths
    if n > 1:
        parents = read_int_list()  # p2, p3, ..., pn where pi is the parent of node i
        
        # For each node, set its depth as parent's depth + 1
        for i in range(2, n + 1):
            parent = parents[i - 2]  # Adjust index since parents list is 0-indexed
            parent_depth = depths[parent - 1]  # Adjust for 0-indexed depths list
            depths.append(parent_depth + 1)
    
    # Count nodes at each depth
    depth_counts = Counter(depths)
    
    # Count depths with odd number of nodes
    # When an odd number of apples are at a level, one apple will survive and reach the root
    result = sum(count & 1 for count in depth_counts.values())
    
    print(result)

if __name__ == "__main__":
    main()