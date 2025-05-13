#!/usr/bin/env python3

from sys import stdin
from library import Point

stdin = iter(stdin)

def min_distance_less_than_d1(ab1, ab2, d1):
    """Check if the minimum distance between a person's trajectories is less than d1."""
    # Vector between the line segments
    L = ab2 - ab1
    
    # Project the start and end points onto L
    proj1 = ab1.dot(L)
    proj2 = ab2.dot(L)
    
    # Check if minimum distance point is between the endpoints
    between = (proj1 * proj2 < 0)
    
    if between:
        # Minimum distance is the altitude to the line
        # Check if altitude is less than d1
        return ab1.cross(L)**2 <= d1**2 * L.norm_square()
    else:
        # Minimum distance is one of the endpoints
        min_square = min(ab1.norm_square(), ab2.norm_square())
        return min_square <= d1**2


if __name__ == "__main__":
    N = int(next(stdin))
    d1, d2 = (int(x) for x in next(stdin).split())
    ABs = []
    
    for _ in range(N):
        Ax, Ay, Bx, By = (int(x) for x in next(stdin).split())
        # Store the vector between positions A and B
        ABs.append(Point(Bx - Ax, By - Ay))

    resetState = True
    count = 0

    for i in range(len(ABs) - 1):
        ab1, ab2 = ABs[i:i+2]
        
        # Count "Hello" if friends are close enough and either:
        # 1) It's their first meeting, or
        # 2) They were far enough apart since last meeting
        if resetState and min_distance_less_than_d1(ab1, ab2, d1):
            count += 1
            resetState = False
        
        # Reset state if distance becomes greater than d2
        resetState = resetState or (ab2.norm_square() > d2**2)

    print(count)