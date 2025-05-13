#!/usr/bin/env python3

from library import fast_int, fast_int_list, xor_list, answer, prefix_xor

def solve():
    n = fast_int()
    a = fast_int_list()

    # Case 1: If XOR of entire array is 0, we can always partition
    total_xor = xor_list(a)
    if total_xor == 0:
        return True

    # Calculate prefix XORs
    prefix = prefix_xor(a)

    # Case 2: Check if we can partition into exactly 2 segments with equal XOR
    for i in range(1, n):
        # Check if the XOR of first i elements equals the XOR of the rest
        if prefix[i] == (prefix[n] ^ prefix[i]):
            return True

    # Case 3: Check if we can partition into exactly 3 segments with equal XOR
    for i in range(1, n):
        for j in range(i+1, n):
            first_seg = prefix[i]
            second_seg = prefix[j] ^ prefix[i]
            third_seg = prefix[n] ^ prefix[j]

            if first_seg == second_seg and second_seg == third_seg:
                return True

    return False

# Process multiple test cases
for _ in range(fast_int()):
    answer(solve())