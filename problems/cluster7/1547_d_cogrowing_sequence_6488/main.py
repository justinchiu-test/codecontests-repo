#!/usr/bin/env python3

from library import fast_int, fast_int_list

def min_co_growing_sequence_with(array):
    sequence, prev_value = [], 0
    for value in array:
        n = prev_value & (prev_value ^ value)
        prev_value = value ^ n
        sequence.append(n)
    return ' '.join(map(str, sequence))

def solve_test_case():
    fast_int()  # consume n
    return min_co_growing_sequence_with(fast_int_list())

for _ in range(fast_int()):
    print(solve_test_case())