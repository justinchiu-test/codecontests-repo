#!/usr/bin/env python3

import sys
import os

# Add parent directory to path to import library
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import read_ints

w, b = read_ints()
p = [[0] * (b + 1) for _ in range(w + 1)]
for i in range(1, w + 1):
    p[i][0] = 1

for i in range(1, w + 1):
    for j in range(1, b + 1):
        p[i][j] = i / (i + j)
        if j >= 3:
            p[i][j] += (j / (i + j)) * ((j - 1) / (i + j - 1)) * ((j - 2) / (i + j - 2)) * p[i][j - 3]
        if j >= 2:
            p[i][j] += (j / (i + j)) * ((j - 1) / (i + j - 1)) * ((i) / (i + j - 2)) * p[i - 1][j - 2]

print("%.9f" % p[w][b])