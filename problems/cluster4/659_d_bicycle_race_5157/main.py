#!/usr/bin/env python3

from library import read_int, read_n_points, Point, cross_product, print_answer

def solve():
    n = read_int()
    # We need n+1 points for a closed polygon with n segments
    points = read_n_points(n+1)
    
    # Count the number of right turns (dangerous positions)
    dangerous_count = 0
    for i in range(2, n):
        # Create vectors for consecutive segments
        v1 = (points[i].x - points[i-1].x, points[i].y - points[i-1].y)
        v2 = (points[i-1].x - points[i-2].x, points[i-1].y - points[i-2].y)
        
        # If cross product is negative, it's a right turn
        if cross_product(v1, v2) < 0:
            dangerous_count += 1
    
    print_answer(dangerous_count)

if __name__ == "__main__":
    solve()