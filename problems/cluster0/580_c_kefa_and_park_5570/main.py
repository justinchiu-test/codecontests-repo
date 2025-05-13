#!/usr/bin/env python3

from library import read_ints, read_int_list

# Read input
n, m = read_ints()
cats = read_int_list()

# Create tree
tree = [[] for i in range(n)]
for _ in range(n-1):
    x, y = read_ints()
    tree[x-1].append(y-1)
    tree[y-1].append(x-1)

# BFS traversal to find valid restaurants
visited = [0] * n
result = 0
queue = [(0, 0)]  # (vertex, consecutive cats)
i = 0

while i < len(queue):
    vertex, cat_count = queue[i]
    visited[vertex] = 1
    
    # Calculate new number of consecutive cats
    new_cat_count = 0
    if cats[vertex] == 1:
        new_cat_count = cat_count + 1
    else:
        new_cat_count = 0
    
    # Check if we're below the maximum consecutive cats threshold
    if new_cat_count <= m:
        is_leaf = True
        for neighbor in tree[vertex]:
            if not visited[neighbor]:
                is_leaf = False
                queue.append((neighbor, new_cat_count))
        
        # If it's a leaf node and valid path, count it
        if is_leaf and vertex != 0:  # Not counting the root
            result += 1
    
    i += 1

print(result)