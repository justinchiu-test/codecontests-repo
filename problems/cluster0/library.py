"""
Library file for cluster0.
This contains shared code that can be imported by problems in this cluster.
"""
from collections import defaultdict, deque
import sys

# Input parsing utilities
def read_int():
    """Read a single integer from stdin."""
    return int(input())

def read_ints():
    """Read a list of integers from stdin."""
    return list(map(int, input().split()))

def read_int_pair():
    """Read a pair of integers from stdin."""
    return map(int, input().split())

def read_int_tuple(n=2):
    """Read a tuple of n integers from stdin."""
    return tuple(map(int, input().split()))

def read_graph(n, m, one_indexed=True, directed=False):
    """
    Read m edges of a graph with n vertices.
    
    Args:
        n: Number of vertices
        m: Number of edges
        one_indexed: Whether vertices are 1-indexed
        directed: Whether the graph is directed
    
    Returns:
        Tuple of (adjacency list, edges list)
    """
    offset = 1 if one_indexed else 0
    adj_list = [[] for _ in range(n + offset)]
    edges = []
    
    for _ in range(m):
        u, v = read_int_pair()
        edges.append((u, v))
        adj_list[u].append(v)
        if not directed:
            adj_list[v].append(u)
    
    return adj_list, edges

def read_tree(n, one_indexed=True, return_edges=True):
    """
    Read a tree with n vertices (n-1 edges).
    
    Args:
        n: Number of vertices
        one_indexed: Whether vertices are 1-indexed
        return_edges: Whether to return the edges list
    
    Returns:
        Adjacency list representation and optionally the edges list
    """
    return read_graph(n, n-1, one_indexed, directed=False) if return_edges else read_graph(n, n-1, one_indexed, directed=False)[0]

# DFS and BFS implementations
def dfs(graph, start, visited=None):
    """
    Perform DFS traversal of the graph from the start vertex.
    
    Args:
        graph: Adjacency list representation of the graph
        start: Starting vertex
        visited: Set of visited vertices (optional)
    
    Returns:
        List of visited vertices in DFS order
    """
    if visited is None:
        visited = set()
    
    result = []
    
    def dfs_recursive(node):
        visited.add(node)
        result.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_recursive(neighbor)
    
    dfs_recursive(start)
    return result

def bfs(graph, start, visited=None):
    """
    Perform BFS traversal of the graph from the start vertex.
    
    Args:
        graph: Adjacency list representation of the graph
        start: Starting vertex
        visited: Set of visited vertices (optional)
    
    Returns:
        List of visited vertices in BFS order
    """
    if visited is None:
        visited = set()
    
    result = []
    queue = deque([start])
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

def bipartite_check(graph):
    """
    Check if a graph is bipartite and return the coloring.
    
    Args:
        graph: Adjacency list representation of the graph
    
    Returns:
        Tuple (is_bipartite, colors) where:
            is_bipartite: Boolean indicating if the graph is bipartite
            colors: Dict mapping vertices to their color (0 or 1)
    """
    n = len(graph)
    colors = {}
    
    for start in range(1, n):
        if start not in colors:
            colors[start] = 0
            queue = deque([start])
            
            while queue:
                node = queue.popleft()
                
                for neighbor in graph[node]:
                    if neighbor not in colors:
                        colors[neighbor] = 1 - colors[node]
                        queue.append(neighbor)
                    elif colors[neighbor] == colors[node]:
                        return False, colors
    
    return True, colors

# Output formatting utilities
def print_array(arr, sep=" "):
    """Print an array with the given separator."""
    print(sep.join(map(str, arr)))

def yes_no(condition):
    """Return 'YES' if condition is True, 'NO' otherwise."""
    return "YES" if condition else "NO"

def format_float(value, precision=10):
    """Format a float with the specified precision."""
    return f"{value:.{precision}f}"