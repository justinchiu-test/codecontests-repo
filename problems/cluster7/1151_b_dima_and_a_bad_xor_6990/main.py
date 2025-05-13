#!/usr/bin/env python3
import sys
import os

# Add the parent directory to the path so we can import the library
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import read_int_tuple, read_2d_array, xor_list

n, m = read_int_tuple()
a = read_2d_array(n)

# Check if first column XOR is non-zero
first_col = [row[0] for row in a]
if xor_list(first_col) != 0:
    print("TAK")
    print(' '.join('1' for _ in range(n)))
else:
    # Try to find a row where another element differs from the first element
    for i in range(n):
        for j in range(1, m):
            if a[i][j] != a[i][0]:
                print('TAK')
                result = ['1'] * n
                result[i] = str(j + 1)
                print(' '.join(result))
                exit(0)
    print('NIE')
