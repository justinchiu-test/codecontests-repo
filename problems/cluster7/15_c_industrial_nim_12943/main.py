#!/usr/bin/env python3

from library import fast_int, fast_ints, xor_range

def solve():
    n = fast_int()
    nim_sum = 0

    # Process each pile
    for _ in range(n):
        x, m = fast_ints()
        # The Nim value is XOR(1...x-1) ^ XOR(1...x+m-1)
        # = XOR(x...x+m-1)
        nim_sum ^= xor_range(x - 1) ^ xor_range(x + m - 1)

    # In Nim, the player who faces a zero nim-sum loses
    # In this version, "tolik" moves first, so if nim_sum is 0, tolik loses
    winner = "bolik" if nim_sum == 0 else "tolik"
    print(winner)

if __name__ == '__main__':
    solve()