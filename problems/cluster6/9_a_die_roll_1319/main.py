#!/usr/bin/env python3

from library import simplify_fraction, read_int_tuple

y, w = read_int_tuple()
max_val = max(y, w)
# The number of favorable outcomes is (7 - max_val) out of 6 total outcomes
numerator = 7 - max_val
denominator = 6

print(simplify_fraction(numerator, denominator))