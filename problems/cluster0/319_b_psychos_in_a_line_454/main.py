#!/usr/bin/env python3

import sys
sys.path.append('/home/justinchiu_cohere_com/codecontests-repo/problems/cluster0')
from library import read_int, read_ints

# Read input
n = read_int()
t = read_ints()

# Initialize arrays
p = [0] * n  # predecessor array
s = [0] * n  # steps array
r = t[0]     # max value seen so far

# Process the array
for i in range(n - 1):
    j = i + 1
    x = t[j]
    
    if x > r:
        # If current value is greater than max seen so far, update max
        r = x
    else:
        # Process sequence of "kills"
        # This loop simulates the removal of elements
        while t[i] < x:
            # Update steps needed for j and move to predecessor of i
            s[j] = max(s[j], s[i])
            i = p[i]
        
        # Set i as predecessor of j
        p[j] = i
        
        # Increment steps needed for j
        s[j] += 1

# Output the maximum number of steps
print(max(s))