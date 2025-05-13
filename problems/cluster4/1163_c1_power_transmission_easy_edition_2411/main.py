#!/usr/bin/env python3

from library import read_int, read_n_points, Line, Point, print_answer

def solve():
    n = read_int()
    points = read_n_points(n)
    
    # Store unique lines
    unique_lines = set()
    
    # Generate all possible lines through pairs of points
    for i in range(n):
        for j in range(i + 1, n):
            if points[i] != points[j]:  # Ensure we have distinct points
                line = Line.from_points(points[i], points[j])
                unique_lines.add(line)
    
    # Group lines by their slope (direction)
    slope_groups = {}
    for line in unique_lines:
        # Normalize the slope for consistent comparison
        if line.b == 0:  # Vertical line
            slope = float('inf')
        else:
            slope = -line.a / line.b  # Slope is -a/b from ax + by + c = 0
        
        if slope not in slope_groups:
            slope_groups[slope] = []
        slope_groups[slope].append(line)
    
    result = 0
    slope_counts = [len(group) for group in slope_groups.values()]
    
    # Calculate the number of intersection points
    for i in range(len(slope_counts)):
        # Every line in this slope group intersects with every line in other groups
        # Sum total = slope_count[i] * (total_lines - slope_count[i])
        result += slope_counts[i] * (sum(slope_counts) - slope_counts[i])
    
    # Divide by 2 as each intersection is counted twice
    print_answer(result // 2)

if __name__ == "__main__":
    solve()