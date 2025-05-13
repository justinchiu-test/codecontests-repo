#!/usr/bin/env python3

from library import read_ints

def main():
    n, s = read_ints()
    
    # Special case for n=2
    if n == 2:
        xc, xd = read_ints()  # Read edge but don't use it
        print("%.10f" % s)
        return
    
    # Initialize node degrees
    degrees = [0] * n
    
    # Read edges and calculate node degrees
    for _ in range(n - 1):
        xc, xd = read_ints()
        degrees[xd - 1] += 1
        degrees[xc - 1] += 1
    
    # Count leaf nodes (degree = 1)
    leaf_count = sum(1 for degree in degrees if degree == 1)
    
    # Calculate diameter with proper formatting
    result = 2 * (s / leaf_count)
    print("%.10f" % result)

if __name__ == "__main__":
    main()