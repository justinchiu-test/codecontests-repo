#!/usr/bin/env python3
from library import *

def main():
    n = read_int()
    a = read_ints()
    # prefix XOR array
    pref = prefix_xor(a)
    # dp for parity-based counts
    dp = [[0] * (2**20 + 5) for _ in range(2)]
    ans = 0
    for i, v in enumerate(pref):
        ans += dp[i % 2][v]
        dp[i % 2][v] += 1
    print(ans)

if __name__ == '__main__':
    main()
