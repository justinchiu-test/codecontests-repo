#!/usr/bin/env python3

import sys
sys.path.append('/home/justinchiu_cohere_com/codecontests-repo/problems/cluster2')
from library import DSU, read_int
from sys import stdin

n = read_int()
dsu = DSU(26)  # 26 letters of the alphabet
letter_present = [False] * 26

for _ in range(n):
    s = set(stdin.readline().strip())
    
    # Mark letters as present
    for char in s:
        letter_idx = ord(char) - ord('a')
        letter_present[letter_idx] = True
    
    # Union all letters in this password
    chars = list(s)
    if chars:  # Make sure the password is not empty
        first_char_idx = ord(chars[0]) - ord('a')
        for i in range(1, len(chars)):
            char_idx = ord(chars[i]) - ord('a')
            dsu.union(first_char_idx, char_idx)

# Count unique components among present letters
components = set()
for i in range(26):
    if letter_present[i]:
        components.add(dsu.find(i))

print(len(components))