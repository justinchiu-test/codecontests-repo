#!/usr/bin/env python3

from collections import deque
from library import read_int, read_int_list

def main():
    n = read_int()
    
    # Initialize parent and children mappings
    parent = {i: 0 for i in range(1, n+1)}
    children = {i: [] for i in range(1, n+1)}
    
    # Read parent information
    parents_list = read_int_list()
    for i in range(2, n+1):
        parent[i] = parents_list[i-2]
        children[parents_list[i-2]].append(i)
    
    # Read colors
    colors_list = read_int_list()
    color = {i: colors_list[i-1] for i in range(1, n+1)}
    
    # BFS to traverse the tree
    queue = deque([1])
    paint_count = 0
    
    while queue:
        node = queue.popleft()
        parent_color = 0 if node == 1 else color[parent[node]]
        
        # If color is different from parent, need to paint
        if parent_color != color[node]:
            paint_count += 1
        
        # Add children to queue
        for child in children[node]:
            queue.append(child)
    
    print(paint_count)

if __name__ == "__main__":
    main()