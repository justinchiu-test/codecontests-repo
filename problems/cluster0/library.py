"""
Library file for cluster0.
This contains shared code that can be imported by problems in this cluster.
"""
from collections import defaultdict, deque
import sys
from typing import List, Dict, Set, Tuple, Callable, Any, Iterator, Optional, Union, DefaultDict

# Input parsing utilities
def ints() -> List[int]:
    """Parse a line of space-separated integers."""
    return list(map(int, input().split()))

def int_tuple() -> Tuple[int, ...]:
    """Parse a line of space-separated integers into a tuple."""
    return tuple(map(int, input().split()))

def int_lists(n: int) -> List[List[int]]:
    """Parse n lines of space-separated integers."""
    return [ints() for _ in range(n)]

def chars() -> List[str]:
    """Parse a line into individual characters."""
    return list(input().strip())

# Graph utilities
def read_graph(n: int, m: int, directed: bool = False, indexed_from: int = 1) -> List[List[int]]:
    """
    Read a graph with n nodes and m edges.

    Args:
        n: Number of nodes
        m: Number of edges
        directed: If True, edges are directed
        indexed_from: The index of the first node (usually 1 or 0)

    Returns:
        Adjacency list representation of the graph
    """
    graph = [[] for _ in range(n + (1 if indexed_from == 1 else 0))]
    for _ in range(m):
        u, v = ints()
        u -= indexed_from
        v -= indexed_from
        graph[u].append(v)
        if not directed:
            graph[v].append(u)
    return graph

def read_tree(n: int, indexed_from: int = 1) -> List[List[int]]:
    """
    Read a tree with n nodes (n-1 edges).

    Args:
        n: Number of nodes
        indexed_from: The index of the first node (usually 1 or 0)

    Returns:
        Adjacency list representation of the tree
    """
    return read_graph(n, n-1, directed=False, indexed_from=indexed_from)

def read_tree_with_parent(n: int, indexed_from: int = 1) -> List[List[int]]:
    """
    Read a tree with n nodes where each node specifies its parent.
    Node 1 is assumed to be the root with no parent.

    Args:
        n: Number of nodes
        indexed_from: The index of the first node (usually 1 or 0)

    Returns:
        Adjacency list representation of the tree
    """
    parents = ints()
    graph = [[] for _ in range(n + (1 if indexed_from == 1 else 0))]

    for i in range(1, n):
        parent = parents[i - 1] - indexed_from
        child = i + (1 - indexed_from)
        graph[parent].append(child)
        graph[child].append(parent)

    return graph

def count_degrees(n: int, edges: List[Tuple[int, int]], indexed_from: int = 1) -> List[int]:
    """
    Count degrees of nodes in a graph from an edge list.

    Args:
        n: Number of nodes
        edges: List of edges as (u, v) pairs
        indexed_from: The index of the first node (usually 1 or 0)

    Returns:
        List where degrees[u] is the degree of node u
    """
    degrees = [0] * (n + (1 if indexed_from == 1 else 0))
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1
    return degrees

def compute_node_degrees(graph: List[List[int]]) -> List[int]:
    """
    Compute the degree of each node in a graph.

    Args:
        graph: Adjacency list representation of the graph

    Returns:
        List where degrees[u] is the degree of node u
    """
    return [len(neighbors) for neighbors in graph]

def identify_network_topology(n: int, degrees: List[int]) -> str:
    """
    Identify the topology of a network based on degrees.

    Args:
        n: Number of nodes
        degrees: List of node degrees

    Returns:
        String describing the topology: "bus", "ring", "star", or "unknown"
    """
    # Count nodes with specific degrees
    degree_1_count = 0  # Nodes with degree 1
    degree_2_count = 0  # Nodes with degree 2
    degree_n_minus_1_count = 0  # Nodes with degree n-1

    for i in range(1, n + 1):
        if degrees[i] == 1:
            degree_1_count += 1
        elif degrees[i] == 2:
            degree_2_count += 1
        elif degrees[i] == n - 1:
            degree_n_minus_1_count += 1

    # Determine topology
    if degree_1_count == 2 and degree_2_count == n - 2:
        return "bus topology"
    elif degree_2_count == n:
        return "ring topology"
    elif degree_1_count == n - 1 and degree_n_minus_1_count == 1:
        return "star topology"
    else:
        return "unknown topology"

# Traversal algorithms
def bfs(graph: List[List[int]], start: int) -> List[int]:
    """
    Breadth-first search traversal of a graph.

    Args:
        graph: Adjacency list representation of the graph
        start: Starting node

    Returns:
        List of distances from start to each node (or -1 if unreachable)
    """
    n = len(graph)
    dist = [-1] * n
    dist[start] = 0
    queue = deque([start])

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)

    return dist

def bfs_with_cats(tree: List[List[int]], cats: List[int], m: int) -> int:
    """
    BFS with cat limitation for Kefa and Park problem.

    Args:
        tree: Adjacency list representation of the tree
        cats: List where cats[i] = 1 if node i has a cat, 0 otherwise
        m: Maximum number of consecutive cats allowed

    Returns:
        Number of leaf nodes reachable without exceeding m consecutive cats
    """
    n = len(tree)
    visited = [False] * n
    leaf_count = 0

    queue = [(0, 0)]  # (node, consecutive cats)
    i = 0

    while i < len(queue):
        node, consecutive_cats = queue[i]
        visited[node] = True

        current_cats = consecutive_cats
        if cats[node] == 1:
            current_cats += 1
        else:
            current_cats = 0

        if current_cats <= m:
            is_leaf = True
            for neighbor in tree[node]:
                if not visited[neighbor]:
                    is_leaf = False
                    queue.append((neighbor, current_cats))
            if is_leaf and node != 0:  # Count leaf nodes (except root if it's a leaf)
                leaf_count += 1

        i += 1

    return leaf_count

def dfs(graph: List[List[int]], start: int) -> List[bool]:
    """
    Depth-first search traversal of a graph.

    Args:
        graph: Adjacency list representation of the graph
        start: Starting node

    Returns:
        List indicating which nodes are reachable from start
    """
    n = len(graph)
    visited = [False] * n

    def _dfs(u: int) -> None:
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                _dfs(v)

    _dfs(start)
    return visited

def dfs_with_parent(graph: List[List[int]], start: int, parent: int = -1) -> List[bool]:
    """
    DFS traversal that tracks parents to avoid cycles in undirected graphs.

    Args:
        graph: Adjacency list representation of the graph
        start: Starting node
        parent: Parent of the starting node

    Returns:
        List of visited nodes
    """
    n = len(graph)
    visited = [False] * n

    def _dfs(u: int, parent: int) -> None:
        visited[u] = True
        for v in graph[u]:
            if v != parent and not visited[v]:
                _dfs(v, u)

    _dfs(start, parent)
    return visited

def dfs_with_size(graph: List[List[int]], root: int = 0, include_self: bool = True) -> List[int]:
    """
    DFS to compute subtree sizes in a tree.

    Args:
        graph: Adjacency list representation of the tree
        root: Root node
        include_self: If True, include the node itself in size calculation

    Returns:
        List where sizes[u] is the size of the subtree rooted at u
    """
    n = len(graph)
    sizes = [1 if include_self else 0] * n

    def _dfs(node: int, parent: int) -> int:
        size = 1  # Count the node itself
        for child in graph[node]:
            if child != parent:
                child_size = _dfs(child, node)
                size += child_size

        if include_self:
            sizes[node] = size
        else:
            sizes[node] = size - 1  # Exclude the node itself

        return size

    _dfs(root, -1)
    return sizes

def dfs_expected_length(graph: List[List[int]], start: int) -> float:
    """
    DFS to compute expected path length for Journey problem.

    Args:
        graph: Adjacency list representation of the tree
        start: Starting node (root)

    Returns:
        Expected length of a journey
    """
    n = len(graph)
    visited = [False] * n
    result = 0.0

    def dfs_helper(node: int, depth: int, prob: float):
        nonlocal result
        visited[node] = True

        # Count number of unvisited neighbors
        unvisited = sum(1 for next_node in graph[node] if not visited[next_node])

        # If leaf node (except root), add to result
        if node != start and len(graph[node]) == 1:
            result += depth * prob
            return

        # Visit unvisited neighbors with equal probability
        for next_node in graph[node]:
            if not visited[next_node]:
                next_prob = prob
                if unvisited > 0:
                    next_prob /= unvisited
                dfs_helper(next_node, depth + 1, next_prob)

    dfs_helper(start, 0, 1.0)
    return result

def count_color_changes(n: int, parents: List[int], colors: List[int]) -> int:
    """
    Count color changes needed in a tree coloring.

    Args:
        n: Number of nodes
        parents: List where parents[i-2] is the parent of node i (1-indexed)
        colors: List of desired colors for each node

    Returns:
        Minimum number of color operations needed
    """
    # Create tree as adjacency list
    tree = [[] for _ in range(n + 1)]
    for i in range(2, n + 1):
        parent = parents[i - 2]
        tree[parent].append(i)

    # BFS to count color changes
    queue = deque([1])  # Start from root
    color_changes = 1  # Root node always needs coloring

    while queue:
        node = queue.popleft()

        for child in tree[node]:
            # If child color is different from parent, count a color change
            if colors[child - 1] != colors[node - 1]:
                color_changes += 1
            queue.append(child)

    return color_changes

def optimal_edge_removal(tree: List[List[int]], n: int) -> int:
    """
    Calculate the maximum number of edges that can be removed from a tree
    to leave all components with even size.

    Args:
        tree: Adjacency list representation of the tree
        n: Number of nodes

    Returns:
        Maximum number of edges to remove, or -1 if impossible
    """
    # If n is odd, no solution exists
    if n % 2 != 0:
        return -1

    # Compute subtree sizes
    sizes = dfs_with_size(tree, 0, False)

    # Count edges to remove
    removed_edges = 0
    for i in range(1, n):
        if sizes[i] % 2 == 1:
            removed_edges += 1

    return removed_edges

# Union-Find (Disjoint Set Union)
class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.count = n  # Number of connected components

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """
        Union of sets containing x and y.
        Returns True if x and y were in different sets before the union.
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        # Union by size
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        self.count -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        """Check if x and y are in the same set."""
        return self.find(x) == self.find(y)

# Output utilities
def print_list(lst: List[Any], sep: str = ' ') -> None:
    """Print a list with custom separator."""
    print(sep.join(map(str, lst)))

def print_yes_no(condition: bool, yes_str: str = "YES", no_str: str = "NO") -> None:
    """Print yes or no based on a condition."""
    print(yes_str if condition else no_str)

# Recursive limit
def set_recursion_limit(limit: int = 10**6) -> None:
    """Set recursion limit to a higher value."""
    sys.setrecursionlimit(limit)

# Modular arithmetic
MOD = 10**9 + 7

def mod_add(a: int, b: int, mod: int = MOD) -> int:
    """Add two numbers and take modulo."""
    return (a + b) % mod

def mod_mul(a: int, b: int, mod: int = MOD) -> int:
    """Multiply two numbers and take modulo."""
    return (a * b) % mod

def mod_pow(a: int, b: int, mod: int = MOD) -> int:
    """Calculate (a^b) % mod efficiently."""
    result = 1
    a %= mod
    while b:
        if b & 1:
            result = (result * a) % mod
        a = (a * a) % mod
        b >>= 1
    return result