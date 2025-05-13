#!/usr/bin/env python3

from library import read_ints, xor_list, print_list

n, m = read_ints()
a = read_ints()
b = read_ints()
if xor_list(a) != xor_list(b):
    print("NO")
    exit(0)

print("YES")
# First row: compute leading element, then remaining b[1:]
first = xor_list(a[1:]) ^ b[0]
print_list([first] + b[1:])
# Remaining rows: each row has one element from a[1:] then zeros
zeros = [0] * (m - 1)
for x in a[1:]:
    print_list([x] + zeros)
