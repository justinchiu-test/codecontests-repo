#!/usr/bin/env python3

from library import read_int, read_ints, read_test_cases, print_array, min_cogrowing_sequence

def process_test_case():
    read_int()  # Skip the array length (not needed)
    arr = read_ints()
    return min_cogrowing_sequence(arr)

results = read_test_cases(process_test_case)
for result in results:
    print_array(result)