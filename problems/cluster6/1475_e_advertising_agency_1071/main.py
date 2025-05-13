#!/usr/bin/env python3

from library import combination, MOD, read_int, read_ints, solve_multiple_cases

@solve_multiple_cases
def solve():
    n, k = read_ints()
    a = read_ints()
    
    # Sort the array in descending order to pick bloggers with most followers
    a.sort(reverse=True)
    
    # Count frequency of each follower count
    counts = {}
    for i in a:
        counts[i] = counts.get(i, 0) + 1
    
    # Find the cutoff value (the k-th blogger's follower count)
    cutoff_value = a[k-1]
    
    # Count how many bloggers have more followers than the cutoff
    bloggers_above_cutoff = 0
    for i in range(k):
        if a[i] > cutoff_value:
            bloggers_above_cutoff += 1
    
    # Calculate how many bloggers with the cutoff value we need to select
    slots_to_fill = k - bloggers_above_cutoff
    # Total bloggers with exactly the cutoff value
    total_with_cutoff = counts[cutoff_value]
    
    # Calculate the number of ways to select 'slots_to_fill' bloggers 
    # from 'total_with_cutoff' bloggers
    return combination(total_with_cutoff, slots_to_fill, MOD)