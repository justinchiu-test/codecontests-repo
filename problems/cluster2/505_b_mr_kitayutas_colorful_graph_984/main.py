#!/usr/bin/env python3

from library import Graph, bfs

def build_graph():
    n, m = map(int, input().split())
    
    # Create a graph for each color
    color_graphs = {}
    
    for _ in range(m):
        u, v, c = map(int, input().split())
        if c not in color_graphs:
            color_graphs[c] = Graph(n + 1)  # 1-indexed
        
        color_graphs[c].add_edge(u, v)
    
    return color_graphs

def count_paths(u, v, color_graphs):
    count = 0
    
    for c, graph in color_graphs.items():
        # Check if there's a path between u and v using color c
        visited = bfs(graph, u)
        if v in visited:
            count += 1
    
    return count

if __name__ == "__main__":
    color_graphs = build_graph()
    q = int(input())
    
    for _ in range(q):
        u, v = map(int, input().split())
        print(count_paths(u, v, color_graphs))