#!/usr/bin/env python3

from library import read_int, read_ints, read_test_cases, find_xor_mapping_key

def process_test_case():
    read_int()  # Skip array length
    numbers = read_ints()
    return find_xor_mapping_key(numbers)

results = read_test_cases(process_test_case)
for result in results:
    print(result)