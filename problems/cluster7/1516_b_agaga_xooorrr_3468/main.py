#!/usr/bin/env python3

from library import read_int, read_ints, read_test_cases, print_yes_no, can_have_equal_xor_segments

def process_test_case():
    read_int()  # Array length not needed
    arr = read_ints()
    return can_have_equal_xor_segments(arr)

results = read_test_cases(process_test_case)
for result in results:
    print_yes_no(result)