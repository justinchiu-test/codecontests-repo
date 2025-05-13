#!/usr/bin/env python3
import sys
import os

# Add the parent directory to the path so we can import the library
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import read_int_tuple, is_power_of_two

def solve():
    n, x = read_int_tuple()

    # Special case: can't have exactly 2 numbers with XOR 0
    if n == 2 and x == 0:
        print("NO")
        return

    print("YES")

    # Special cases for n=1 and n=2
    if n == 1:
        print(x)
        return

    if n == 2:
        print(f"{x} 0")
        return

    # For n ≥ 3, we'll use the approach from the original code with large powers of 2
    # to ensure we can create any XOR value
    a = 2**17  # A large power of 2
    b = 2**18  # Another large power of 2

    # Include the first n-3 positive integers
    running_xor = 0
    for i in range(1, n-2):
        print(i, end=" ")
        running_xor ^= i

    # Determine the last 3 numbers to achieve the target XOR
    if running_xor == x:
        # If we already have the target XOR, use numbers with XOR 0
        print(f"{a} {b} {a+b}")
    else:
        # Otherwise adjust to reach the target XOR
        print(f"0 {a} {a^running_xor^x}")

solve()
