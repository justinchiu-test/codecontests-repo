#!/usr/bin/env python3
import sys
import os

# Add the parent directory to the path so we can import the library
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import read_int, read_int_tuple, xor_range

def solve():
    n = read_int()
    xor_result = 0

    for _ in range(n):
        x, m = read_int_tuple()
        # XOR of all numbers from x to x+m-1 is calculated as:
        # XOR(0 to x+m-1) XOR XOR(0 to x-1)
        xor_result ^= xor_range(x - 1) ^ xor_range(x + m - 1)

    print(["tolik", "bolik"][xor_result == 0])

if __name__ == '__main__':
    solve()
