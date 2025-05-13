#!/usr/bin/env python3

from library import DSU

n = int(input().strip())

# We use the DSU to track connected components of letters
# Each letter is represented by its position in the alphabet (0-25)
dsu = DSU(26)
letter_exists = [False] * 26

for _ in range(n):
    s = set(input().strip())
    
    # Mark all letters in the password as existing
    letter_indices = [ord(ch) - ord('a') for ch in s]
    for idx in letter_indices:
        letter_exists[idx] = True
    
    # Union all letters in the same password
    for i in range(len(letter_indices) - 1):
        dsu.union(letter_indices[i], letter_indices[i + 1])

# Count the number of distinct components among letters that exist
roots = set()
for i in range(26):
    if letter_exists[i]:
        roots.add(dsu.find(i))

print(len(roots))