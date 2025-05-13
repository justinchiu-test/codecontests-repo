#!/usr/bin/env python3

from library import read_int, read_ints, xor_sum, read_test_cases

def solve_test_case():
    n = read_int()
    a = read_ints()
    
    # Calculate the total XOR of the array
    total_xor = xor_sum(a)
    
    # If the total XOR is 0, we can split the array into equal segments
    if total_xor == 0:
        return "YES"
    
    # Check if we can split into exactly 2 segments with equal XOR
    current_xor = 0
    segment_count = 0
    
    for i in range(len(a) - 1):
        current_xor ^= a[i]
        if current_xor == total_xor:
            segment_count += 1
            current_xor = 0
            
    # If we found at least 2 segments with XOR equal to total XOR,
    # and the remaining elements also have XOR equal to total XOR,
    # then the answer is Yes
    if segment_count >= 2:
        return "YES"
    
    # Check if we can form exactly 3 equal segments
    current_xor = 0
    segment_count = 0
    
    for i in range(len(a)):
        current_xor ^= a[i]
        if current_xor == total_xor:
            segment_count += 1
            current_xor = 0
    
    return "YES" if segment_count >= 2 else "NO"

# Process each test case
for result in read_test_cases(solve_test_case):
    print(result)