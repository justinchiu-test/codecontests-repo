#!/usr/bin/env python3

from library import read_str, Combinatorics, MOD

# Initialize combinatorics with precomputed factorials
combinatorics = Combinatorics(200200)

s = read_str()
open_count = 0
close_count = s.count(')')
answer = 0

# For each opening bracket, calculate the number of ways to form subsequences
for char in s:
    if char == '(':
        open_count += 1
        # Calculate C(open_count + close_count - 1, open_count)
        answer = (answer + combinatorics.combination(open_count + close_count - 1, open_count)) % MOD
    else:
        close_count -= 1

print(answer % MOD)