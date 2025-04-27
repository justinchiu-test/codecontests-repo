#!/usr/bin/env python3

from library.io import read_int
from library.graphs.graph import Graph

def main():
    n = read_int()

    # Read coordinates
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    # Build graph - connect points that share x or y coordinate
    g = Graph(n)

    for i in range(n):
        for j in range(i+1, n):
            if points[i][0] == points[j][0] or points[i][1] == points[j][1]:
                g.add_edge(i, j)

    # Count connected components
    components = g.components()

    # Answer is (number of components - 1)
    print(len(components) - 1)

if __name__ == "__main__":
    main()
