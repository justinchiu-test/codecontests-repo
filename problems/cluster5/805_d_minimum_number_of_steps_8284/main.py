#!/usr/bin/env python3

from library import read_str

def main():
    # Constants
    MOD = 1000000007
    
    # Read input
    s = read_str()
    
    # Count to track the number of 'a's encountered so far
    # This counts the number of ways to replace "ab" substrings
    a_count = 0
    
    # Total number of steps needed
    total_steps = 0
    
    # Process each character in the string
    for char in s:
        if char == 'a':
            # When we see an 'a', we double the potential replacements 
            # (each previous 'a' can now potentially form an "ab" with a future 'b')
            a_count = (a_count * 2) % MOD
            # Add this new 'a' to the count
            a_count = (a_count + 1) % MOD
        elif char == 'b':
            # When we see a 'b', we can replace each previously counted 'a' with "ab"
            # This adds to our total steps
            total_steps = (total_steps + a_count) % MOD
    
    # Print the result
    print(total_steps)

if __name__ == "__main__":
    main()