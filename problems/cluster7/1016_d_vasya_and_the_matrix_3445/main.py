#!/usr/bin/env python3

from library import read_int_pair, read_ints, xor_sum, print_yes_no, create_matrix, print_matrix

n, m = read_int_pair()
row_xors = read_ints()
col_xors = read_ints()

if xor_sum(row_xors) != xor_sum(col_xors):
    print_yes_no(False)
    exit()

print("YES")

# Create the matrix
matrix = create_matrix(n, m)

# Fill in the first row
first_element = xor_sum(row_xors[1:]) ^ col_xors[0]
matrix[0][0] = first_element
for j in range(1, m):
    matrix[0][j] = col_xors[j]

# Fill in the remaining rows
for i in range(1, n):
    matrix[i][0] = row_xors[i]

# Print the matrix
print_matrix(matrix)