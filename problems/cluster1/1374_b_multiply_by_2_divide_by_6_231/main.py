#!/usr/bin/env python3

from library import ni

t = ni()
for _ in range(t):
    n = ni()
    if n == 1:
        print(0)
        continue
    if n % 3 != 0:
        print(-1)
        continue
    cnt3 = 0
    while n % 3 == 0:
        n //= 3
        cnt3 += 1
    cnt2 = 0
    while n % 2 == 0:
        n //= 2
        cnt2 += 1
    if n != 1 or cnt2 > cnt3:
        print(-1)
    else:
        print(2 * cnt3 - cnt2)
