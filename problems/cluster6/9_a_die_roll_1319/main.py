#!/usr/bin/env python3

# Import library using the helper function
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import read_ints, fraction_to_str

x, y = read_ints()
z = 7 - max(x, y)
print(fraction_to_str(z, 6))