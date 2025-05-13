#!/usr/bin/env python3

from library import read_ints, read_matrix, find_nonzero_xor_combination

n, m = read_ints()
a = read_matrix(n)

# Try to find a combination of elements (one from each row) with non-zero XOR
result = find_nonzero_xor_combination(a)

if result:
    print("TAK")
    print(' '.join(map(str, result)))
else:
    print("NIE")