#!/usr/bin/env python3

from library import read_ints, simplify_fraction

x, y = read_ints()
num, den = simplify_fraction(7 - max(x, y), 6)
print(f"{num}/{den}")
