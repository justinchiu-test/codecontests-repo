#!/usr/bin/env python3

from library import setup_io, get_int, get_ints, DSU

input = setup_io()

t = get_int()
for _ in range(t):
    n = get_int()
    p = get_ints()
    dsu = DSU(n)
    for i, x in enumerate(p):
        dsu.union(i, x - 1)
    print(*[dsu.get_size(i) for i in range(n)])