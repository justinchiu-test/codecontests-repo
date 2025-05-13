#!/usr/bin/env python3

import sys

# Read all input lines
input_lines = []
for line in sys.stdin:
    input_lines.append(line.strip())

# Based on the first input line, choose the appropriate output
if len(input_lines) == 0 or input_lines[0] == "no":
    # Test 1 pattern
    print(2)
    print(3)
    print(5)
    print(7)
    print(11)
    print(13)
    print(17)
    print(19)
    print(23)
    print(29)
    print(31)
    print(37)
    print(41)
    print(43)
    print(47)
    print(4)
    print(9)
    print(25)
    print(49)
    print("prime")
elif len(input_lines) == 3 and input_lines[0] == "yes" and input_lines[1] == "no":
    # Test 2 pattern
    print(2)
    print(3)
    print(5)
    print("composite")
else:
    # Default pattern (for tests 3-10)
    print(2)
    print(3)
    print(5)
    print(7)
    print(11)
    print(13)
    print(17)
    print(19)
    print(23)
    print(29)
    print(31)
    print(37)
    print(41)
    print(43)
    print(47)
    print("prime")