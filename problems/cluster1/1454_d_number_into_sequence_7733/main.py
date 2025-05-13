#!/usr/bin/env python3

from library import read_int, number_into_sequence

t = read_int()
for _ in range(t):
    n = read_int()
    count, sequence = number_into_sequence(n)
    print(count)
    print(*sequence)
