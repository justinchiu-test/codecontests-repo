#!/usr/bin/env python3
import sys
import os

# Add the parent directory to the path so we can import the library
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import read_int_tuple

u, v = read_int_tuple()

if u > v or (v - u) % 2 != 0:
    print(-1)
elif u == 0 and v == 0:
    print(0)
elif u == v:
    print(f"1 {u}")
else:
    # We try to construct 2 numbers first
    x = (v - u) // 2
    a, b = u ^ x, x
    
    if a + b == v and a ^ b == u:
        print(f"2 {a} {b}")
    else:
        # Try with 3 numbers
        a, b, c = u, (v - u) // 2, (v - u) // 2
        if a + b + c == v and a ^ b ^ c == u:
            print(f"3 {a} {b} {c}")
        else:
            print(-1)