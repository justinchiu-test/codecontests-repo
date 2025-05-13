#!/usr/bin/env python3

from library import read_int_pair, print_array

n, x = read_int_pair()
limit = 1 << n

# Keep track of prefixes we've seen (and their XOR with x)
seen = {}
seen[0] = True
if x < limit:
    seen[x] = True

answer = []
current_xor = 0

# Try all possible values up to 2^n
for i in range(1, limit):
    if i in seen:
        continue

    # Add this value to the sequence
    value = current_xor ^ i
    answer.append(value)
    current_xor = i

    # Mark this prefix and its XOR with x as seen
    seen[i] = True
    if i ^ x < limit:
        seen[i ^ x] = True

# Output the result
print(len(answer))
if answer:
    print_array(answer)