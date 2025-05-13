#!/usr/bin/env python3

from collections import Counter

n, m = map(int, input().split())

# If there's only one pair, we can always choose the numbers in it as x and y
if m == 1:
    print("YES")
    exit(0)

# Read pairs and store them as tuples
pairs = []
for _ in range(m):
    a, b = map(int, input().split())
    pairs.append((a, b))

# If all pairs are the same, the answer is trivially YES
if all(pair == pairs[0] for pair in pairs):
    print("YES")
    exit(0)

# Try to choose one of the numbers from the first pair as x
# Then find a potential y that covers the remaining pairs
for x in pairs[0]:
    # Count occurrences of each number in pairs not covered by x
    remaining_numbers = []
    for a, b in pairs:
        if a != x and b != x:
            remaining_numbers.extend([a, b])
    
    # If there are no remaining pairs, any other number can be y
    if not remaining_numbers:
        print("YES")
        exit(0)
    
    # Count occurrences of each number
    counter = Counter(remaining_numbers)
    
    # Find the most frequent number
    most_common = counter.most_common(1)[0]
    potential_y, count = most_common
    
    # Check if the potential y covers all remaining pairs
    covers_all = True
    for a, b in pairs:
        if a != x and b != x and a != potential_y and b != potential_y:
            covers_all = False
            break
    
    if covers_all:
        print("YES")
        exit(0)

print("NO")