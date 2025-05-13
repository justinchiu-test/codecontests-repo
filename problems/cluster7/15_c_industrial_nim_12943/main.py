#!/usr/bin/env python3

from library import read_int, read_ints, xor_range

def solve():
    n = read_int()
    total_xor = 0
    
    for _ in range(n):
        x, m = read_ints()
        # XOR of range [x, x+m-1] can be calculated as XOR of [1, x+m-1] XOR [1, x-1]
        total_xor ^= xor_range(x - 1) ^ xor_range(x + m - 1)
    
    # In Nim, if XOR sum is 0, second player wins; otherwise, first player wins
    print("bolik" if total_xor == 0 else "tolik")

if __name__ == '__main__':
    solve()