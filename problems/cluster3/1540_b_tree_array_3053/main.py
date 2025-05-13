#!/usr/bin/env python3

from library import read_int, read_int_tuple, enable_fast_io
from collections import deque

def main():
    enable_fast_io()
    
    # Modulus for arithmetic operations
    mod = 10**9 + 7
    
    # Read input
    n = read_int()
    
    # Build the tree
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        x, y = read_int_tuple()
        x -= 1  # Convert to 0-indexed
        y -= 1
        graph[x].append(y)
        graph[y].append(x)
    
    # Precompute Pascal's triangle (for combinations)
    pascal = [[1]]
    pre = [1]
    for i in range(n + 2):
        new_row = [0] * (i + 2)
        for j, a in enumerate(pre):
            new_row[j] = (new_row[j] + a) % mod
            new_row[j + 1] = (new_row[j + 1] + a) % mod
        pascal.append(new_row)
        pre = new_row
    
    # Convert pascal to prefix sums
    for pa in pascal:
        for i in range(len(pa) - 1):
            pa[i + 1] = (pa[i + 1] + pa[i]) % mod
    
    # Precompute powers of 1/2
    half = (mod + 1) >> 1  # This is the modular inverse of 2
    powers_of_half = [1]
    for _ in range(n + 5):
        powers_of_half.append(powers_of_half[-1] * half % mod)
    
    # Inverse of n (for 1/n calculations)
    inv_n = pow(n, mod - 2, mod)
    
    # Calculate the expected number of inversions
    answer = 0
    for root in range(n):
        # Recreate the tree for BFS with root as the starting node
        tree = [[] for _ in range(n)]
        for i in range(n):
            tree[i] = graph[i].copy()
        
        # BFS to get parent and depth information
        parent = [-1] * n
        queue = deque([root])
        nodes_by_bfs = []
        depth = [0] * n
        
        while queue:
            node = queue.popleft()
            nodes_by_bfs.append(node)
            
            for neighbor in tree[node]:
                if neighbor != parent[node]:
                    parent[neighbor] = node
                    tree[neighbor].remove(node)  # Remove the parent from the neighbor's adjacency list
                    queue.append(neighbor)
                    depth[neighbor] = depth[node] + 1
        
        # Calculate subtree sizes
        subtree_size = [1] * n
        for node in reversed(nodes_by_bfs[1:]):  # Skip the root
            subtree_size[parent[node]] += subtree_size[node]
        
        # Calculate inversions contribution
        for node in nodes_by_bfs:
            if node <= root:
                continue
            
            d = depth[node]
            answer = (answer + subtree_size[node] * inv_n) % mod
            
            current = node
            while parent[current] != root:
                p = parent[current]
                s = subtree_size[p] - subtree_size[current]
                contribution = (s * pascal[d-1][depth[p]-1]) % mod
                contribution = (contribution * inv_n) % mod
                contribution = (contribution * powers_of_half[d-1]) % mod
                answer = (answer + contribution) % mod
                current = p
    
    print(answer)

if __name__ == "__main__":
    main()