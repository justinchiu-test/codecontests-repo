#!/usr/bin/env python3
import sys
import os

# Add the parent directory to the path so we can import the library
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import read_int_tuple, read_ints, xor_list

n, m = read_int_tuple()
a = read_ints()
b = read_ints()

if xor_list(a) != xor_list(b):
    print("NO")
    quit()

print("YES")
one = xor_list(a[1:]) ^ b[0]
print(one, end=" ")
for i in b[1:]:
    print(i, end=" ")
print()

st = "0 " * (m - 1)
for i in a[1:]:
    print(i, end=" ")
    print(st)
