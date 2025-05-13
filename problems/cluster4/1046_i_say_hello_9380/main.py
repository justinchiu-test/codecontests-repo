#!/usr/bin/env python3

from library import read_int, read_ints, Vector, dist_point_segment_sq

def main():
    N = read_int()
    d1, d2 = read_ints()
    ABs = []
    for _ in range(N):
        Ax, Ay, Bx, By = read_ints()
        # vector from A to B
        ABs.append(Vector.from_points((Ax, Ay), (Bx, By)))
    origin = Vector(0, 0)
    d1sq = d1 * d1
    d2sq = d2 * d2
    reset = True
    count = 0
    for ab1, ab2 in zip(ABs, ABs[1:]):
        if reset and dist_point_segment_sq(origin, ab1, ab2) <= d1sq:
            count += 1
            reset = False
        if ab2.norm_sq() > d2sq:
            reset = True
    print(count)

if __name__ == "__main__":
    main()
