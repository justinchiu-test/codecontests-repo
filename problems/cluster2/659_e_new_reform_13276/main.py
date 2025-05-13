#!/usr/bin/env python3

from library import Graph
import sys

sys.setrecursionlimit(200000)

def main():
    n, m = map(int, input().split())
    graph = Graph(n + 1)  # 1-indexed
    
    # Read edges
    for _ in range(m):
        x, y = map(int, input().split())
        graph.add_edge(x, y)
    
    # We need to count the number of connected components that are trees (have no cycles)
    visited = [False] * (n + 1)
    
    def is_tree(start):
        """Check if the connected component starting from 'start' is a tree (no cycles)"""
        parent = [-1] * (n + 1)
        
        def dfs_check_cycle(vertex, par):
            visited[vertex] = True
            parent[vertex] = par
            
            for neighbor in graph.adj[vertex]:
                if neighbor == par:
                    continue
                elif not visited[neighbor]:
                    if not dfs_check_cycle(neighbor, vertex):
                        return False
                else:
                    # Found a back edge (cycle)
                    return False
            return True
        
        return dfs_check_cycle(start, -1)
    
    # Count connected components that are trees
    tree_count = 0
    for i in range(1, n + 1):
        if not visited[i]:
            if is_tree(i):
                tree_count += 1
    
    print(tree_count)

if __name__ == "__main__":
    main()