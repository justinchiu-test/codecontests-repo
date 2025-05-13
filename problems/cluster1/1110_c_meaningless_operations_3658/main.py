#!/usr/bin/env python3

from library import read_int, get_smallest_prime_factor, is_power_of_two, highest_power_of_2_less_than

def solve_for_number(n):
    # Check if n is one less than a power of 2
    if is_power_of_two(n + 1):
        # n is of form 2^k - 1, so find its largest proper divisor
        # or return 1 if prime
        factor = get_smallest_prime_factor(n)
        return n // factor if factor < n else 1
    else:
        # n is not of form 2^k - 1, the answer is 2^(k+1) - 1
        return (highest_power_of_2_less_than(n) << 1) - 1

def solve():
    n = read_int()
    return solve_for_number(n)

q = read_int()
for _ in range(q):
    print(solve())