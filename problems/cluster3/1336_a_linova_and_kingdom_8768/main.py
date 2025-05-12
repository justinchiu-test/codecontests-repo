#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import setup_io, read_tree, get_subtree_size, get_tree_depths, read_ints

input = setup_io()

# Read input
n, k = read_ints()
graph = read_tree(n)

# Calculate depths and subtree sizes
depths = get_tree_depths(graph, root=1)
subtree_sizes = get_subtree_size(graph, root=1, parent=None)

# Calculate the value for each node and sort
values = []
for i in range(1, n + 1):
    # Each node's value is (subtree size - 1) - depth
    # This represents how many nodes in its subtree can be industrial
    # vs the distance penalty for making this node a capital
    values.append(subtree_sizes[i] - 1 - depths[i])

values.sort(reverse=True)

# Take the best (n-k) nodes to be industrial
# The rest will be capitals
print(sum(values[:n-k]))