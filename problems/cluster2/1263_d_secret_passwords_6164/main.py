#!/usr/bin/env python3

from library import get_int, DSU

n = get_int()
letter_used = [False] * 26
dsu = DSU(26)

for _ in range(n):
    password = set(input().strip())
    
    first_letter = None
    for letter in password:
        letter_idx = ord(letter) - ord('a')
        letter_used[letter_idx] = True
        
        if first_letter is None:
            first_letter = letter_idx
        else:
            dsu.union(first_letter, letter_idx)

# Count distinct connected components that are used
roots = set()
for i in range(26):
    if letter_used[i]:
        roots.add(dsu.get(i))

print(len(roots))