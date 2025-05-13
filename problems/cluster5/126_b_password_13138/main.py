#!/usr/bin/env python3

from library import z_function, read_str

def main():
    s = read_str()
    n = len(s)
    
    # Calculate Z-function for the string
    Z = z_function(s)
    
    # Find valid suffixes that are also prefixes
    third = []
    for i in range(1, n):  # Skip the first position (whole string)
        if i + Z[i] == n:  # This suffix reaches the end of the string
            third.append(Z[i])
    
    if not third:  # No valid suffixes found
        print('Just a legend')
        return
    
    if len(third) == 1:
        # Check if there's another occurrence of this prefix/suffix in the string
        if Z.count(third[0]) >= 2 or (1 <= third[0] < n and max(Z[1:third[0]], default=0) > third[0]):
            print(s[:third[0]])
        else:
            print('Just a legend')
    else:
        # If we have multiple candidates, check the longest
        if Z.count(third[0]) >= 2 or (1 <= third[0] < n and max(Z[1:third[0]], default=0) > third[0]):
            print(s[:third[0]])
        else:
            print(s[:third[1]])

if __name__ == "__main__":
    main()