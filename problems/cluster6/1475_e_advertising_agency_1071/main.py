#!/usr/bin/env python3

from library import read_int, read_ints, Combinatorics, MOD, read_test_cases

# Initialize combinatorics with precomputed factorials
combinatorics = Combinatorics()

def solve():
    n, k = read_ints()
    a = read_ints()
    
    # Sort in descending order to get the k highest values
    a.sort(reverse=True)
    
    # Count frequency of each value
    freq = {}
    for i in a:
        freq[i] = freq.get(i, 0) + 1
    
    # The kth highest value
    kth_value = a[k-1]
    
    # How many of the kth value are in the top k
    count_in_top_k = sum(1 for i in range(k) if a[i] == kth_value)
    
    # Total count of the kth value
    total_count = freq[kth_value]
    
    # We need to choose count_in_top_k elements from total_count
    return combinatorics.combination(total_count, count_in_top_k)

for _ in read_test_cases():
    print(solve())