#!/usr/bin/env python3

from library import read_ints, make_graph
from collections import deque

def main():
    n, m = read_ints()  # n: number of nodes, m: max consecutive cats
    cats = read_ints()  # cats[i] indicates if node i has a cat
    
    # Build the tree
    graph = make_graph(n)
    for _ in range(n - 1):
        x, y = read_ints()
        x -= 1  # Convert to 0-indexed
        y -= 1
        graph[x].append(y)
        graph[y].append(x)
    
    # BFS traversal
    visited = [False] * n
    restaurant_count = 0
    queue = deque([(0, 0)])  # (node, consecutive_cats)
    
    while queue:
        node, consecutive_cats = queue.popleft()
        visited[node] = True
        
        # Update consecutive_cats count
        if cats[node] == 1:
            consecutive_cats += 1
        else:
            consecutive_cats = 0
        
        # If too many consecutive cats, skip this path
        if consecutive_cats > m:
            continue
        
        # Check if it's a leaf (restaurant)
        is_leaf = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                is_leaf = False
                queue.append((neighbor, consecutive_cats))
        
        # If it's a leaf and we can reach it, count it
        if is_leaf and node != 0:
            restaurant_count += 1
    
    print(restaurant_count)

if __name__ == "__main__":
    main()