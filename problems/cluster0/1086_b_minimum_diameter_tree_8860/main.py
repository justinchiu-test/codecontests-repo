#!/usr/bin/env python3

import sys
sys.path.append('/home/justinchiu_cohere_com/codecontests-repo/problems/cluster0')
from library import read_int_pair, read_ints, format_float

def solution():
    # Read number of vertices and total edge length
    n, s = read_int_pair()
    
    # Special case for n=2
    if n == 2:
        read_ints()  # Read and ignore the edge (only one possible tree)
        return format_float(s)
    
    # Count degree of each vertex
    degree = [0] * n
    for _ in range(n - 1):
        u, v = read_int_pair()
        degree[u - 1] += 1
        degree[v - 1] += 1
    
    # Count leaf nodes (vertices with degree 1)
    leaf_count = sum(1 for d in degree if d == 1)
    
    # Calculate and print the result with required formatting
    result = 2 * (s / leaf_count)
    return format_float(result)

if __name__ == "__main__":
    print(solution())