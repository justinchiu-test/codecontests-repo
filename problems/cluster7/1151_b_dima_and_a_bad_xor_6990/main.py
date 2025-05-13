#!/usr/bin/env python3

from library import fast_ints, fast_int_grid, tak, nie, print_list, xor_list

n, m = fast_ints()
a = fast_int_grid(n)

# Check if taking first element from each row gives non-zero XOR
first_column = [row[0] for row in a]
if xor_list(first_column) != 0:
    tak()
    print_list(['1'] * n)
    exit(0)

# Look for a row where we can use a different element to get non-zero XOR
for i in range(n):
    for j in range(1, m):
        if a[i][j] != a[i][0]:
            # Found a different element, use it
            tak()
            result = ['1'] * n
            result[i] = str(j + 1)
            print_list(result)
            exit(0)

# No solution found
nie()