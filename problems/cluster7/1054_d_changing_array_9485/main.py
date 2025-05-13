#!/usr/bin/env python3
from library import *

def main():
    n, k = read_ints()
    arr = read_ints()
    # prefix XOR with initial 0
    newarr = prefix_xor(arr)
    counts = {}
    mask = (1 << k) - 1
    for num in newarr:
        key = (min(num, mask - num), max(num, mask - num))
        counts[key] = counts.get(key, 0) + 1
    bad = 0
    for m in counts.values():
        half = m // 2
        bad += half * (half - 1) // 2
        half = m - half
        bad += half * (half - 1) // 2
    total = n * (n + 1) // 2
    print(total - bad)

if __name__ == '__main__':
    main()
