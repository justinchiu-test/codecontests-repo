#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import read_int, lcm_quotient_count

b = read_int()
print(lcm_quotient_count(b))