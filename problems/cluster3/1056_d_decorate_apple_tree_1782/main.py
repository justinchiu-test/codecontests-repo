#!/usr/bin/env python3

from library import read_tree_parent_format, count_subtree_leaves

n = int(input())
if n == 1:
    print(1)
    exit()

# Read tree in parent format
adj = read_tree_parent_format(n)

# Count leaves in each subtree - these represent the colors needed
leaf_count = count_subtree_leaves(adj, 1)

# Sort leaf counts to get the answer - skip the dummy element at index 0
colors_needed = sorted(leaf_count[1:])
print(*colors_needed)