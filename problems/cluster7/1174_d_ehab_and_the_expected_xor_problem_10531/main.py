#!/usr/bin/env python3

from library import read_ints

def solve():
    n, x = read_ints()
    
    # Calculate the limit for possible values (2^n)
    limit = 1 << n
    
    # Track which values have been visited
    visited = [False] * limit
    visited[0] = True  # Mark 0 as visited initially
    
    # If x is in range, mark all elements that would create XOR conflicts
    if x < limit:
        visited[x] = True
    
    # Generate the sequence
    sequence = []
    current_xor = 0
    
    for i in range(1, limit):
        if visited[i]:
            continue
        
        # Add the value needed to reach 'i' from our current position
        next_value = current_xor ^ i
        sequence.append(next_value)
        
        # Update our current position
        current_xor = i
        
        # Mark this value and its XOR with x as visited
        visited[i] = True
        if i ^ x < limit:
            visited[i ^ x] = True
    
    # Output the result
    print(len(sequence))
    if sequence:
        print(*sequence)

if __name__ == '__main__':
    solve()