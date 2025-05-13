#!/usr/bin/env python3

from library import read_int_pair, print_count_and_array

u, v = read_int_pair()

if u > v:
    print(-1)
elif u == v == 0:
    print(0)
elif u == v:
    print_count_and_array(1, [u])
else:
    # Check if we can construct a solution
    if u % 2 != v % 2 or (v - u) % 2 != 0:
        print(-1)
        exit()

    # Try with 2 numbers
    half_diff = (v - u) // 2
    if u & half_diff == 0:  # No bits overlap
        print_count_and_array(2, [u + half_diff, half_diff])
    else:
        # Use 3 numbers
        print_count_and_array(3, [u, half_diff, half_diff])