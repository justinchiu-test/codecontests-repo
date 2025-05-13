#!/usr/bin/env python3
from library import *

def main():
    n, m = read_ints()
    a = read_ints()
    b = read_ints()
    if xor_list(a) != xor_list(b):
        print("NO")
        return
    print("YES")
    # first line: one and rest of b
    one = xor_list(a[1:]) ^ b[0]
    print(one, *b[1:])
    # next m-1 lines: each a[i] and zeros
    # line suffix of zeros without trailing space
    if m > 1:
        st = " ".join(["0"] * (m - 1))
    else:
        st = ""
    for x in a[1:]:
        if st:
            print(x, st)
        else:
            print(x)

if __name__ == '__main__':
    main()
