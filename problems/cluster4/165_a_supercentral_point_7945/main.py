#!/usr/bin/env python3

#!/usr/bin/env python3
"""
Count supercentral points with neighbors in all four cardinal directions.
"""
from library import read_int, read_points

def main():
    n = read_int()
    pts = read_points(n)
    cnt = 0
    for p in pts:
        x, y = p.real, p.imag
        left = any(q.real < x and q.imag == y for q in pts)
        right = any(q.real > x and q.imag == y for q in pts)
        up = any(q.imag > y and q.real == x for q in pts)
        down = any(q.imag < y and q.real == x for q in pts)
        if left and right and up and down:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
