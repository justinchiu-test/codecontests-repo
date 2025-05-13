#!/usr/bin/env python3

from library import read_ints, frac_str

x, y = read_ints()
print(frac_str(7 - max(x, y), 6))
