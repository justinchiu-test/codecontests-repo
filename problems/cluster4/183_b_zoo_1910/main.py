#!/usr/bin/env python3

from library import Point, gcd

def normalize_rational(num, den):
    """Normalize a rational number to its simplest form."""
    # Handle negative numbers
    if (num < 0) != (den < 0):  # One is negative but not both
        num = abs(num)
        den = -abs(den)
    else:
        num = abs(num)
        den = abs(den)
    
    # Put it in simplest form
    g = gcd(abs(num), abs(den))
    num //= g
    den //= g
    
    return (num, den)

# Read input
n, m = map(int, input().split())
flamingos = []

for _ in range(m):
    x, y = map(int, input().split())
    flamingos.append(Point(x, y))

# Initialize maximum hits for each binocular (1-indexed)
maxhits = [1] * (n + 1)
maxhits[0] = 0  # Ignore index 0

# Find lines passing through each pair of flamingos
line_to_points = {}
for i in range(m):
    for j in range(i + 1, m):  # Only need to check each pair once
        p1, p2 = flamingos[i], flamingos[j]
        
        # Calculate line parameters
        dy = p2.y - p1.y
        dx = p2.x - p1.x
        
        if dy == 0:  # Horizontal line, no intercept with x-axis
            continue
        
        # Calculate slope and x-intercept
        slope = normalize_rational(dy, dx)
        c_prime = p1.y * dx - p1.x * dy
        x_intercept = -c_prime / dy
        
        line = (slope, x_intercept)
        
        # Check if this line passes through a binocular
        if int(x_intercept) == x_intercept and 1 <= x_intercept <= n:
            if line in line_to_points:
                # Add these flamingos to the existing line
                points = line_to_points[line]
                points.add(i)
                points.add(j)
            else:
                # Create new line with these flamingos
                points = {i, j}
                line_to_points[line] = points

# Update maxhits for each binocular
for line, points in line_to_points.items():
    x_intercept = int(line[1])
    maxhits[x_intercept] = max(maxhits[x_intercept], len(points))

# Sum up the maximum hits for all binoculars
total_hits = sum(maxhits)
print(total_hits)