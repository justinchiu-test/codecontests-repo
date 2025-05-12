#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import read_test_cases, read_int, get_prime_factor_counts

def solve_case():
    n = read_int()
    factor_counts = get_prime_factor_counts(n)

    if not factor_counts:
        # n is a prime number
        print(1)
        print(n)
        return

    # Find the prime with the highest count
    max_prime, max_count = max(factor_counts.items(), key=lambda x: x[1])

    # Create the sequence
    sequence = [max_prime] * (max_count - 1)

    # Calculate the last element
    last_element = n
    for p in sequence:
        last_element //= p

    sequence.append(last_element)

    # Print the result
    print(len(sequence))
    print(*sequence)

for _ in range(read_test_cases()):
    solve_case()
