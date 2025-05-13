#!/usr/bin/env python3

from library import read_int, read_n_points, Line, Point, print_answer
from itertools import combinations

def solve():
    n = read_int()
    points = read_n_points(n)
    
    # Store lines by their direction (slope)
    lines_by_direction = {}
    
    # Generate all possible lines through pairs of points
    for p1, p2 in combinations(points, 2):
        if p1 != p2:  # Ensure we have distinct points
            line = Line.from_points(p1, p2)
            
            # Normalize the slope for consistent comparison
            if line.b == 0:  # Vertical line
                slope = (0, 1)  # Represent vertical line with (0, 1)
                intercept = -line.c / line.a  # x-intercept
            else:
                # Use the normalized form: y = mx + b
                slope = (1, -line.a / line.b)  # (1, m) where m is the slope
                intercept = -line.c / line.b  # y-intercept
            
            if slope not in lines_by_direction:
                lines_by_direction[slope] = set()
            
            lines_by_direction[slope].add(intercept)
    
    # Count the total number of unique lines
    total_lines = sum(len(intercepts) for intercepts in lines_by_direction.values())
    
    # Calculate the number of intersection points
    result = 0
    for direction, intercepts in lines_by_direction.items():
        # Lines with the same direction do not intersect with each other
        # Lines with different directions intersect exactly once (unless they are the same line)
        lines_with_other_directions = total_lines - len(intercepts)
        result += len(intercepts) * lines_with_other_directions
    
    # Divide by 2 as each intersection is counted twice
    print_answer(result // 2)

if __name__ == "__main__":
    solve()