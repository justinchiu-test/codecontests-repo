#!/usr/bin/env python3

from library import DSU
from sys import stdin

inp = lambda: stdin.readline().strip()

n = int(inp())

# Create a DSU with 26 characters (a-z)
dsu = DSU(26)

# Track which characters are actually present in the input
present = [False] * 26

# Process each string
for _ in range(n):
    # Get unique characters in the string
    chars = set(inp())
    
    # Mark these characters as present
    for c in chars:
        present[ord(c) - ord('a')] = True
    
    # Union all characters in this string to connect them
    # Each union operation merges the sets containing two character ids
    if len(chars) > 1:
        first_char = ord(list(chars)[0]) - ord('a')
        for c in list(chars)[1:]:
            dsu.union(first_char, ord(c) - ord('a'))

# Count the number of unique connected components that contain present characters
password_count = 0
counted = set()

for i in range(26):
    if present[i]:
        # Get the representative for this character's set
        rep = dsu.find(i)
        
        # If we haven't counted this representative yet, count it
        if rep not in counted:
            password_count += 1
            counted.add(rep)

print(password_count)