#!/usr/bin/env python3

from collections import deque
from library.io import read_int_tuple

def main():
    x0, y0, x1, y1 = read_int_tuple()
    n = int(input())

    # Read allowed cells
    allowed = {}
    for _ in range(n):
        r, a, b = map(int, input().split())
        for j in range(a, b+1):
            allowed[(r, j)] = True

    # BFS to find shortest path
    visited = {}
    q = deque([(x0, y0)])
    visited[(x0, y0)] = 0

    # All 8 adjacent directions for the king
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),  # Vertical and horizontal
        (-1, -1), (-1, 1), (1, 1), (1, -1)  # Diagonal
    ]

    result = -1
    while q:
        x, y = q.popleft()
        distance = visited[(x, y)]

        # Check if destination reached
        if x == x1 and y == y1:
            result = distance
            break

        # Try all 8 directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Check if the new position is allowed and not visited
            if (nx, ny) in allowed and (nx, ny) not in visited:
                q.append((nx, ny))
                visited[(nx, ny)] = distance + 1

    print(result)

if __name__ == "__main__":
    main()
