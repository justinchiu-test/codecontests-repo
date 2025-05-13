#!/usr/bin/env python3
from library import read_tree, set_recursion_limit, optimal_edge_removal

# Set recursion limit for large inputs
set_recursion_limit(300000)

# Read input
n = int(input())
tree = read_tree(n)

# Calculate and print the result
print(optimal_edge_removal(tree, n))