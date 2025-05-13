#!/usr/bin/env python3

import sys
import os

# Add parent directory to path to import library
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import read_int, read_ints, combination

def solve():
    # Read input
    n, k = read_ints()  # n = total bloggers, k = number of bloggers to choose
    popularity = read_ints()  # Popularity rating of each blogger
    
    # Sort popularity in ascending order
    popularity.sort()
    
    # Count occurrences of each popularity rating
    counts = {}
    for rating in popularity:
        counts[rating] = counts.get(rating, 0) + 1
    
    # Find the threshold popularity rating
    threshold_index = n - k
    while threshold_index < n - 1 and popularity[threshold_index + 1] == popularity[threshold_index]:
        threshold_index += 1
    
    # Calculate number of ways to choose k bloggers
    # We need to choose (ind - (n - k) + 1) bloggers from those with the threshold popularity
    threshold_rating = popularity[n - k]
    total_with_threshold = counts[threshold_rating]
    needed_from_threshold = threshold_index - (n - k) + 1
    
    # Calculate the combination and print result
    print(combination(total_with_threshold, needed_from_threshold))

# Process all test cases
t = read_int()
for _ in range(t):
    solve()