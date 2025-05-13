#!/usr/bin/env python3

from library import read_ints, normalize_vector, Point, print_answer

def solve():
    # Read input
    n, x0, y0 = read_ints()
    gun = Point(x0, y0)
    
    # Use a set to store unique normalized vectors (directions)
    directions = set()
    
    for _ in range(n):
        x, y = read_ints()
        target = Point(x, y)
        
        # Calculate the vector from gun to stormtrooper
        dx = target.x - gun.x
        dy = target.y - gun.y
        
        # Normalize the vector to get a unique direction
        direction = normalize_vector(dx, dy)
        
        # Add the direction to our set of unique directions
        directions.add(direction)
    
    # The number of unique directions is the minimum number of shots needed
    print_answer(len(directions))

if __name__ == "__main__":
    solve()