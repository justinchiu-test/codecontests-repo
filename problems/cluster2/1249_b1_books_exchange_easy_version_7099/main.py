#!/usr/bin/env python3

from library import DSU

def solve_test_case():
    n = int(input())
    p = list(map(int, input().split()))
    
    # Create a DSU with n elements
    dsu = DSU(n)
    
    # Union elements based on book exchange (0-indexed)
    for i, book_destination in enumerate(p):
        dsu.union(i, book_destination - 1)  # Adjust for 0-indexing
    
    # For each student, print the size of their cycle (time needed to get their book back)
    return [dsu.get_size(i) for i in range(n)]

# Process all test cases
t = int(input())
for _ in range(t):
    print(*solve_test_case())