#!/usr/bin/env python3

from library import read_int, meaningless_operations

q = read_int()
for _ in range(q):
    a = read_int()
    print(meaningless_operations(a))