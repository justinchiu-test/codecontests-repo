#!/usr/bin/env python3

from library import get_ints

def main(): 
    n, m = get_ints()
    graph = [[] for _ in range(n+1)]
    
    for _ in range(m):
        x, y = get_ints()
        graph[x].append(y)
        graph[y].append(x)
    
    # Check each connected component: 
    # - If there is a cycle, we can orient roads to avoid any separate city
    # - If no cycle, we need one separate city
    
    visited = [False] * (n+1)
    tree_components = 0
    
    def dfs_check_cycle(node, parent):
        visited[node] = True
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if visited[neighbor]:
                # Found a cycle
                return True
            if dfs_check_cycle(neighbor, node):
                return True
        return False
    
    for i in range(1, n+1):
        if not visited[i]:
            # If component has no cycle, it's a tree and needs one separate city
            if not dfs_check_cycle(i, -1):
                tree_components += 1
    
    print(tree_components)

if __name__ == "__main__":
    main()