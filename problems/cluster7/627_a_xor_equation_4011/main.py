#!/usr/bin/env python3

from library import read_ints

def solve():
    s, x = read_ints()
    
    # Check if a solution exists
    # For an equation a + b = s and a ^ b = x, we need:
    # 1. s ≥ x (since a + b ≥ a ^ b for non-negative integers)
    # 2. (s - x) must be even (due to the relationship between + and ^)
    if s < x or (s - x) % 2 != 0:
        print(0)
        return
    
    # Calculate the components:
    # u represents the common bits in a and b (a & b)
    # d represents the different bits (a ^ b), which is x
    common_bits = (s - x) // 2
    different_bits = x
    
    result = 1
    
    # Process each bit position
    while common_bits > 0 or different_bits > 0:
        # Extract lowest bit
        u_bit = common_bits & 1
        d_bit = different_bits & 1
        
        # Check bit combinations:
        # If a bit is 1 in both common and different parts, impossible situation
        if u_bit == 1 and d_bit == 1:
            result = 0
            break
        # If a bit is 0 in common but 1 in different, we have two choices (a=0,b=1 or a=1,b=0)
        elif u_bit == 0 and d_bit == 1:
            result *= 2
        
        # Move to next bit
        common_bits >>= 1
        different_bits >>= 1
    
    # Special case: if s = x, we need to exclude cases where both a and b are 0,
    # or both a and b are equal to s/2
    if s == x:
        result = max(0, result - 2)
    
    print(result)

if __name__ == "__main__":
    solve()