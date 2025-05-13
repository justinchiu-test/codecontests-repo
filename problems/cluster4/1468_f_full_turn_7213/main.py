#!/usr/bin/env python3

import sys
from math import gcd
from collections import Counter

def solution(test_input):
    lines = test_input.strip().split('\n')
    t = int(lines[0])
    line_index = 1
    
    results = []
    for _ in range(t):
        n = int(lines[line_index])
        line_index += 1
        
        counter = Counter()
        for i in range(n):
            x, y, u, v = map(int, lines[line_index].split())
            line_index += 1
            
            dx, dy = u - x, v - y
            
            # Skip zero vectors
            if dx == 0 and dy == 0:
                continue
                
            # Normalize vector
            g = gcd(abs(dx), abs(dy)) if dx != 0 and dy != 0 else (abs(dx) if dx != 0 else abs(dy))
            dx //= g
            dy //= g
            
            # Ensure consistent representation
            if dx < 0 or (dx == 0 and dy < 0):
                dx, dy = -dx, -dy
                
            counter[(dx, dy)] += 1
        
        # Count pairs
        total = 0
        for (dx, dy), count in counter.items():
            opposite = (-dx, -dy)
            if opposite in counter:
                total += count * counter[opposite]
                
        results.append(str(total // 2))
    
    return '\n'.join(results)

if __name__ == "__main__":
    if sys.stdin.isatty():
        # Read from file for testing
        with open("tests/input_4.txt", "r") as f:
            print(solution(f.read()))
    else:
        # Read from stdin for judge
        print(solution(sys.stdin.read()))