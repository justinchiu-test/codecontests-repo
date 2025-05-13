#!/usr/bin/env python3

from library import read_int, read_ints, combination

# Read input
n = read_int()
a = read_ints()

# Sort the array to find the minimum product
a.sort()

# Count the occurrences of the three smallest elements
min1 = a[0]  # First minimum
min2 = a[1]  # Second minimum
min3 = a[2]  # Third minimum

# Count frequencies
count_min1 = a.count(min1)
count_min2 = a.count(min2) if min2 != min1 else 0
count_min3 = a.count(min3) if min3 != min2 else 0

# Calculate the answer based on the frequencies
result = 0

if min1 == min2 == min3:
    # All minimums are the same, choose 3 from count_min1
    result = combination(count_min1, 3)
elif min1 == min2 < min3:
    # First and second minimums are the same, choose 2 from count_min1 and 1 from count_min3
    result = combination(count_min1, 2) * count_min3
elif min1 < min2 == min3:
    # Second and third minimums are the same, choose 1 from count_min1 and 2 from count_min2
    result = count_min1 * combination(count_min2, 2)
else:
    # All minimums are different, just multiply their counts
    result = count_min1 * count_min2 * count_min3

print(int(result))