#!/usr/bin/env python3
from library import ints, read_tree, bfs_with_cats

n, m = ints()
cats = ints()
tree = read_tree(n)

# Find leaf nodes reachable without exceeding m consecutive cats
print(bfs_with_cats(tree, cats, m))