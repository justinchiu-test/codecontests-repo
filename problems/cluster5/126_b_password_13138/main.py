#!/usr/bin/env python3

from sys import path
path.append('..')
from library import read_str, z_algorithm

def main():
    s = read_str()
    n = len(s)
    
    # Compute Z-function for string s
    Z = z_algorithm(s)
    
    # Find strings that are both prefixes and suffixes
    suffix_prefixes = []
    for i in range(1, n):
        if i + Z[i] == n:  # If substring matches from i to the end
            suffix_prefixes.append(Z[i])
    
    # Sort by length (descending)
    suffix_prefixes.sort(reverse=True)
    
    # If no suffix and prefix matches found
    if not suffix_prefixes:
        print("Just a legend")
        return
    
    # Check if the longest suffix-prefix appears elsewhere in the string
    longest_suffix_prefix = suffix_prefixes[0]
    
    # Check if the longest suffix-prefix appears in the middle of the string
    if Z.count(longest_suffix_prefix) >= 2 or max(Z) > longest_suffix_prefix:
        print(s[:longest_suffix_prefix])
    # If there's a second longest suffix-prefix, use it
    elif len(suffix_prefixes) > 1:
        print(s[:suffix_prefixes[1]])
    else:
        print("Just a legend")

if __name__ == "__main__":
    main()