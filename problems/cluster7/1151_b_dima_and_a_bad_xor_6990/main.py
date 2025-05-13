#!/usr/bin/env python3

from library import read_int_pair, read_int_matrix, print_answer, xor_sum, print_array

n, m = read_int_pair()
matrix = read_int_matrix(n)

# Check if selecting the first column gives non-zero XOR
first_col_values = [row[0] for row in matrix]
first_col_xor = xor_sum(first_col_values)

if first_col_xor != 0:
    print_answer(True, "TAK", "NIE")
    print_array(['1'] * n)
    exit()

# If first column XOR is zero, try to find a different element in any row
for i in range(n):
    for j in range(1, m):
        if matrix[i][j] != matrix[i][0]:
            print_answer(True, "TAK", "NIE")

            # Build the selection: 1 for all rows except the current one
            selection = ['1'] * n
            selection[i] = str(j + 1)  # 1-indexed

            print_array(selection)
            exit()

# If all rows have identical elements, XOR will always be zero
print_answer(False, "TAK", "NIE")