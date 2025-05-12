#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import read_test_cases, read_int, operations_to_multiply_2_divide_6

for _ in range(read_test_cases()):
    n = read_int()
    print(operations_to_multiply_2_divide_6(n))
