#!/usr/bin/env python3

from library import read_int_tuple, enable_fast_io, diameter_cuts

def main():
    enable_fast_io()
    
    # Read input
    n, k = read_int_tuple()
    
    # Build the tree
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = read_int_tuple()
        a -= 1  # Convert to 0-indexed
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    
    # Calculate the number of valid sets of edges
    result = diameter_cuts(graph, k)
    
    # Print result
    print(result)

if __name__ == "__main__":
    main()