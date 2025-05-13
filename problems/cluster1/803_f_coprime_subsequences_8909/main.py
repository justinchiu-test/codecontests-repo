#!/usr/bin/env python3

from library import read_int, read_int_list, MOD
from collections import defaultdict

def count_coprime_subsequences():
    """
    Count the number of subsequences where all elements are coprime (gcd = 1)
    using the inclusion-exclusion principle.
    """
    n = read_int()
    nums = read_int_list()

    # Count occurrences of each factor
    count = defaultdict(int)

    # For each number, increment count for all its divisors
    for num in nums:
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                count[i] += 1
                if i * i != num:  # Avoid counting perfect square divisors twice
                    count[num // i] += 1

    max_k = max(count.keys())

    # Calculate 2^count[k] - 1 for each k (number of non-empty subsets)
    freq = {k: (1 << count[k]) - 1 for k in count}

    # Apply inclusion-exclusion principle
    for k in sorted(count.keys(), reverse=True):
        for multiple in range(k * 2, max_k + 1, k):
            if multiple in freq:
                freq[k] = (freq[k] - freq[multiple]) % MOD

    return freq[1]  # Number of subsequences with gcd = 1

print(count_coprime_subsequences())