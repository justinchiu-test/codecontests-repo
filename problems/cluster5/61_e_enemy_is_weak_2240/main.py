#!/usr/bin/env python3

from sys import path
path.append('..')
from library import read_int, read_ints

class SegmentTree:
    """
    Segment tree with point updates and range queries.
    Supports multiple columns of data per node.
    """
    def __init__(self, n):
        self.tree = [[0, 0] for _ in range(n << 1)]  # Two columns per node
        self.n = n

    def query(self, r, col):
        """Query the sum in range [0, r) for column col"""
        res = 0
        l = self.n
        r += self.n

        while l < r:
            if l & 1:
                res += self.tree[l][col]
                l += 1

            if r & 1:
                r -= 1
                res += self.tree[r][col]

            l >>= 1
            r >>= 1

        return res

    def update(self, ix, val, col):
        """Add val to position ix in column col"""
        ix += self.n

        # Update value
        self.tree[ix][col] += val

        # Propagate changes upward
        while ix > 1:
            self.tree[ix >> 1][col] = self.tree[ix][col] + self.tree[ix ^ 1][col]
            ix >>= 1

def main():
    n = read_int()
    a = read_ints()
    
    # Initialize segment tree and result
    tree = SegmentTree(n)
    ans = 0
    
    # Create a mapping from values to their sorted positions (ranks)
    mem = {i: j for j, i in enumerate(sorted(a))}
    
    # Process array from right to left
    for i in range(n - 1, -1, -1):
        cur = mem[a[i]]  # Get rank of current element
        
        # Get count of elements that are greater than current element and
        # have at least one element greater than them to their right
        ans += tree.query(cur, 1)
        
        # Increment count of elements greater than current in column 0
        tree.update(cur, 1, 0)
        
        # Update column 1 with count of elements greater than current
        # that have at least one element greater than them to their right
        tree.update(cur, tree.query(cur, 0), 1)
    
    print(ans)

if __name__ == "__main__":
    main()