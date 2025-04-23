#!/usr/bin/env python3

import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
n, k = map(int, input().split())
a, b, c, d = map(int, input().split())
if k < n + 1 or n == 4:
    print("-1")
    exit(0)
l = [_ for _ in range(1, n + 1)]
l.remove(a)
l.remove(b)
l.remove(c)
l.remove(d)
print(a, end = ' ')
print(c, end = ' ')
for x in l:
    print(x, end = ' ')
print(d, end = ' ')
print(b, end = ' ')
print("")
print(c, end = ' ')
print(a, end = ' ')
for x in l:
    print(x, end = ' ')
print(b, end = ' ')
print(d, end = ' ')
