#!/usr/bin/env python3

from library import Point, read_int, read_n_points, are_collinear, print_answer

def solve():
    n = read_int()
    points = read_n_points(n)
    
    # Handle cases with fewer than 3 points
    if n < 3:
        print_answer(0)
    else:
        # Count triangles with non-zero area
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    # Check if the three points form a triangle with non-zero area
                    if not are_collinear(points[i], points[j], points[k]):
                        count += 1
        
        print_answer(count)

if __name__ == "__main__":
    solve()