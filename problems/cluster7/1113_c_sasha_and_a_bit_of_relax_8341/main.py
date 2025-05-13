#!/usr/bin/env python3

from library import fast_int, fast_int_list, prefix_xor
from collections import defaultdict

def solve():
    n = fast_int()
    a = fast_int_list()

    # Calculate prefix XOR array
    pref = prefix_xor(a)

    # Keep track of prefixes with the same parity (even/odd length)
    even_parity = defaultdict(int)
    odd_parity = defaultdict(int)

    # Initial state: empty array has even parity
    even_parity[0] = 1

    count = 0

    # For each prefix XOR, check if we've seen the same value with the same parity
    for i in range(1, n+1):
        if i % 2 == 0:  # Even length
            count += even_parity[pref[i]]
            even_parity[pref[i]] += 1
        else:  # Odd length
            count += odd_parity[pref[i]]
            odd_parity[pref[i]] += 1

    return count

print(solve())