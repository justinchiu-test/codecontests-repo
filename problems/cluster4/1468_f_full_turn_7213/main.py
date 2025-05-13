#!/usr/bin/env python3

from library import read_int, read_ints, gcd, print_answer
from collections import Counter

def solve_test_case():
    n = read_int()
    direction_counts = Counter()
    
    for _ in range(n):
        x, y, u, v = read_ints()
        dx, dy = u - x, v - y
        
        # Make sure we have the correct sign convention for the normalized vector
        g = gcd(abs(dx), abs(dy))
        dx //= g
        dy //= g
        
        direction_counts[(dx, dy)] += 1
    
    total_pairs = 0
    for direction, count in direction_counts.items():
        opposite = (-direction[0], -direction[1])
        if opposite in direction_counts:
            total_pairs += count * direction_counts[opposite]
    
    # Divide by 2 because each pair is counted twice
    print_answer(total_pairs // 2)

def solve():
    t = read_int()
    for _ in range(t):
        solve_test_case()

if __name__ == "__main__":
    solve()