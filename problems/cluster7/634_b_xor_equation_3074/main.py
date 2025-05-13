#!/usr/bin/env python3

from library import read_ints, get_bit

def solve():
    s, x = read_ints()
    
    # Check if a solution is possible
    # s = a + b, x = a ^ b
    # For a solution to exist, s - x must be even
    if x > s or (s - x) % 2 != 0:
        print(0)
        return
    
    # Calculate (s - x) / 2, which represents the common bits in a and b
    common_bits = (s - x) // 2
    
    # Each bit position has two options (0-0 or 1-1) for common bits,
    # while for different bits (x has 1), there's only one option (0-1 or 1-0)
    result = 1
    invalid = False
    
    for bit in range(64):  # Check up to 64 bits to be safe
        mask = 1 << bit
        
        # If x has a 1 at this position (different bits)
        if get_bit(x, bit) == 1:
            # Double the result for each bit position with a 1 in x
            result *= 2
            
            # If common_bits also has a 1 here, it's invalid (cannot be both common and different)
            if get_bit(common_bits, bit) == 1:
                invalid = True
                break
    
    # Special case: when s = x, we need to subtract 2 (the cases where a = 0, b = 0 or a = s, b = 0)
    if s == x:
        result -= 2
    
    # If we found an invalid configuration
    if invalid:
        result = 0
    
    print(result)

if __name__ == "__main__":
    solve()