from collections import defaultdict, deque
from queue import Queue
import sys
from typing import List, Tuple, Dict, Set, Optional, Callable, Any, Union

# Input/Output handling functions
def read_int() -> int:
    """Read a single integer from input."""
    return int(input())

def read_ints() -> List[int]:
    """Read a line of space-separated integers."""
    return list(map(int, input().split()))

def read_graph(n: int, m: int, directed: bool = False, indexed: int = 1) -> List[List[int]]:
    """
    Read a graph with n nodes and m edges.

    Args:
        n: Number of nodes
        m: Number of edges
        directed: If True, the graph is directed
        indexed: Base index of nodes (1 for 1-indexed, 0 for 0-indexed)

    Returns:
        Adjacency list representation of the graph
    """
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = read_ints()
        u -= indexed
        v -= indexed
        graph[u].append(v)
        if not directed:
            graph[v].append(u)
    return graph

def read_tree(n: int, indexed: int = 1) -> List[List[int]]:
    """
    Read a tree with n nodes.

    Args:
        n: Number of nodes
        indexed: Base index of nodes (1 for 1-indexed, 0 for 0-indexed)

    Returns:
        Adjacency list representation of the tree
    """
    return read_graph(n, n-1, directed=False, indexed=indexed)

def read_test_cases() -> int:
    """
    Read the number of test cases from input.
    If the first line contains multiple values, assumes it's not a test case count
    and returns 1 (for a single test case).

    Returns:
        Number of test cases
    """
    line = input().strip()
    if len(line.split()) == 1:
        return int(line)
    else:
        # Put the line back to be read by the next input call
        global _saved_line
        _saved_line = line
        return 1

_saved_line = None
def read_line():
    """
    Read a line from input, or use a saved line if available.
    This is used in conjunction with read_test_cases.

    Returns:
        The line read from input
    """
    global _saved_line
    if _saved_line:
        line = _saved_line
        _saved_line = None
        return line
    return input()

# Graph algorithms
def dfs(graph: List[List[int]], start: int,
        visit_fn: Optional[Callable[[int], Any]] = None,
        visited: Optional[List[bool]] = None) -> List[bool]:
    """
    Perform depth-first search on a graph.

    Args:
        graph: Adjacency list representation of the graph
        start: Starting node
        visit_fn: Function to call when visiting a node
        visited: Boolean array of visited nodes

    Returns:
        Boolean array indicating which nodes were visited
    """
    if visited is None:
        visited = [False] * len(graph)

    def _dfs(node: int):
        visited[node] = True
        if visit_fn:
            visit_fn(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                _dfs(neighbor)

    _dfs(start)
    return visited

def bfs(graph: List[List[int]], start: int,
        visit_fn: Optional[Callable[[int], Any]] = None) -> List[bool]:
    """
    Perform breadth-first search on a graph.

    Args:
        graph: Adjacency list representation of the graph
        start: Starting node
        visit_fn: Function to call when visiting a node

    Returns:
        Boolean array indicating which nodes were visited
    """
    n = len(graph)
    visited = [False] * n
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        if visit_fn:
            visit_fn(node)

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return visited

def bipartite_coloring(graph: List[List[int]], start: int = 0) -> List[int]:
    """
    Color a graph using BFS to find a bipartite coloring.

    Args:
        graph: Adjacency list representation of the graph
        start: Starting node for BFS

    Returns:
        Array where color[i] is the color of node i (0 or 1), or -1 if unvisited
    """
    n = len(graph)
    color = [-1] * n
    color[start] = 0

    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if color[neighbor] == -1:
                color[neighbor] = 1 - color[node]
                queue.append(neighbor)
            elif color[neighbor] == color[node]:
                # Not bipartite
                return []

    return color

def subtree_size(graph: List[List[int]], node: int, parent: int = -1) -> int:
    """
    Calculate the size of the subtree rooted at a node.

    Args:
        graph: Adjacency list representation of the graph
        node: Root of the subtree
        parent: Parent of the node (to avoid going back)

    Returns:
        Size of the subtree (including the root)
    """
    size = 1  # Count the node itself
    for neighbor in graph[node]:
        if neighbor != parent:
            size += subtree_size(graph, neighbor, node)
    return size

def calculate_subtree_sizes(graph: List[List[int]], root: int = 0) -> List[int]:
    """
    Calculate the sizes of all subtrees in a tree.

    Args:
        graph: Adjacency list representation of the tree
        root: Root of the tree

    Returns:
        Array where subtree_sizes[i] is the size of the subtree rooted at node i
    """
    n = len(graph)
    subtree_sizes = [0] * n

    def dfs(node, parent):
        size = 1  # Count the node itself
        for neighbor in graph[node]:
            if neighbor != parent:
                size += dfs(neighbor, node)
        subtree_sizes[node] = size
        return size

    dfs(root, -1)
    return subtree_sizes

def tree_dfs(graph: List[List[int]], node: int, parent: int = -1,
             pre_visit: Optional[Callable[[int, int], Any]] = None,
             post_visit: Optional[Callable[[int, int], Any]] = None) -> None:
    """
    Perform a DFS on a tree with pre and post visit callbacks.

    Args:
        graph: Adjacency list representation of the tree
        node: Current node
        parent: Parent of the node
        pre_visit: Function to call before visiting children (params: node, parent)
        post_visit: Function to call after visiting children (params: node, parent)
    """
    if pre_visit:
        pre_visit(node, parent)

    for neighbor in graph[node]:
        if neighbor != parent:
            tree_dfs(graph, neighbor, node, pre_visit, post_visit)

    if post_visit:
        post_visit(node, parent)

def create_parent_array(graph: List[List[int]], root: int = 0) -> List[int]:
    """
    Create an array where each element is the parent of the node.

    Args:
        graph: Adjacency list representation of the tree
        root: Root of the tree

    Returns:
        Array where parent[i] is the parent of node i
    """
    n = len(graph)
    parent = [-1] * n

    def dfs(node, par):
        parent[node] = par
        for neighbor in graph[node]:
            if neighbor != par:
                dfs(neighbor, node)

    dfs(root, -1)
    return parent

def count_components(graph: List[List[int]]) -> int:
    """
    Count the number of connected components in a graph.

    Args:
        graph: Adjacency list representation of the graph

    Returns:
        Number of connected components
    """
    n = len(graph)
    visited = [False] * n
    count = 0

    for i in range(n):
        if not visited[i]:
            count += 1
            dfs(graph, i, visited=visited)

    return count

def find_tree_depth(graph: List[List[int]], root: int = 0) -> List[int]:
    """
    Find the depth of each node in a tree.

    Args:
        graph: Adjacency list representation of the tree
        root: Root of the tree

    Returns:
        Array where depths[i] is the depth of node i
    """
    depths = [-1] * len(graph)
    depths[root] = 0

    queue = deque([root])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if depths[neighbor] == -1:
                depths[neighbor] = depths[node] + 1
                queue.append(neighbor)

    return depths

def find_max_depth(graph: List[List[int]], root: int = 0) -> int:
    """
    Find the maximum depth of a tree.

    Args:
        graph: Adjacency list representation of the tree
        root: Root of the tree

    Returns:
        Maximum depth of the tree
    """
    depths = find_tree_depth(graph, root)
    return max(depths)

def count_leaf_nodes(graph: List[List[int]]) -> Dict[int, int]:
    """
    Count the number of leaf nodes in a graph.

    Args:
        graph: Adjacency list representation of the graph

    Returns:
        Dictionary mapping each node to the count of leaf nodes in its subtree
    """
    n = len(graph)
    leaf_count = [0] * n

    def is_leaf(node, parent):
        # A node is a leaf if it has only one neighbor (its parent)
        # or no neighbors at all (for isolated nodes)
        return len([nb for nb in graph[node] if nb != parent]) == 0

    def dfs(node, parent):
        if is_leaf(node, parent):
            leaf_count[node] = 1
            return 1

        count = 0
        for neighbor in graph[node]:
            if neighbor != parent:
                count += dfs(neighbor, node)

        leaf_count[node] = count
        return count

    for root in range(n):
        if leaf_count[root] == 0:  # Not processed yet
            dfs(root, -1)

    return {i: leaf_count[i] for i in range(n)}

def get_node_degrees(graph: List[List[int]]) -> List[int]:
    """
    Calculate the degree of each node in the graph.

    Args:
        graph: Adjacency list representation of the graph

    Returns:
        List where result[i] is the degree of node i
    """
    return [len(neighbors) for neighbors in graph]

def find_hub_nodes(graph: List[List[int]]) -> List[int]:
    """
    Find nodes with degree greater than 2 (hub nodes in a tree).

    Args:
        graph: Adjacency list representation of the graph

    Returns:
        List of nodes with degree > 2
    """
    return [i for i, neighbors in enumerate(graph) if len(neighbors) > 2]

def find_leaf_nodes(graph: List[List[int]]) -> List[int]:
    """
    Find leaf nodes (nodes with degree 1 in a tree).

    Args:
        graph: Adjacency list representation of the graph

    Returns:
        List of leaf nodes
    """
    return [i for i, neighbors in enumerate(graph) if len(neighbors) == 1]

def create_child_array(parent_array: List[int]) -> List[List[int]]:
    """
    Create a child array from a parent array.

    Args:
        parent_array: Array where parent_array[i] is the parent of node i

    Returns:
        List where result[i] is the list of children of node i
    """
    n = len(parent_array)
    children = [[] for _ in range(n)]

    for i in range(n):
        if parent_array[i] != -1:  # Not the root
            children[parent_array[i]].append(i)

    return children

# Utility functions
def create_2d_array(n: int, m: int, default=0) -> List[List[Any]]:
    """Create a 2D array with default values."""
    return [[default for _ in range(m)] for _ in range(n)]

def make_graph(n: int) -> List[List[int]]:
    """Create an empty graph with n nodes."""
    return [[] for _ in range(n)]

def format_output(value) -> str:
    """Format the output according to the expected format in the test cases."""
    if isinstance(value, float):
        # Check if it's a round number
        if value == int(value):
            return f"{value:.1f}"
        else:
            return str(value)
    return str(value)