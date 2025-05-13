#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import int_input, ints_input, supercentral_point

n = int_input()
points = [ints_input() for _ in range(n)]

print(supercentral_point(points))