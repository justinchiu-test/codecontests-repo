#!/usr/bin/env python3

from library import Graph, count_connected_components

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    
    # Create an undirected graph
    graph = Graph(n)
    
    # Read the direct links (edges) that Holmes has already found
    for _ in range(m):
        v, w = map(int, input().split())
        v -= 1  # Convert to 0-indexed
        w -= 1
        graph.add_edge(v, w)
    
    # Find the connected components
    visited = {}
    component_sizes = []
    
    def dfs(node):
        visited[node] = True
        size = 1
        
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                size += dfs(neighbor)
        
        return size
    
    # Count the number of connected components and their sizes
    cc = 0
    for i in range(n):
        if i not in visited:
            size = dfs(i)
            component_sizes.append(size)
            cc += 1
    
    # If there's only one connected component, the problem is already solved
    if cc == 1:
        print(1 % k)
        exit()
    
    # Calculate the number of ways to add T direct links to connect all components
    # T = cc - 1 (minimum number of links needed to connect cc components)
    # Answer is (n^(cc-2)) * (product of component sizes)
    
    ans = 1
    # Compute n^(cc-2) % k
    for i in range(cc - 2):
        ans = (ans * n) % k
    
    # Multiply by product of component sizes
    for size in component_sizes:
        ans = (ans * size) % k
    
    print(ans)