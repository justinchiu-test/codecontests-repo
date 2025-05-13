#!/usr/bin/env python3

from library import read_int, read_ints

class SegmentTree:
    """
    Segment tree implementation with two channels.

    This tree supports two operations:
    1. Update a position with a value in a specific channel
    2. Query the sum of a range [l, r) in a specific channel
    """
    def __init__(self, size):
        """Initialize a segment tree of given size with two channels."""
        self.tree = [[0, 0] for _ in range(size << 1)]  # Two channels (0 and 1)
        self.size = size

    def query(self, r, channel):
        """
        Query the sum in range [size, r) for a specific channel.

        Args:
            r: Right boundary (exclusive)
            channel: Channel to query (0 or 1)

        Returns:
            Sum of values in range [size, r) in the specified channel
        """
        result = 0
        l = self.size  # Start from the leftmost leaf
        r += self.size  # Convert index to tree node

        while l < r:
            if l & 1:  # If l is odd, it's a right child
                result += self.tree[l][channel]
                l += 1

            if r & 1:  # If r is odd, it's a right child
                r -= 1
                result += self.tree[r][channel]

            # Move to parent nodes
            l >>= 1
            r >>= 1

        return result

    def update(self, index, value, channel):
        """
        Update a position with a value in a specific channel.

        Args:
            index: Position to update
            value: Value to add
            channel: Channel to update (0 or 1)
        """
        index += self.size  # Convert index to tree node

        # Update leaf node
        self.tree[index][channel] += value

        # Update parent nodes
        while index > 1:
            parent = index >> 1
            self.tree[parent][channel] = self.tree[index][channel] + self.tree[index ^ 1][channel]
            index = parent

def enemy_is_weak():
    """
    Solution for the Enemy is Weak problem.

    The problem asks to find the number of triplets i < j < k such that
    a[i] > a[j] > a[k], where a is the array of soldier powers.

    We use a segment tree to maintain two counters:
    - Counter 0: Number of elements greater than the current element
    - Counter 1: Number of pairs (i, j) such that i < j and a[i] > a[j]
      ending at the current position
    """
    # Read input
    n = read_int()
    powers = read_ints()

    # Create segment tree and initialize answer
    tree = SegmentTree(n)
    answer = 0

    # Map original values to ranks (0 to n-1) to make tree operations easier
    # This is needed because powers can be very large (up to 10^9)
    value_to_rank = {value: rank for rank, value in enumerate(sorted(powers))}

    # Process array from right to left
    for i in range(n - 1, -1, -1):
        # Get rank of current value
        rank = value_to_rank[powers[i]]

        # Count triplets where the current element is the smallest (a[k])
        # These are pairs (a[i] > a[j]) that end before this element
        answer += tree.query(rank, 1)

        # Update count of elements greater than current element
        tree.update(rank, 1, 0)

        # Update count of pairs (a[i] > a[j]) ending at current element
        # The number of such pairs is the number of elements greater than current element
        tree.update(rank, tree.query(rank, 0), 1)

    return answer

print(enemy_is_weak())
