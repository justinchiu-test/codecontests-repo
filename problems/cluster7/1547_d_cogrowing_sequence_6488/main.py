#!/usr/bin/env python3

from library import read_int, read_ints, min_cogrowing_sequence, read_test_cases

def solve_test_case():
    n = read_int()
    arr = read_ints()
    return ' '.join(map(str, min_cogrowing_sequence(arr)))

# Process each test case
for result in read_test_cases(solve_test_case):
    print(result)