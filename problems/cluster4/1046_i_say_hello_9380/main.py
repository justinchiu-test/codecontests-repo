#!/usr/bin/env python3

"""
Count how many adjacent segment pairs come within a distance threshold.
"""
from library import getint, getints, Vector

def min_distance_less_than_d1(a, b, d1):
    """Check if minimum distance between segment endpoints a->b is <= d1."""
    L = b - a
    proj1 = a.dot(L)
    proj2 = b.dot(L)
    if proj1 * proj2 < 0:
        return a.cross(L)**2 <= d1**2 * L.norm2()
    return min(a.norm2(), b.norm2()) <= d1**2


def main():
    N = getint()
    d1, d2 = getints()
    ABs = []
    for _ in range(N):
        Ax, Ay, Bx, By = getints()
        ABs.append(Vector(Bx, By) - Vector(Ax, Ay))

    count = 0
    active = True
    for u, v in zip(ABs, ABs[1:]):
        if active and min_distance_less_than_d1(u, v, d1):
            count += 1
            active = False
        active = active or (v.norm2() > d2**2)
    print(count)

if __name__ == "__main__":
    main()
