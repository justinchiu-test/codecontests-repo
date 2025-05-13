#!/usr/bin/env python3

from library import get_ints, gcd

n, m = get_ints()
a = get_ints()

def process_divisor(x):
    global answer
    if x % 2 == 0:
        return
    for i in range(30):
        v = 2 ** i * x
        if v > m:
            break
        answer += m - v

# Find gcd of (a_i - 1) for all i
g = 0
for x in a:
    g = gcd(g, x - 1)

answer = 0
for i in range(1, int(g**0.5) + 1):
    if g % i == 0:
        process_divisor(i)
        if i * i != g:
            process_divisor(g // i)

print(answer)