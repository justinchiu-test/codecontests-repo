#!/usr/bin/env python3

# Explicitly construct the path to import library.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import int_tuple_input, unique_slopes

n, x0, y0 = int_tuple_input()
points = []

for _ in range(n):
    points.append(int_tuple_input())

print(unique_slopes(points, (x0, y0)))