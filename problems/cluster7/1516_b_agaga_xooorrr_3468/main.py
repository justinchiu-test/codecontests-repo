#!/usr/bin/env python3
import sys
import os

# Add the parent directory to the path so we can import the library
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import read_int, read_ints, xor_list, is_xor_zero

def solve_test_case():
    n = read_int()
    a = read_ints()
    
    # If the XOR of the entire array is 0, we can always split it
    total_xor = xor_list(a)
    if is_xor_zero(a):
        return "YES"
    
    # Try to find a way to split the array into 3 segments
    # such that the first two have XOR values equal to the total XOR
    current_xor = 0
    found_segments = 0
    
    for val in a:
        current_xor ^= val
        if current_xor == total_xor:
            found_segments += 1
            current_xor = 0
            
        if found_segments == 2:
            return "YES"
    
    return "NO"

t = read_int()
for _ in range(t):
    print(solve_test_case())