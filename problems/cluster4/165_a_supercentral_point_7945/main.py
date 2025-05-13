#!/usr/bin/env python3

from library import Point, read_int, read_n_points, print_answer

def solve():
    n = read_int()
    points = read_n_points(n)
    
    ans = 0
    for p in points:
        has_right = has_left = has_upper = has_lower = False
        
        for q in points:
            if p.x < q.x and p.y == q.y:  # right neighbor
                has_right = True
            elif p.x > q.x and p.y == q.y:  # left neighbor
                has_left = True
            elif p.x == q.x and p.y < q.y:  # upper neighbor
                has_upper = True
            elif p.x == q.x and p.y > q.y:  # lower neighbor
                has_lower = True
        
        if has_right and has_left and has_upper and has_lower:
            ans += 1
    
    print_answer(ans)

if __name__ == "__main__":
    solve()