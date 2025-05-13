#!/usr/bin/env python3

from library import read_ints

# Read input
n, sx, sy = read_ints()
students = [read_ints() for _ in range(n)]

# Count students in each quadrant relative to the school
left_up = 0    # x < sx, y > sy
left_down = 0  # x < sx, y < sy
right_up = 0   # x > sx, y > sy
right_down = 0 # x > sx, y < sy
up = 0         # x = sx, y > sy
down = 0       # x = sx, y < sy
left = 0       # x < sx, y = sy
right = 0      # x > sx, y = sy

for x, y in students:
    if x < sx and y < sy:
        left_down += 1
    elif x < sx and y > sy:
        left_up += 1
    elif x == sx and y != sy:
        if y > sy:
            up += 1
        else:
            down += 1
    elif x > sx and y < sy:
        right_down += 1
    elif x > sx and y > sy:
        right_up += 1
    elif x != sx and y == sy:
        if x < sx:
            left += 1
        else:
            right += 1

# Calculate students that would visit the tent at each possible location
counts = [
    left_up + right_up + up,     # Above the school
    left_up + left_down + left,  # Left of the school
    right_up + right_down + right, # Right of the school
    left_down + right_down + down  # Below the school
]

# Find the best position
max_count = max(counts)
best_position = counts.index(max_count)

# Output the results
print(max_count)
if best_position == 0:
    print(sx, sy + 1)
elif best_position == 1:
    print(sx - 1, sy)
elif best_position == 2:
    print(sx + 1, sy)
else:
    print(sx, sy - 1)