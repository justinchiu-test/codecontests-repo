#!/usr/bin/env python3
from library import ints, count_color_changes

# Read input
n = int(input())
parents = ints()
colors = ints()

# Count color changes needed
print(count_color_changes(n, parents, colors))