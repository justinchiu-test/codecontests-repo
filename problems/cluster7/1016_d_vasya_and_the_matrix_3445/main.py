#!/usr/bin/env python3
from library import nl, xor_list

n, m = nl(2)
a = nl(n)
b = nl(m)
if xor_list(a) != xor_list(b):
    print("NO")
    exit()
print("YES")
one = xor_list(a[1:]) ^ b[0]
print(one, *b[1:])
for ai in a[1:]:
    print(ai, *([0] * (m-1)))
