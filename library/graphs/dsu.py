"""
Disjoint Set Union (DSU) implementation for graph problems.
"""

from typing import Dict, List


class DSU:
    """Disjoint Set Union (Union-Find) data structure.

    Supports union by rank and path compression for efficient operations.
    """

    def __init__(self, n: int):
        """Initialize a DSU with n elements.

        Args:
            n: Number of elements (0 to n-1)
        """
        self.parent = list(range(n))
        self.rank = [1] * n
        self.size = [1] * n
        self.components = n

    def find(self, x: int) -> int:
        """Find the representative (root) of the set containing x.

        Uses path compression for efficiency.

        Args:
            x: The element to find

        Returns:
            The root element of the set containing x
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """Union the sets containing x and y.

        Uses union by rank for efficiency.

        Args:
            x: First element
            y: Second element

        Returns:
            True if x and y were in different sets (union performed),
            False if they were already in the same set
        """
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return False

        # Union by rank
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
            self.size[y_root] += self.size[x_root]
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
            self.size[x_root] += self.size[y_root]
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1
            self.size[x_root] += self.size[y_root]

        self.components -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        """Check if x and y are in the same set.

        Args:
            x: First element
            y: Second element

        Returns:
            True if x and y are in the same set, False otherwise
        """
        return self.find(x) == self.find(y)

    def get_size(self, x: int) -> int:
        """Get the size of the set containing x.

        Args:
            x: The element

        Returns:
            Size of the set containing x
        """
        return self.size[self.find(x)]

    def get_components(self) -> int:
        """Get the number of disjoint sets.

        Returns:
            Number of disjoint sets
        """
        return self.components

    def get_groups(self) -> Dict[int, List[int]]:
        """Get all groups as a dictionary mapping roots to lists of elements.

        Returns:
            Dictionary where keys are roots and values are lists of elements in that set
        """
        groups = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            if root not in groups:
                groups[root] = []
            groups[root].append(i)
        return groups
