# Geometry Library Plan for Cluster 4

Based on the problem tags and the code examined, this cluster is heavily focused on geometry problems. We'll build a geometry library with reusable components for common geometric operations and algorithms.

## Library Structure

### 1. Basic Geometry Components
- **Point/Vector class**: 2D point representation with vector operations
  - Vector arithmetic (add, subtract, multiply by scalar)
  - Dot and cross products
  - Normalization and distance calculations
  - Angle calculations
- **Line class**: Line representation and operations
  - Creation from points, point-slope
  - Intersection detection
  - Distance calculations
- **Segment class**: Line segment with operations
  - Length calculations
  - Point-on-segment detection
  - Intersection detection
- **Polygon class**: Polygon representation with common operations
  - Area and perimeter calculations
  - Convexity testing
  - Point containment testing

### 2. Common Geometric Algorithms
- **Convex Hull algorithms**: Graham scan
- **Line intersection**: Detecting and finding intersection points
- **Collinearity tests**: Checking if points are on the same line
- **Orientation tests**: Clockwise/counterclockwise/collinear
- **Unique slopes calculation**: For problems like laser gun detection
- **Parallelogram vertex calculation**: Given 3 points

### 3. Input/Output Utilities
- Functions to parse geometric inputs (points)
- Rational number handling for exact calculations

## Problem Checklist

As we refactor each problem, we'll check it off here:

- [x] 1046_i_say_hello_9380
- [x] 1163_c1_power_transmission_easy_edition_2411
- [x] 1163_c2_power_transmission_hard_edition_12093
- [x] 1271_c_shawarma_tent_643
- [x] 135_b_rectangle_and_square_9812
- [x] 136_d_rectangle_and_square_9500
- [ ] 13_b_letter_a_6066
- [ ] 1468_f_full_turn_7213
- [x] 165_a_supercentral_point_7945
- [x] 183_b_zoo_1910
- [ ] 2_c_commentator_problem_4414
- [ ] 32_e_hideandseek_3373
- [x] 334_b_eight_point_sets_7016
- [ ] 407_a_triangle_11184
- [ ] 464_b_restore_cube__2130
- [ ] 498_a_crazy_town_4318
- [ ] 499_c_crazy_town_6399
- [x] 514_b_han_solo_and_lazer_gun_9314
- [x] 552_d_vanya_and_triangles_5048
- [ ] 598_f_cut_length_4738
- [x] 617_d_polyline_7236
- [ ] 618_c_constellation_3489
- [ ] 630_o_arrow_1929
- [x] 659_d_bicycle_race_5157
- [x] 749_b_parallelogram_is_back_2975
- [ ] 850_a_five_dimensional_points_3812
- [ ] 886_f_symmetric_projections_6728
- [ ] 889_d_symmetric_projections_6832
- [ ] 934_e_a_colourful_prospect_3399
- [x] 961_d_pair_of_lines_12769

## Implementation Strategy

1. First, continue developing the core geometric classes and functions in library.py
2. Add utility functions for common calculations
3. Refactor problems one by one, starting with simpler ones
4. For each problem:
   - Understand the original solution
   - Identify which library components to use
   - Rewrite using the library components
   - Test to ensure it still passes
5. As we work through problems, enhance the library as needed

## Progress Update

We've successfully refactored 12 problems, focusing on:

1. **Point operations**: Vector geometry with dot/cross products and collinearity tests
2. **Line representation**: Rational/normalized line representation and intersection calculations
3. **Shape detection**: Square and rectangle validation
4. **Utility functions**: Reading points from input, checking relative positions

Our library now includes:
- A robust `Point` class with vector operations
- `Line` and `Segment` classes for representing lines and segments
- A `Polygon` class for polygon operations
- Utility functions for common geometric operations
- Input/output helpers for parsing geometric data

The completed problems include:
- Power transmission line intersection counting
- Checking if points form squares/rectangles
- Finding minimum polylines through points
- Eight-point grid pattern detection
- Pair of lines placement testing
- Unique slopes calculation for laser gun problems

## Refactored Problem Types

### Power Transmission (1163_c1 & 1163_c2)
- Implemented line representation and counting unique line-line intersections

### Shawarma Tent (1271_c)
- Used point comparison and quadrant checking

### Rectangle and Square (135_b & 136_d)
- Added polygon detection, square detection, rectangle detection functions

### Polyline (617_d)
- Used point collinearity testing to determine minimum segment count

### Eight Point Sets (334_b)
- Implemented grid pattern detection

### Pair of Lines (961_d)
- Added functions to check if points can be placed on two lines using collinearity

We'll continue refactoring the remaining problems, with a focus on maximizing code reuse and minimizing total code size.