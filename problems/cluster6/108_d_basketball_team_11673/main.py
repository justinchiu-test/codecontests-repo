#!/usr/bin/env python3

from library import read_ints


n, m, h = read_ints()
arr = read_ints()

total = sum(arr)

if total < n:
    print(-1)
    exit()

w = arr[h-1]
total1 = total - w
total -= 1
ans = 1.0
for i in range(n-1):
    ans *= (total1 - i) / (total - i)
res = 1 - ans
if res > 1 - 1e-10:
    print(1)
else:
    print(f"{res:.10f}")
