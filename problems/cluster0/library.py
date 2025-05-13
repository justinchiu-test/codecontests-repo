"""
Library file for cluster0.
This contains shared code that can be imported by problems in this cluster.
"""

import sys
import threading
from collections import defaultdict, deque, Counter

# Input/Output Utilities
read_ints = lambda: map(int, input().split())
read_int = lambda: int(input().strip())
read_int_list = lambda: list(map(int, input().split()))

def read_graph(n, m, directed=False, one_indexed=True):
    """Read m edges for a graph with n nodes"""
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = read_ints()
        if one_indexed:
            u -= 1
            v -= 1
        g[u].append(v)
        if not directed:
            g[v].append(u)
    return g

def read_tree(n, one_indexed=True):
    """Read n-1 edges for a tree with n nodes"""
    return read_graph(n, n-1, directed=False, one_indexed=one_indexed)

def read_node_values(n, one_indexed=False):
    """Read n values associated with nodes"""
    values = read_int_list()
    if one_indexed and len(values) == n + 1:
        return values[1:]  # Skip the 0-th element
    return values

def read_parent_array(n, one_indexed=True):
    """Read parent array for a tree with n nodes
    Returns parents where parents[i] is the parent of node i
    """
    parents = read_int_list()
    if one_indexed:
        # Convert 1-indexed to 0-indexed
        return [p-1 for p in parents]
    return parents

# Graph class
class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]
    
    def add_edge(self, u, v, directed=False, one_indexed=False):
        if one_indexed:
            u -= 1
            v -= 1
        self.adj[u].append(v)
        if not directed:
            self.adj[v].append(u)
    
    def degree(self, v):
        return len(self.adj[v])
    
    def max_degree_node(self):
        return max(range(self.n), key=lambda i: self.degree(i))
    
    def bfs(self, start, visited=None):
        if visited is None:
            visited = [False] * self.n
        queue = deque([start])
        visited[start] = True
        while queue:
            vertex = queue.popleft()
            for neighbor in self.adj[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return visited
    
    def dfs(self, node, parent=-1, visited=None):
        if visited is None:
            visited = [False] * self.n
        visited[node] = True
        for neighbor in self.adj[node]:
            if neighbor != parent and not visited[neighbor]:
                self.dfs(neighbor, node, visited)
        return visited
    
    def count_components(self):
        visited = [False] * self.n
        count = 0
        for i in range(self.n):
            if not visited[i]:
                self.dfs(i, -1, visited)
                count += 1
        return count
    
    def spanning_tree(self, start=0):
        """Construct a spanning tree starting from 'start' using BFS
        Returns list of edges in the spanning tree
        """
        visited = [False] * self.n
        visited[start] = True
        edges = []
        queue = deque([start])
        
        while queue:
            node = queue.popleft()
            for neighbor in self.adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    edges.append((node, neighbor))
                    queue.append(neighbor)
        
        return edges

# Graph Algorithms
def bfs(graph, start, visited=None):
    """BFS traversal of graph starting from vertex 'start'"""
    if visited is None:
        visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return visited

def dfs(graph, node, parent=-1, visited=None):
    """DFS traversal of graph starting from node"""
    if visited is None:
        visited = [False] * len(graph)
    visited[node] = True
    for neighbor in graph[node]:
        if neighbor != parent and not visited[neighbor]:
            dfs(graph, neighbor, node, visited)
    return visited

def dfs_iterative(graph, start, visited=None):
    """Iterative DFS using a stack, useful for avoiding recursion limits"""
    if visited is None:
        visited = [False] * len(graph)
    stack = [start]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            for neighbor in reversed(graph[node]):  # Reversed to match recursive DFS order
                if not visited[neighbor]:
                    stack.append(neighbor)
    return visited

def build_tree_from_parent_array(parents):
    """Convert parent array to adjacency list representation
    parents[i] is the parent of node i
    """
    n = len(parents) + 1  # +1 for the root
    tree = [[] for _ in range(n)]
    for i, parent in enumerate(parents, 1):  # Start from 1 as 0 is the root
        tree[parent].append(i)
        tree[i].append(parent)
    return tree

# Tree Algorithms
def calculate_subtree_sizes(tree, node, parent=-1):
    """Calculate size of subtree rooted at each node"""
    sizes = [1] * len(tree)  # Initialize all sizes to 1 (count self)
    
    def _dfs(v, p):
        for u in tree[v]:
            if u != p:
                _dfs(u, v)
                sizes[v] += sizes[u]
    
    _dfs(node, parent)
    return sizes

def calculate_depths(tree, root):
    """Calculate depth of each node in tree"""
    depths = [0] * len(tree)
    
    def _dfs(node, parent, depth):
        depths[node] = depth
        for child in tree[node]:
            if child != parent:
                _dfs(child, node, depth + 1)
    
    _dfs(root, -1, 0)
    return depths

def find_leaf_nodes(tree, root=0):
    """Find all leaf nodes in tree"""
    leaves = []
    for i in range(len(tree)):
        # A leaf node has only one connection (to its parent)
        # except the root which might have only one child
        if len(tree[i]) == 1 and i != root:
            leaves.append(i)
    return leaves

def count_nodes_by_level(tree, root=0):
    """Count nodes at each level of the tree"""
    depths = calculate_depths(tree, root)
    return Counter(depths)

def count_odd_level_nodes(tree, root=0):
    """Count nodes at each level and return sum of odd counts"""
    level_counts = count_nodes_by_level(tree, root)
    return sum(count & 1 for count in level_counts.values())

def is_bipartite(graph):
    """Check if a graph is bipartite using BFS coloring"""
    n = len(graph)
    color = [-1] * n  # -1: uncolored, 0: first color, 1: second color
    
    for start in range(n):
        if color[start] == -1:
            color[start] = 0
            queue = deque([start])
            
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]  # Opposite color
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False  # Same color for adjacent nodes, not bipartite
    
    return True

def bipartite_sets(graph):
    """Split graph into two sets if it's bipartite
    Returns (set0, set1) or None if not bipartite
    """
    n = len(graph)
    color = [-1] * n  # -1: uncolored, 0: first color, 1: second color
    
    for start in range(n):
        if color[start] == -1:
            color[start] = 0
            queue = deque([start])
            
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]  # Opposite color
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return None  # Not bipartite
    
    set0 = [i for i in range(n) if color[i] == 0]
    set1 = [i for i in range(n) if color[i] == 1]
    return (set0, set1)

# Node class for tree problems
class Node:
    def __init__(self, id=None, parent=None):
        self.id = id
        self.parent = parent
        self.children = []
        self.data = {}  # Additional data like depth, size, etc.

    def add_child(self, child):
        self.children.append(child)

# Utility Functions
def setup_large_recursion():
    """Set up for large recursion"""
    sys.setrecursionlimit(300000)
    threading.stack_size(10 ** 8)

def to_zero_index(index):
    """Convert 1-based index to 0-based"""
    return index - 1

def to_one_index(index):
    """Convert 0-based index to 1-based"""
    return index + 1

def run_with_large_stack(func):
    """Run function with large stack size"""
    threading.stack_size(10 ** 8)
    thread = threading.Thread(target=func)
    thread.start()
    thread.join()