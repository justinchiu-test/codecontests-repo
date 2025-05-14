#!/usr/bin/env python3

"""
Count close consecutive segments under distance threshold.
"""
from library import read_int, read_ints
from library import segment_point_dist2, norm2

def main():
    n = read_int()
    d1, d2 = read_ints()
    segs = []
    for _ in range(n):
        x1, y1, x2, y2 = read_ints()
        # represent segment as vector endpoint from origin
        segs.append(complex(x2 - x1, y2 - y1))
    origin = 0+0j
    cnt = 0
    reset = True
    for a, b in zip(segs, segs[1:]):
        # check if trajectory segment [a,b] enters circle of radius d1
        if reset and segment_point_dist2(a, b, origin) <= d1 * d1:
            cnt += 1
            reset = False
        # reset when outside larger circle at endpoint
        reset = reset or (norm2(b) > d2 * d2)
    print(cnt)

if __name__ == '__main__':
    main()
