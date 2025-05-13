#!/usr/bin/env python3

from library import read_int, read_points, is_supercentral

def main():
    n = read_int()
    pts = read_points(n)
    # count supercentral points
    ans = sum(1 for p in pts if is_supercentral(p, pts))
    print(ans)

if __name__ == "__main__":
    main()
