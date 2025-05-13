#!/usr/bin/env python3
import sys
import os

# Add the parent directory to the path so we can import the library
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import read_int, read_ints

def solve_test_case():
    n = read_int()
    numbers = read_ints()
    numbers_set = set(numbers)
    max_val = max(numbers)

    # Try each possible k value
    for k in range(1, 2*max_val+1):
        # Check if XORing all numbers by k gives the same set
        valid = True
        for num in numbers:
            xored = num ^ k
            if xored not in numbers_set:
                valid = False
                break

        if valid:
            return k

    return -1

t = read_int()
for _ in range(t):
    result = solve_test_case()
    print(result)
