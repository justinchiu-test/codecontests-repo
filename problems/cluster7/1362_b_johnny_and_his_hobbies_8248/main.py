#!/usr/bin/env python3

from library import read_int, read_ints

def solve_test_case():
    n = read_int()
    s = set(read_ints())
    
    # The maximum value in the set is the upper bound for potential k values
    max_val = max(s)
    
    # Try every possible value of k from 1 to 2 * max_val
    for k in range(1, 2 * max_val + 1):
        # For each k, check if XOR with k transforms the set back to itself
        transformed_set = set()
        
        for num in s:
            transformed_set.add(num ^ k)
        
        # If the transformed set equals the original set, we found a valid k
        if transformed_set == s:
            return k
    
    # If no valid k is found
    return -1

# Process each test case
t = read_int()
for _ in range(t):
    print(solve_test_case())