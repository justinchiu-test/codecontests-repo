#!/usr/bin/env python3

from library import fast_ints, yes, xor_list

n, x = fast_ints()

if n == 2 and x == 0:
    print("NO")
    exit(0)

yes()

if n == 1:
    print(x)
    exit(0)

if n == 2:
    print(f"{x} 0")
    exit(0)

a = 2**17  # 131072
b = 2**18  # 262144
ans = 0

# Print first n-3 numbers
for i in range(n-3):
    print(i+1, end=" ")
    ans ^= (i+1)

# Handle the last 3 numbers
if ans == x:
    print(a, b, a+b)
else:
    print(0, a, a ^ ans ^ x)