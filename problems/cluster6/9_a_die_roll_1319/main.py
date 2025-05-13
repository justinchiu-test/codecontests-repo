#!/usr/bin/env python3

from library import simplify_fraction, read_ints

# Read input
y, w = read_ints()
max_points = max(y, w)

# Calculate favorable outcomes: points greater than or equal to max_points
favorable_outcomes = 6 - max_points + 1
total_outcomes = 6

# Simplify the fraction
numerator, denominator = simplify_fraction(favorable_outcomes, total_outcomes)
print(f"{numerator}/{denominator}")