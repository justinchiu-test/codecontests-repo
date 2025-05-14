#!/usr/bin/env python3

from library import rints, xor_sum

n, m = rints()
a = rints()
b = rints()
if xor_sum(a) != xor_sum(b):
    print("NO")
    exit()
print("YES")
one = xor_sum(a[1:]) ^ b[0]
print(one, end = " ")
for i in b[1:]:
    print(i, end=" ")
print()
st = ""
for _ in range(m - 1):
    st += "0 "
for i in a[1:]:
    print(i, end=" ")
    print(st)
