#!/usr/bin/env python3

from library import read_test_cases, read_int, get_prime_factors_with_counts

def solve():
    n = read_int()

    # Get prime factorization with counts
    factors = get_prime_factors_with_counts(n)

    if not factors:  # If n is 1
        return [1, [n]]

    # Find the prime factor with the highest frequency
    max_factor = max(factors.items(), key=lambda x: x[1])
    prime, count = max_factor

    # Create the sequence
    result = [prime] * (count - 1)
    last_number = n
    for _ in range(count - 1):
        last_number //= prime

    result.append(last_number)

    return [count, result]

for length, sequence in read_test_cases(solve):
    print(length)
    print(*sequence)