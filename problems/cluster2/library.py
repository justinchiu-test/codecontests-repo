"""
Library file for cluster2.
This contains shared code that can be imported by problems in this cluster.
"""
from collections import defaultdict, deque
import sys

# Input/Output helpers
def read_int():
    """Read a single integer from stdin."""
    return int(input())

def read_ints():
    """Read multiple integers from a single line."""
    return list(map(int, input().split()))

def read_int_pairs(n):
    """Read n pairs of integers from n lines."""
    return [list(map(int, input().split())) for _ in range(n)]

def read_grid(n):
    """Read n lines to form a grid."""
    return [input() for _ in range(n)]

def yes_no(condition, uppercase=True):
    """
    Return YES/NO or Yes/No based on condition.
    
    Args:
        condition: Boolean value
        uppercase: If True, return YES/NO, otherwise Yes/No
    
    Returns:
        String YES/NO or Yes/No
    """
    if uppercase:
        return "YES" if condition else "NO"
    else:
        return "Yes" if condition else "No"

# Graph representation
def create_graph(n, edges=None, directed=False, one_indexed=True):
    """
    Create an adjacency list representation of a graph.
    
    Args:
        n: Number of vertices
        edges: List of edges as pairs [u, v]
        directed: Whether the graph is directed
        one_indexed: Whether vertices are 1-indexed in the input
        
    Returns:
        Adjacency list as a list of lists
    """
    graph = [[] for _ in range(n)]
    
    if edges:
        for u, v in edges:
            if one_indexed:
                u -= 1
                v -= 1
            graph[u].append(v)
            if not directed:
                graph[v].append(u)
                
    return graph

# Graph algorithms
def dfs(graph, start, visited=None):
    """
    Perform DFS traversal on a graph from start vertex.
    
    Args:
        graph: Adjacency list representation
        start: Starting vertex
        visited: Optional visited array
        
    Returns:
        List of visited vertices
    """
    if visited is None:
        visited = [False] * len(graph)
    
    visited[start] = True
    result = [start]
    
    for neighbor in graph[start]:
        if not visited[neighbor]:
            result.extend(dfs(graph, neighbor, visited))
            
    return result

def dfs_cycle(graph, start, parent=-1, visited=None):
    """
    DFS to detect cycles in undirected graph.
    
    Args:
        graph: Adjacency list
        start: Current vertex
        parent: Parent vertex
        visited: Visited array
    
    Returns:
        True if cycle exists, False otherwise
    """
    if visited is None:
        visited = [False] * len(graph)
    
    visited[start] = True
    
    for neighbor in graph[start]:
        if not visited[neighbor]:
            if dfs_cycle(graph, neighbor, start, visited):
                return True
        elif neighbor != parent:
            return True
    
    return False

def bfs(graph, start):
    """
    Perform BFS traversal on a graph from start vertex.
    
    Args:
        graph: Adjacency list representation
        start: Starting vertex
        
    Returns:
        List of visited vertices in BFS order
    """
    n = len(graph)
    visited = [False] * n
    queue = deque([start])
    visited[start] = True
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                
    return result

def find_connected_components(graph):
    """
    Find all connected components in an undirected graph.
    
    Args:
        graph: Adjacency list representation
        
    Returns:
        List of connected components (each component is a list of vertices)
    """
    n = len(graph)
    visited = [False] * n
    components = []
    
    for i in range(n):
        if not visited[i]:
            component = []
            
            # Use BFS to find all vertices in this component
            queue = deque([i])
            visited[i] = True
            
            while queue:
                vertex = queue.popleft()
                component.append(vertex)
                
                for neighbor in graph[vertex]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            
            components.append(component)
    
    return components

def count_connected_components(graph):
    """Count the number of connected components in an undirected graph."""
    n = len(graph)
    visited = [False] * n
    count = 0
    
    for i in range(n):
        if not visited[i]:
            count += 1
            
            # Use BFS to mark all vertices in this component
            queue = deque([i])
            visited[i] = True
            
            while queue:
                vertex = queue.popleft()
                
                for neighbor in graph[vertex]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
    
    return count

def has_cycle_undirected(graph):
    """
    Check if an undirected graph has a cycle.
    
    Args:
        graph: Adjacency list representation
        
    Returns:
        True if cycle exists, False otherwise
    """
    n = len(graph)
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            if dfs_cycle(graph, i, -1, visited):
                return True
                
    return False

def is_tree(graph):
    """
    Check if a graph is a tree (connected and acyclic).
    
    Args:
        graph: Adjacency list representation
    
    Returns:
        True if the graph is a tree, False otherwise
    """
    n = len(graph)
    
    # A tree has exactly n-1 edges
    edge_count = sum(len(neighbors) for neighbors in graph) // 2
    if edge_count != n - 1:
        return False
    
    # A tree must be connected (single component)
    return count_connected_components(graph) == 1

# Disjoint Set Union (Union-Find)
class DSU:
    """Disjoint Set Union (Union-Find) data structure."""
    
    def __init__(self, n):
        """Initialize DSU with n elements."""
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
        self.components = n
        
    def find(self, x):
        """Find the root of the set containing x."""
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
        
    def union(self, x, y):
        """Union the sets containing x and y."""
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False  # Already in the same set
            
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
            self.size[root_x] += self.size[root_y]
            
        self.components -= 1
        return True
        
    def same_set(self, x, y):
        """Check if x and y are in the same set."""
        return self.find(x) == self.find(y)
        
    def get_size(self, x):
        """Get the size of the set containing x."""
        return self.size[self.find(x)]
        
    def get_components_count(self):
        """Get the number of components."""
        return self.components

# Undirected graph class
class UndirectedGraph:
    """Class representing an undirected graph."""
    
    def __init__(self, n=0):
        """Initialize an empty graph with n vertices."""
        self.graph = [[] for _ in range(n)]
        self.n = n
        
    def add_vertex(self):
        """Add a new vertex to the graph."""
        self.graph.append([])
        self.n += 1
        return self.n - 1
        
    def add_edge(self, u, v):
        """Add an undirected edge between u and v."""
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def remove_edge(self, u, v):
        """Remove the edge between u and v if it exists."""
        if v in self.graph[u]:
            self.graph[u].remove(v)
        if u in self.graph[v]:
            self.graph[v].remove(u)
            
    def has_edge(self, u, v):
        """Check if there is an edge between u and v."""
        return v in self.graph[u]
        
    def neighbors(self, u):
        """Get all neighbors of vertex u."""
        return self.graph[u]
        
    def vertices(self):
        """Get all vertices of the graph."""
        return range(self.n)
        
    def bfs(self, start):
        """Perform BFS from start vertex."""
        return bfs(self.graph, start)
        
    def dfs(self, start):
        """Perform DFS from start vertex."""
        return dfs(self.graph, start)
        
    def find_connected_components(self):
        """Find all connected components."""
        return find_connected_components(self.graph)
        
    def count_connected_components(self):
        """Count the number of connected components."""
        return count_connected_components(self.graph)
        
    def has_cycle(self):
        """Check if the graph has a cycle."""
        return has_cycle_undirected(self.graph)
    
    def is_tree(self):
        """Check if the graph is a tree."""
        return is_tree(self.graph)