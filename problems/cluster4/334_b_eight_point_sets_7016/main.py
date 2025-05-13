#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library import points_input

# Read 8 points
points = points_input(8)

# Sort points by their coordinates
points.sort()

# Check if the structure is "respectable"
# A respectable arrangement is 3 columns of points
# with column 1 and 3 having 3 points each, and column 2 having 2 points
# And 3 rows with row 1 and 3 having 3 points each, and row 2 having 2 points
try:
    # Check column structure
    if not (points[0][0] == points[1][0] == points[2][0] and      # First column has 3 points
            points[3][0] == points[4][0] and                      # Second column has 2 points
            points[5][0] == points[6][0] == points[7][0] and      # Third column has 3 points
            points[0][0] != points[3][0] and                      # Different columns
            points[3][0] != points[5][0] and
            points[0][0] != points[5][0]):
        raise ValueError("Invalid column structure")
    
    # Extract y-coordinates in each column
    col1_y = sorted([points[0][1], points[1][1], points[2][1]])
    col2_y = sorted([points[3][1], points[4][1]])
    col3_y = sorted([points[5][1], points[6][1], points[7][1]])
    
    # Check row structure by comparing y-coordinates
    if not (col1_y[0] == col2_y[0] == col3_y[0] and              # First row has 3 points
            col1_y[1] == col3_y[1] and                           # Second row has 2 points
            col1_y[2] == col2_y[1] == col3_y[2] and              # Third row has 3 points
            col1_y[0] != col1_y[1] and                           # Different rows
            col1_y[1] != col1_y[2] and
            col1_y[0] != col1_y[2]):
        raise ValueError("Invalid row structure")
    
    print("respectable")
except ValueError:
    print("ugly")