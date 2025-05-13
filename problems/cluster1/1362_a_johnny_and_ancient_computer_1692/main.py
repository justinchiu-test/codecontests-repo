#!/usr/bin/env python3

from library import read_test_cases, read_ints, is_power_of_two

def min_operations(a, b):
    """
    Calculate minimum operations to transform a to b.
    Each operation is multiplying or dividing by 2, 4, or 8.
    """
    if a == b:
        return 0

    # Ensure a is the smaller number
    if a > b:
        a, b = b, a

    # Check if b is a multiple of a
    if b % a != 0:
        return -1

    # Calculate the ratio
    ratio = b // a

    # Check if ratio is a power of 2
    if not is_power_of_two(ratio):
        return -1

    # Calculate operations needed (dividing by 8, 4, and 2)
    # First count the bits (1s in binary representation)
    operations = ratio.bit_length() - 1

    # Operation count using 8, 4, 2 as multipliers
    return (operations + 2) // 3  # Ceiling division by 3

def solve():
    a, b = read_ints()
    return min_operations(a, b)

for result in read_test_cases(solve):
    print(result)