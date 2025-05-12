#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import read_test_cases, read_int, find_x_for_2k_minus_1_divides_n

for _ in range(read_test_cases()):
    n = read_int()
    print(find_x_for_2k_minus_1_divides_n(n))
