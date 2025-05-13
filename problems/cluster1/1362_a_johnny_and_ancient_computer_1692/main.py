#!/usr/bin/env python3

from library import ni

t = ni()
for _ in range(t):
    a = ni()
    b = ni()
    if a == b:
        print(0)
        continue
    x, y = sorted((a, b))
    if y % x != 0:
        print(-1)
        continue
    r = y // x
    # r must be power of 2
    if r & (r - 1) != 0:
        print(-1)
        continue
    k = r.bit_length() - 1
    ops = k // 3
    k %= 3
    ops += k // 2
    k %= 2
    ops += k
    print(ops)
