#!/usr/bin/env python3

from library import read_ints, read_int_list

def main():
    # Read input
    n, k = read_ints()
    distances = read_int_list()
    
    # Group nodes by their distance from the root
    nodes_by_dist = [[] for _ in range(n+1)]
    for node, dist in enumerate(distances):
        nodes_by_dist[dist].append(node)
    
    # Check initial conditions
    # 1. There should be exactly one node with distance 0 (the root)
    # 2. The number of nodes at distance 1 should not exceed k (max degree)
    if len(nodes_by_dist[0]) != 1 or len(nodes_by_dist[1]) > k:
        print(-1)
        return
    
    # Check if it's possible to connect all nodes at each level
    for i in range(1, n):
        # Each node at distance i can connect to at most k-1 nodes at distance i+1
        # (because one edge is already used to connect to a node at distance i-1)
        # For the root node (i=0), it can connect to k nodes
        max_connections = len(nodes_by_dist[i]) * (k if i == 0 else k-1)
        if max_connections < len(nodes_by_dist[i+1]):
            print(-1)
            return
    
    # Construct edges
    edges = []
    for i in range(n):
        next_node_idx = 0
        
        if len(nodes_by_dist[i+1]) > 0:
            for current_node in nodes_by_dist[i]:
                current_connections = 0
                
                # Connect to nodes at distance i+1
                max_allowed = k if i == 0 else k-1
                while (current_connections < max_allowed and 
                       next_node_idx < len(nodes_by_dist[i+1])):
                    # Add edge between current node and next available node at distance i+1
                    next_node = nodes_by_dist[i+1][next_node_idx]
                    edges.append((current_node+1, next_node+1))  # Convert to 1-indexed
                    next_node_idx += 1
                    current_connections += 1
    
    # Output the result
    print(len(edges))
    for u, v in edges:
        print(u, v)

if __name__ == "__main__":
    main()