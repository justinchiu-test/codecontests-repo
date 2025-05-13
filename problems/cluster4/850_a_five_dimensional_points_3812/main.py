#!/usr/bin/env python3

from library import read_int, read_ints, print_answer

class Point5D:
    def __init__(self, coords):
        self.coords = coords
    
    def dot_product(self, other):
        return sum(a * b for a, b in zip(self.coords, other.coords))
    
    def angle_acute(self, p1, p2):
        # Check if angle between vectors (self->p1) and (self->p2) is acute
        v1 = [p1.coords[i] - self.coords[i] for i in range(5)]
        v2 = [p2.coords[i] - self.coords[i] for i in range(5)]
        
        # Dot product > 0 means acute angle
        return sum(v1[i] * v2[i] for i in range(5)) > 0

def solve():
    n = read_int()
    points = []
    
    for _ in range(n):
        coords = read_ints()
        points.append(Point5D(coords))
    
    # Special case for large n as per problem constraints
    if n > 11:
        print_answer(0)
        return
    
    # Find points that can be vertices of a convex cone
    valid_points = []
    
    for i in range(n):
        is_valid = True
        for j in range(n):
            if i == j:
                continue
            
            for k in range(j + 1, n):
                if i == k:
                    continue
                
                # Check if angle between vectors is acute
                if points[i].angle_acute(points[j], points[k]):
                    is_valid = False
                    break
            
            if not is_valid:
                break
        
        if is_valid:
            valid_points.append(i + 1)  # Add 1 since indices are 1-based in output
    
    # Print results
    print_answer(len(valid_points))
    for point_idx in valid_points:
        print_answer(point_idx)

if __name__ == "__main__":
    solve()