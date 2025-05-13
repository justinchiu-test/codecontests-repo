#!/usr/bin/env python3

from library import fast_ints, print_list

def solve(u, v):
    # Check if u > v (impossible case)
    if u > v:
        return -1

    # Both are zero case
    if u == 0 and v == 0:
        return 0

    # Single number case: u equals v
    if u == v:
        return [1, u]

    # Check parity: difference between v and u must be even
    if (v - u) % 2 != 0:
        return -1

    # Try with two numbers
    half_diff = (v - u) // 2
    a = u + half_diff
    b = half_diff

    if a + b == v and a ^ b == u:
        return [2, a, b]

    # Try with three numbers
    a, b, c = u, half_diff, half_diff
    if a + b + c == v and a ^ b ^ c == u:
        return [3, a, b, c]

    # No solution
    return -1

u, v = fast_ints()
result = solve(u, v)

if result == -1 or result == 0:
    print(result)
else:
    print_list(result)