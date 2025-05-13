#!/usr/bin/env python3

from library import fast_ints, fast_int_list, xor_list, yes, no, create_matrix, print_matrix

n, m = fast_ints()
a = fast_int_list()
b = fast_int_list()

# Check if xor sum of rows equals xor sum of columns
if xor_list(a) != xor_list(b):
    no()
    exit(0)

yes()

# Create the matrix
matrix = create_matrix(n, m)

# Fill the first row with column XOR values
matrix[0] = b.copy()

# Calculate the top-left element
matrix[0][0] = xor_list(a[1:]) ^ b[0]

# Fill the remaining rows with zeros except the first column
for i in range(1, n):
    matrix[i][0] = a[i]

# Print the matrix
print_matrix(matrix)