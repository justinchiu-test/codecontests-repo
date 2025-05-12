#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import read_int, count_operations_to_one

n = read_int()
print(count_operations_to_one(n))
