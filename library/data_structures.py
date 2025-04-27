"""
Common data structures for competitive programming.
"""

import heapq
from typing import Callable, Generic, List, TypeVar

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


class SegmentTree:
    """Segment Tree data structure for range queries and updates."""

    def __init__(
        self, arr: List[T], operation: Callable[[T, T], T], identity_element: T
    ):
        """Initialize a segment tree.

        Args:
            arr: The input array
            operation: The binary operation to apply (e.g., min, max, sum)
            identity_element: The identity element for the operation
        """
        self.n = len(arr)
        self.operation = operation
        self.identity = identity_element

        # Allocate memory for the segment tree
        self.size = 1
        while self.size < self.n:
            self.size *= 2

        self.tree = [identity_element] * (2 * self.size)

        # Build the segment tree
        for i in range(self.n):
            self.tree[self.size + i] = arr[i]

        for i in range(self.size - 1, 0, -1):
            self.tree[i] = operation(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, index: int, value: T) -> None:
        """Update the value at a specific index.

        Args:
            index: The index to update (0-based)
            value: The new value
        """
        index += self.size
        self.tree[index] = value

        while index > 1:
            index //= 2
            self.tree[index] = self.operation(
                self.tree[2 * index], self.tree[2 * index + 1]
            )

    def query(self, left: int, right: int) -> T:
        """Query a range [left, right).

        Args:
            left: The left bound (inclusive, 0-based)
            right: The right bound (exclusive, 0-based)

        Returns:
            The result of applying the operation over the range
        """
        left += self.size
        right += self.size
        result = self.identity

        while left < right:
            if left & 1:
                result = self.operation(result, self.tree[left])
                left += 1
            if right & 1:
                right -= 1
                result = self.operation(result, self.tree[right])
            left //= 2
            right //= 2

        return result


class LazySegmentTree:
    """Lazy Segment Tree for range updates and queries."""

    def __init__(
        self,
        arr: List[T],
        operation: Callable[[T, T], T],
        update_op: Callable[[T, T, int], T],
        identity: T,
        lazy_identity: T,
    ):
        """Initialize a lazy segment tree.

        Args:
            arr: The input array
            operation: The binary operation to apply (e.g., min, max, sum)
            update_op: Function to apply update values
            identity: The identity element for the operation
            lazy_identity: The identity element for lazy updates
        """
        self.n = len(arr)
        self.operation = operation
        self.update_op = update_op
        self.identity = identity
        self.lazy_identity = lazy_identity

        # Allocate memory for the segment tree
        self.size = 1
        while self.size < self.n:
            self.size *= 2

        self.tree = [identity] * (2 * self.size)
        self.lazy = [lazy_identity] * (2 * self.size)

        # Build the segment tree
        for i in range(self.n):
            self.tree[self.size + i] = arr[i]

        for i in range(self.size - 1, 0, -1):
            self.tree[i] = operation(self.tree[2 * i], self.tree[2 * i + 1])

    def push(self, index: int, left: int, right: int) -> None:
        """Push lazy updates down the tree.

        Args:
            index: The current node index
            left: The left bound of the node's range
            right: The right bound of the node's range
        """
        if self.lazy[index] != self.lazy_identity:
            self.tree[index] = self.update_op(
                self.tree[index], self.lazy[index], right - left
            )

            if index < self.size:  # Not a leaf node
                self.lazy[2 * index] = self.lazy[index]
                self.lazy[2 * index + 1] = self.lazy[index]

            self.lazy[index] = self.lazy_identity

    def update_range(self, left: int, right: int, value: T) -> None:
        """Update a range [left, right) with a value.

        Args:
            left: The left bound (inclusive, 0-based)
            right: The right bound (exclusive, 0-based)
            value: The value to update with
        """
        self._update_range(1, 0, self.size, left, right, value)

    def _update_range(
        self,
        index: int,
        segment_left: int,
        segment_right: int,
        query_left: int,
        query_right: int,
        value: T,
    ) -> None:
        """Recursive helper for range updates.

        Args:
            index: The current node index
            segment_left: The left bound of the node's range
            segment_right: The right bound of the node's range
            query_left: The left bound of the query range
            query_right: The right bound of the query range
            value: The value to update with
        """
        self.push(index, segment_left, segment_right)

        # No overlap
        if segment_right <= query_left or query_right <= segment_left:
            return

        # Complete overlap
        if query_left <= segment_left and segment_right <= query_right:
            self.lazy[index] = value
            self.push(index, segment_left, segment_right)
            return

        # Partial overlap
        mid = (segment_left + segment_right) // 2
        self._update_range(2 * index, segment_left, mid, query_left, query_right, value)
        self._update_range(
            2 * index + 1, mid, segment_right, query_left, query_right, value
        )

        self.tree[index] = self.operation(
            self.tree[2 * index], self.tree[2 * index + 1]
        )

    def query(self, left: int, right: int) -> T:
        """Query a range [left, right).

        Args:
            left: The left bound (inclusive, 0-based)
            right: The right bound (exclusive, 0-based)

        Returns:
            The result of applying the operation over the range
        """
        return self._query(1, 0, self.size, left, right)

    def _query(
        self,
        index: int,
        segment_left: int,
        segment_right: int,
        query_left: int,
        query_right: int,
    ) -> T:
        """Recursive helper for range queries.

        Args:
            index: The current node index
            segment_left: The left bound of the node's range
            segment_right: The right bound of the node's range
            query_left: The left bound of the query range
            query_right: The right bound of the query range

        Returns:
            The result of applying the operation over the range
        """
        self.push(index, segment_left, segment_right)

        # No overlap
        if segment_right <= query_left or query_right <= segment_left:
            return self.identity

        # Complete overlap
        if query_left <= segment_left and segment_right <= query_right:
            return self.tree[index]

        # Partial overlap
        mid = (segment_left + segment_right) // 2
        left_result = self._query(2 * index, segment_left, mid, query_left, query_right)
        right_result = self._query(
            2 * index + 1, mid, segment_right, query_left, query_right
        )

        return self.operation(left_result, right_result)


class FenwickTree:
    """Fenwick Tree (Binary Indexed Tree) for range sum queries and point updates."""

    def __init__(self, n: int):
        """Initialize a Fenwick tree with n elements.

        Args:
            n: The number of elements
        """
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, index: int, delta: int) -> None:
        """Update the value at a specific index by delta.

        Args:
            index: The index to update (0-based)
            delta: The value to add
        """
        index += 1  # Convert to 1-based indexing

        while index <= self.n:
            self.tree[index] += delta
            index += index & -index  # Move to next relevant index

    def prefix_sum(self, index: int) -> int:
        """Calculate the sum of elements from 0 to index (inclusive).

        Args:
            index: The upper bound (inclusive, 0-based)

        Returns:
            The sum of elements from 0 to index
        """
        index += 1  # Convert to 1-based indexing
        result = 0

        while index > 0:
            result += self.tree[index]
            index -= index & -index  # Move to previous relevant index

        return result

    def range_sum(self, left: int, right: int) -> int:
        """Calculate the sum of elements from left to right (inclusive).

        Args:
            left: The lower bound (inclusive, 0-based)
            right: The upper bound (inclusive, 0-based)

        Returns:
            The sum of elements from left to right
        """
        return self.prefix_sum(right) - (self.prefix_sum(left - 1) if left > 0 else 0)


class SparseTable:
    """Sparse Table for static range queries with idempotent operations."""

    def __init__(self, arr: List[T], operation: Callable[[T, T], T]):
        """Initialize a sparse table.

        Args:
            arr: The input array
            operation: The binary operation to apply (e.g., min, max, gcd)
        """
        self.n = len(arr)
        self.operation = operation

        # Calculate the maximum log value
        self.log_n = len(bin(self.n)) - 2

        # Initialize sparse table
        self.table = [[0] * self.n for _ in range(self.log_n)]

        # Fill the table for ranges of size 1
        for i in range(self.n):
            self.table[0][i] = arr[i]

        # Fill the table for larger ranges
        for i in range(1, self.log_n):
            j = 0
            while j + (1 << i) <= self.n:
                self.table[i][j] = self.operation(
                    self.table[i - 1][j], self.table[i - 1][j + (1 << (i - 1))]
                )
                j += 1

    def query(self, left: int, right: int) -> T:
        """Query a range [left, right].

        Args:
            left: The left bound (inclusive, 0-based)
            right: The right bound (inclusive, 0-based)

        Returns:
            The result of applying the operation over the range
        """
        length = right - left + 1
        log = len(bin(length)) - 3  # log_2(length)

        return self.operation(
            self.table[log][left], self.table[log][right - (1 << log) + 1]
        )


class Trie:
    """Trie data structure for efficient string operations."""

    def __init__(self):
        """Initialize an empty trie."""
        self.root = {}
        self.end_symbol = "$"

    def insert(self, word: str) -> None:
        """Insert a word into the trie.

        Args:
            word: The word to insert
        """
        node = self.root

        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]

        node[self.end_symbol] = True

    def search(self, word: str) -> bool:
        """Check if a word exists in the trie.

        Args:
            word: The word to search for

        Returns:
            True if the word exists in the trie, False otherwise
        """
        node = self.root

        for char in word:
            if char not in node:
                return False
            node = node[char]

        return self.end_symbol in node

    def starts_with(self, prefix: str) -> bool:
        """Check if any word in the trie starts with the given prefix.

        Args:
            prefix: The prefix to check

        Returns:
            True if any word starts with the prefix, False otherwise
        """
        node = self.root

        for char in prefix:
            if char not in node:
                return False
            node = node[char]

        return True


class PriorityQueue(Generic[T]):
    """Priority queue implementation using heapq."""

    def __init__(self):
        """Initialize an empty priority queue."""
        self.elements = []
        self.counter = 0  # Used for tie-breaking

    def push(self, item: T, priority: float) -> None:
        """Add an item to the queue with a given priority.

        Args:
            item: The item to add
            priority: The priority of the item (lower values have higher priority)
        """
        heapq.heappush(self.elements, (priority, self.counter, item))
        self.counter += 1

    def pop(self) -> T:
        """Remove and return the item with the highest priority.

        Returns:
            The item with the highest priority
        """
        if self.is_empty():
            raise ValueError("Priority queue is empty")

        _, _, item = heapq.heappop(self.elements)
        return item

    def peek(self) -> T:
        """Return, but do not remove, the item with the highest priority.

        Returns:
            The item with the highest priority
        """
        if self.is_empty():
            raise ValueError("Priority queue is empty")

        _, _, item = self.elements[0]
        return item

    def is_empty(self) -> bool:
        """Check if the priority queue is empty.

        Returns:
            True if the priority queue is empty, False otherwise
        """
        return len(self.elements) == 0

    def __len__(self) -> int:
        """Return the number of items in the priority queue.

        Returns:
            The number of items
        """
        return len(self.elements)


class DisjointSetUnion:
    """Disjoint Set Union (Union-Find) data structure.

    This is a wrapper around the DSU class in the graphs package.
    """

    def __init__(self, n: int):
        """Initialize a DSU with n elements.

        Args:
            n: Number of elements (0 to n-1)
        """
        from library.graphs.dsu import DSU

        self.dsu = DSU(n)

    def find(self, x: int) -> int:
        """Find the representative (root) of the set containing x.

        Args:
            x: The element to find

        Returns:
            The root element of the set containing x
        """
        return self.dsu.find(x)

    def union(self, x: int, y: int) -> bool:
        """Union the sets containing x and y.

        Args:
            x: First element
            y: Second element

        Returns:
            True if x and y were in different sets (union performed),
            False if they were already in the same set
        """
        return self.dsu.union(x, y)

    def connected(self, x: int, y: int) -> bool:
        """Check if x and y are in the same set.

        Args:
            x: First element
            y: Second element

        Returns:
            True if x and y are in the same set, False otherwise
        """
        return self.dsu.connected(x, y)

    def get_size(self, x: int) -> int:
        """Get the size of the set containing x.

        Args:
            x: The element

        Returns:
            Size of the set containing x
        """
        return self.dsu.get_size(x)

    def get_components(self) -> int:
        """Get the number of disjoint sets.

        Returns:
            Number of disjoint sets
        """
        return self.dsu.get_components()
