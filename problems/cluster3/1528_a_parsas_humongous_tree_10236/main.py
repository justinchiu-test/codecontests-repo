#!/usr/bin/env python3

from library import read_int, read_int_tuple, enable_fast_io, parsas_tree_max_beauty

def main():
    enable_fast_io()
    
    t = read_int()  # Number of test cases
    
    for _ in range(t):
        n = read_int()  # Number of vertices
        
        # Read the lower and upper bounds for each vertex
        bounds = []
        for _ in range(n):
            l, r = read_int_tuple()
            bounds.append((l, r))
        
        # Build the tree
        graph = [[] for _ in range(n)]
        for _ in range(n - 1):
            a, b = read_int_tuple()
            a -= 1  # Convert to 0-indexed
            b -= 1
            graph[a].append(b)
            graph[b].append(a)
        
        # Calculate the maximum beauty of the tree
        result = parsas_tree_max_beauty(graph, bounds)
        print(result)

if __name__ == "__main__":
    main()