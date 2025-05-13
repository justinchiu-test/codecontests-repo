#!/usr/bin/env python3

from library import read_int, read_ints, MultiColumnSegmentTree

def main():
    # Read input
    n = read_int()
    a = read_ints()
    
    # Initialize segment tree for efficient range sum queries
    tree = MultiColumnSegmentTree(n)
    
    # Map values to their ranks (0-indexed)
    ranks = {val: idx for idx, val in enumerate(sorted(a))}
    
    # Count triplets where a[i] > a[j] > a[k] and i < j < k
    result = 0
    
    # Process the array from right to left
    for i in range(n - 1, -1, -1):
        rank = ranks[a[i]]
        
        # Count elements processed so far that are greater than a[i]
        # and have another element greater than them (column 1)
        result += tree.query(rank, 1)
        
        # Update the first column (count of elements)
        tree.update(rank, 1, 0)
        
        # Update the second column (count of elements with another element greater than them)
        tree.update(rank, tree.query(rank, 0), 1)
    
    return result

if __name__ == "__main__":
    print(main())