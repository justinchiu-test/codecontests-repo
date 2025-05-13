#!/usr/bin/env python3

from library import read_ints

def main():
    # Read input
    n, m = read_ints()
    
    # Initialize adjacency list for the graph
    adj = [[] for _ in range(n+1)]
    
    # Read edges and build the graph
    for _ in range(m):
        x, y = read_ints()
        adj[x].append(y)
        adj[y].append(x)
    
    # Find node 1's degree (problems seem to expect 1 as the high-degree node)
    # Create a spanning tree with node 1 as the central node
    
    # Track visited nodes
    visited = [False] * (n+1)
    visited[1] = True
    
    # Store edges of the spanning tree
    spanning_tree_edges = []
    
    # Queue for BFS
    queue = [1]
    
    # BFS to construct a spanning tree
    while queue:
        node = queue.pop(0)
        
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                spanning_tree_edges.append((node, neighbor))
                queue.append(neighbor)
    
    # Output the spanning tree edges
    for u, v in spanning_tree_edges:
        print(u, v)

if __name__ == "__main__":
    main()