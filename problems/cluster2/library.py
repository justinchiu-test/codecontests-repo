"""
Library file for cluster2.
This contains shared code that can be imported by problems in this cluster.
"""

from collections import deque
from typing import Dict, List, Set, Callable, TypeVar, Generic, Iterable, Optional, Tuple, Union


# Graph Data Structures
class Graph:
    """Base class for graph representation with adjacency list."""
    def __init__(self):
        self._alist = {}

    def add_vertex(self, vertex):
        """Add a vertex to the graph if it doesn't exist."""
        if vertex not in self._alist:
            self._alist[vertex] = set()

    def add_edge(self, source, destination):
        """Add a directed edge from source to destination."""
        self.add_vertex(source)
        self.add_vertex(destination)
        self._alist[source].add(destination)

    def is_edge(self, source, destination):
        """Check if there is an edge from source to destination."""
        return (self.is_vertex(source) and
                destination in self._alist[source])

    def is_vertex(self, vertex):
        """Check if a vertex exists in the graph."""
        return vertex in self._alist

    def neighbors(self, vertex):
        """Return the neighbors of a vertex."""
        return self._alist[vertex]

    def vertices(self):
        """Return all vertices in the graph."""
        return self._alist.keys()


class UndirectedGraph(Graph):
    """Undirected graph representation where each edge goes both ways."""
    def add_edge(self, a, b):
        """Add an undirected edge between a and b."""
        super().add_edge(a, b)
        super().add_edge(b, a)


# Graph Algorithms
def dfs(graph: Graph, start_vertex, visited=None):
    """
    Depth-first search traversal of a graph from a starting vertex.

    Args:
        graph: A Graph instance
        start_vertex: The vertex to start traversal from
        visited: Optional dictionary to track visited vertices

    Returns:
        A dictionary mapping each reached vertex to its parent vertex
    """
    if visited is None:
        visited = {}

    def do_dfs(curr, prev):
        if curr in visited:
            return
        visited[curr] = prev
        for neighbor in graph.neighbors(curr):
            do_dfs(neighbor, curr)

    do_dfs(start_vertex, start_vertex)
    return visited


def dfs_cycle_detection(graph: Graph) -> bool:
    """
    Detect if there is a cycle in the graph using DFS.

    Args:
        graph: A Graph instance

    Returns:
        True if a cycle is detected, False otherwise
    """
    visited = {}
    for vertex in graph.vertices():
        visited[vertex] = False

    has_cycle = [False]  # Use a list to allow modification in nested function

    def dfs_visit(curr, prev):
        if has_cycle[0]:
            return

        visited[curr] = True

        for neighbor in graph.neighbors(curr):
            if visited[neighbor] and neighbor != prev:
                has_cycle[0] = True
                return
            if not visited[neighbor]:
                dfs_visit(neighbor, curr)

    # Try starting DFS from each unvisited vertex
    for vertex in graph.vertices():
        if not visited[vertex]:
            dfs_visit(vertex, vertex)
        if has_cycle[0]:
            break

    return has_cycle[0]


def bfs(graph: Graph, start_vertex):
    """
    Breadth-first search traversal of a graph from a starting vertex.

    Args:
        graph: A Graph instance
        start_vertex: The vertex to start traversal from

    Returns:
        A dictionary mapping each reached vertex to its distance from start_vertex
    """
    visited = {start_vertex: True}
    queue = deque([start_vertex])
    distances = {start_vertex: 0}

    while queue:
        current = queue.popleft()
        for neighbor in graph.neighbors(current):
            if neighbor not in visited:
                visited[neighbor] = True
                queue.append(neighbor)
                distances[neighbor] = distances[current] + 1

    return distances


def count_connected_components(graph: Graph) -> int:
    """
    Count the number of connected components in the graph.

    Args:
        graph: A Graph instance

    Returns:
        The number of connected components
    """
    visited = {}
    for vertex in graph.vertices():
        visited[vertex] = False

    component_count = 0

    for vertex in graph.vertices():
        if not visited[vertex]:
            component_count += 1
            # Mark all vertices in this component as visited
            dfs(graph, vertex, visited)

    return component_count


# Grid-based Graph Utilities
def grid_to_graph(grid: List[List], connect_same=True):
    """
    Convert a 2D grid to a graph. By default, connects cells with the same value.

    Args:
        grid: A 2D list representing the grid
        connect_same: If True, only connect cells with the same value

    Returns:
        An UndirectedGraph representing the grid connections
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    graph = UndirectedGraph()

    # Add all vertices
    for i in range(rows):
        for j in range(cols):
            vertex_id = i * cols + j
            graph.add_vertex(vertex_id)

    # Connect vertices
    for i in range(rows):
        for j in range(cols):
            vertex_id = i * cols + j

            # Connect right
            if j < cols - 1:
                if not connect_same or grid[i][j] == grid[i][j+1]:
                    graph.add_edge(vertex_id, vertex_id + 1)

            # Connect down
            if i < rows - 1:
                if not connect_same or grid[i][j] == grid[i+1][j]:
                    graph.add_edge(vertex_id, vertex_id + cols)

    return graph


# Input/Output Utilities
def read_grid(rows: int, cols: Optional[int] = None):
    """
    Read a grid from standard input.

    Args:
        rows: Number of rows in the grid
        cols: Optional number of columns (inferred from first row if None)

    Returns:
        A 2D list representing the grid
    """
    grid = []
    for _ in range(rows):
        row = input().strip()
        grid.append(list(row))

    return grid

def read_int() -> int:
    """Read a single integer from standard input."""
    return int(input().strip())

def read_ints() -> List[int]:
    """Read space-separated integers as a list."""
    return list(map(int, input().split()))

def read_int_tuple() -> Tuple[int, ...]:
    """Read space-separated integers as a tuple."""
    return tuple(map(int, input().split()))

def read_int_grid(rows: int, cols: Optional[int] = None) -> List[List[int]]:
    """Read a grid of integers from standard input."""
    grid: List[List[int]] = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        grid.append(row)
    return grid

def read_char_grid(rows: int, cols: Optional[int] = None) -> List[List[str]]:
    """Read a grid of characters from standard input."""
    grid: List[List[str]] = []
    for _ in range(rows):
        line = input().rstrip('\n')
        grid.append(list(line))
    return grid

def read_edges(m: int, one_indexed: bool = True) -> List[Tuple[int, int]]:
    """Read m edges (u, v) from standard input."""
    edges: List[Tuple[int, int]] = []
    for _ in range(m):
        u, v = map(int, input().split())
        if one_indexed:
            u -= 1; v -= 1
        edges.append((u, v))
    return edges

def read_weighted_edges(m: int, one_indexed: bool = True) -> List[Tuple[int, int, int]]:
    """Read m weighted edges (u, v, w) from standard input."""
    edges: List[Tuple[int, int, int]] = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        if one_indexed:
            u -= 1; v -= 1
        edges.append((u, v, w))
    return edges


def read_graph(n: int, m: int, directed: bool = False, one_indexed: bool = True):
    """
    Read a graph from standard input.

    Args:
        n: Number of vertices
        m: Number of edges
        directed: If True, creates a directed graph, otherwise undirected
        one_indexed: If True, input vertex IDs start from 1, otherwise 0

    Returns:
        A Graph or UndirectedGraph instance
    """
    graph = Graph() if directed else UndirectedGraph()

    # Initialize vertices
    for i in range(n):
        graph.add_vertex(i)

    # Read edges
    for _ in range(m):
        u, v = map(int, input().split())
        if one_indexed:
            u -= 1
            v -= 1
        graph.add_edge(u, v)

    return graph


# Disjoint Set (Union-Find) data structure
class DisjointSet:
    """Disjoint Set (Union-Find) data structure with path compression and union by rank."""

    def __init__(self, n: int):
        """Initialize a disjoint set with n elements."""
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n  # Number of disjoint sets

    def find(self, x: int) -> int:
        """Find the representative (root) of the set containing x."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """
        Union the sets containing x and y.

        Returns:
            True if x and y were in different sets, False otherwise
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        self.count -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        """Check if x and y are in the same set."""
        return self.find(x) == self.find(y)
