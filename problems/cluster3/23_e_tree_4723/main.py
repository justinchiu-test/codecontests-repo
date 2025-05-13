#!/usr/bin/env python3

from library import read_int, read_int_tuple, enable_fast_io, max_product_components

def main():
    enable_fast_io()
    
    # Read input
    n = read_int()
    
    # Build the tree
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = read_int_tuple()
        u -= 1  # Convert to 0-indexed
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    
    # Calculate the maximum product of connected components
    result = max_product_components(graph)
    
    print(result)

if __name__ == "__main__":
    main()