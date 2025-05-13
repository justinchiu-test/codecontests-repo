"""
Library file for cluster2.
This contains shared code that can be imported by problems in this cluster.
"""
from collections import defaultdict, deque
from typing import List, Set, Dict, Tuple, Optional, Callable, Any, Union, Iterator


class DSU:
    """Disjoint Set Union (DSU) implementation with path compression and union by rank."""
    
    def __init__(self, n: int):
        """Initialize a DSU with n elements.
        
        Args:
            n: Number of elements (0-indexed)
        """
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
        self.count = n  # Number of disjoint sets
    
    def find(self, x: int) -> int:
        """Find the representative of the set containing x.
        
        Args:
            x: Element to find
            
        Returns:
            The representative of the set containing x
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x: int, y: int) -> bool:
        """Union the sets containing x and y.
        
        Args:
            x: First element
            y: Second element
            
        Returns:
            True if x and y were in different sets before the union, False otherwise
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1
        
        self.count -= 1
        return True
    
    def is_same_set(self, x: int, y: int) -> bool:
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
            x: Element
            
        Returns:
            Size of the set containing x
        """
        return self.size[self.find(x)]
    
    def count_sets(self) -> int:
        """Count the number of disjoint sets.
        
        Returns:
            Number of disjoint sets
        """
        return self.count
    
    def get_all_sets(self) -> Dict[int, List[int]]:
        """Get all disjoint sets.
        
        Returns:
            Dictionary mapping each representative to its set members
        """
        sets = defaultdict(list)
        for i in range(len(self.parent)):
            sets[self.find(i)].append(i)
        return sets


class Graph:
    """Graph representation with support for traversal algorithms."""
    
    def __init__(self, n: int, directed: bool = False, weighted: bool = False):
        """Initialize a graph with n vertices.
        
        Args:
            n: Number of vertices (0-indexed)
            directed: Whether the graph is directed
            weighted: Whether the graph has weighted edges
        """
        self.n = n
        self.directed = directed
        self.weighted = weighted
        self.adj = [[] for _ in range(n)]  # Adjacency list
    
    def add_edge(self, u: int, v: int, weight: int = 1) -> None:
        """Add an edge from u to v.
        
        Args:
            u: Source vertex
            v: Destination vertex
            weight: Edge weight (only used if self.weighted is True)
        """
        if self.weighted:
            self.adj[u].append((v, weight))
            if not self.directed:
                self.adj[v].append((u, weight))
        else:
            self.adj[u].append(v)
            if not self.directed:
                self.adj[v].append(u)
    
    def neighbors(self, u: int) -> Iterator[int]:
        """Get all neighbors of a vertex.
        
        Args:
            u: Vertex
            
        Returns:
            Iterator over neighbors
        """
        for v in self.adj[u]:
            if self.weighted:
                yield v[0]  # Extract vertex from (vertex, weight) pair
            else:
                yield v
    
    def dfs(self, start: int, visit_fn: Optional[Callable[[int], None]] = None) -> List[bool]:
        """Perform DFS traversal starting from the given vertex.
        
        Args:
            start: Starting vertex
            visit_fn: Function to call when visiting a vertex
            
        Returns:
            List indicating which vertices were visited
        """
        visited = [False] * self.n
        
        def _dfs(u: int) -> None:
            visited[u] = True
            if visit_fn:
                visit_fn(u)
            
            for v in self.neighbors(u):
                if not visited[v]:
                    _dfs(v)
        
        _dfs(start)
        return visited
    
    def dfs_iterative(self, start: int, visit_fn: Optional[Callable[[int], None]] = None) -> List[bool]:
        """Perform iterative DFS traversal starting from the given vertex.
        
        Args:
            start: Starting vertex
            visit_fn: Function to call when visiting a vertex
            
        Returns:
            List indicating which vertices were visited
        """
        visited = [False] * self.n
        stack = [start]
        
        while stack:
            u = stack.pop()
            if not visited[u]:
                visited[u] = True
                if visit_fn:
                    visit_fn(u)
                
                for v in self.neighbors(u):
                    if not visited[v]:
                        stack.append(v)
        
        return visited
    
    def bfs(self, start: int, visit_fn: Optional[Callable[[int], None]] = None) -> List[bool]:
        """Perform BFS traversal starting from the given vertex.
        
        Args:
            start: Starting vertex
            visit_fn: Function to call when visiting a vertex
            
        Returns:
            List indicating which vertices were visited
        """
        visited = [False] * self.n
        queue = deque([start])
        visited[start] = True
        if visit_fn:
            visit_fn(start)
        
        while queue:
            u = queue.popleft()
            
            for v in self.neighbors(u):
                if not visited[v]:
                    visited[v] = True
                    if visit_fn:
                        visit_fn(v)
                    queue.append(v)
        
        return visited
    
    def find_connected_components(self) -> List[List[int]]:
        """Find all connected components in the graph.
        
        Returns:
            List of connected components, where each component is a list of vertices
        """
        visited = [False] * self.n
        components = []
        
        for i in range(self.n):
            if not visited[i]:
                component = []
                
                def visit_fn(u: int) -> None:
                    component.append(u)
                
                stack = [i]
                visited[i] = True
                component.append(i)
                
                while stack:
                    u = stack.pop()
                    for v in self.neighbors(u):
                        if not visited[v]:
                            visited[v] = True
                            component.append(v)
                            stack.append(v)
                
                components.append(component)
        
        return components
    
    def count_connected_components(self) -> int:
        """Count the number of connected components in the graph.
        
        Returns:
            Number of connected components
        """
        visited = [False] * self.n
        count = 0
        
        for i in range(self.n):
            if not visited[i]:
                count += 1
                stack = [i]
                visited[i] = True
                
                while stack:
                    u = stack.pop()
                    for v in self.neighbors(u):
                        if not visited[v]:
                            visited[v] = True
                            stack.append(v)
        
        return count
    
    def has_cycle_directed(self) -> bool:
        """Check if the directed graph has a cycle.
        
        Returns:
            True if the graph has a cycle, False otherwise
        """
        visited = [False] * self.n
        rec_stack = [False] * self.n
        
        for i in range(self.n):
            if not visited[i]:
                if self._has_cycle_directed_util(i, visited, rec_stack):
                    return True
        
        return False
    
    def _has_cycle_directed_util(self, u: int, visited: List[bool], rec_stack: List[bool]) -> bool:
        """Helper function for has_cycle_directed.
        
        Args:
            u: Current vertex
            visited: List indicating which vertices were visited
            rec_stack: List indicating which vertices are in the current recursion stack
            
        Returns:
            True if a cycle is found, False otherwise
        """
        visited[u] = True
        rec_stack[u] = True
        
        for v in self.neighbors(u):
            if not visited[v]:
                if self._has_cycle_directed_util(v, visited, rec_stack):
                    return True
            elif rec_stack[v]:
                return True
        
        rec_stack[u] = False
        return False
    
    def has_cycle_undirected(self) -> bool:
        """Check if the undirected graph has a cycle.
        
        Returns:
            True if the graph has a cycle, False otherwise
        """
        visited = [False] * self.n
        
        for i in range(self.n):
            if not visited[i]:
                if self._has_cycle_undirected_util(i, -1, visited):
                    return True
        
        return False
    
    def _has_cycle_undirected_util(self, u: int, parent: int, visited: List[bool]) -> bool:
        """Helper function for has_cycle_undirected.
        
        Args:
            u: Current vertex
            parent: Parent vertex
            visited: List indicating which vertices were visited
            
        Returns:
            True if a cycle is found, False otherwise
        """
        visited[u] = True
        
        for v in self.neighbors(u):
            if not visited[v]:
                if self._has_cycle_undirected_util(v, u, visited):
                    return True
            elif v != parent:
                return True
        
        return False
    
    def has_cycle(self) -> bool:
        """Check if the graph has a cycle.
        
        Returns:
            True if the graph has a cycle, False otherwise
        """
        if self.directed:
            return self.has_cycle_directed()
        else:
            return self.has_cycle_undirected()
    
    def shortest_path(self, start: int, end: int) -> Optional[List[int]]:
        """Find the shortest path from start to end using BFS (unweighted graphs).
        
        Args:
            start: Starting vertex
            end: Ending vertex
            
        Returns:
            List representing the shortest path, or None if no path exists
        """
        if start == end:
            return [start]
        
        visited = [False] * self.n
        parent = [-1] * self.n
        queue = deque([start])
        visited[start] = True
        
        while queue and not visited[end]:
            u = queue.popleft()
            
            for v in self.neighbors(u):
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
        
        if not visited[end]:
            return None
        
        # Reconstruct path
        path = []
        current = end
        while current != -1:
            path.append(current)
            current = parent[current]
        
        return list(reversed(path))
    
    def is_tree(self) -> bool:
        """Check if the graph is a tree (connected and acyclic).
        
        Returns:
            True if the graph is a tree, False otherwise
        """
        # A tree has n-1 edges and is connected
        edge_count = sum(len(adj) for adj in self.adj)
        if self.directed:
            return False  # Trees are undirected by definition
        else:
            edge_count //= 2  # For undirected graph, each edge is counted twice
        
        # Check if the graph has n-1 edges
        if edge_count != self.n - 1:
            return False
        
        # Check if the graph is connected (has exactly one connected component)
        visited = self.dfs(0)
        return all(visited)
    
    def count_degrees(self) -> List[int]:
        """Count the degree of each vertex.
        
        Returns:
            List of degrees for each vertex
        """
        return [len(adj) for adj in self.adj]
    
    def is_cyclic_component(self, component: List[int]) -> bool:
        """Check if a component is cyclic (all vertices have degree 2).
        
        Args:
            component: List of vertices in the component
            
        Returns:
            True if the component is cyclic, False otherwise
        """
        if not component:
            return False
        
        # Check if all vertices in the component have degree 2
        for vertex in component:
            if len(self.adj[vertex]) != 2:
                return False
        
        return True
    
    def is_bipartite(self) -> bool:
        """Check if the graph is bipartite (can be colored with 2 colors).
        
        Returns:
            True if the graph is bipartite, False otherwise
        """
        # Initialize all vertices as uncolored (-1)
        color = [-1] * self.n
        
        # BFS coloring for each component
        for start in range(self.n):
            if color[start] == -1:
                # Start with color 0
                color[start] = 0
                queue = deque([start])
                
                while queue:
                    u = queue.popleft()
                    
                    for v in self.neighbors(u):
                        # If uncolored, assign opposite color
                        if color[v] == -1:
                            color[v] = 1 - color[u]
                            queue.append(v)
                        # If already colored with same color as parent, not bipartite
                        elif color[v] == color[u]:
                            return False
        
        return True
    
    def find_odd_length_cycles(self) -> List[List[int]]:
        """Find all odd-length cycles in the graph.
        
        Returns:
            List of cycles, where each cycle is a list of vertices
        """
        cycles = []
        visited = [-1] * self.n  # -1: unvisited, 0: color 0, 1: color 1
        
        def dfs_find_odd_cycles(u, parent, color):
            visited[u] = color
            
            for v in self.neighbors(u):
                if v == parent:
                    continue
                
                if visited[v] == -1:
                    dfs_find_odd_cycles(v, u, 1 - color)
                elif visited[v] == color:
                    # Found an odd-length cycle (same color)
                    cycle = []
                    # Reconstruct the cycle (not implemented for simplicity)
                    cycles.append(cycle)
        
        for i in range(self.n):
            if visited[i] == -1:
                dfs_find_odd_cycles(i, -1, 0)
        
        return cycles
    
    def count_odd_length_cycles(self) -> int:
        """Count the number of vertices in odd-length cycles.
        
        Returns:
            Number of vertices in odd-length cycles
        """
        count = 0
        visited = defaultdict(int)  # 0: unvisited, 1: visiting, 2: visited
        
        def dfs_count_odd_cycles(u, parent, cycle_length):
            visited[u] = 1
            result = 0
            
            for v in self.neighbors(u):
                if v == parent:
                    continue
                
                if visited[v] == 0:
                    # Continue DFS
                    result += dfs_count_odd_cycles(v, u, cycle_length + 1)
                elif visited[v] == 1:
                    # Found a back edge (cycle)
                    # If odd cycle length, count one vertex
                    if (cycle_length + 1) % 2 == 1:
                        result += 1
            
            visited[u] = 2  # Mark as processed
            return result
        
        # Run DFS from each unvisited vertex
        for i in range(self.n):
            if visited[i] == 0:
                count += dfs_count_odd_cycles(i, -1, 0)
        
        return count


class GridGraph:
    """Grid graph representation for 2D grid problems."""
    
    def __init__(self, grid: List[str], diagonal: bool = False):
        """Initialize a grid graph.
        
        Args:
            grid: 2D grid
            diagonal: Whether to include diagonal neighbors
        """
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.diagonal = diagonal
    
    def get_vertex_id(self, r: int, c: int) -> int:
        """Convert 2D coordinates to vertex ID.
        
        Args:
            r: Row
            c: Column
            
        Returns:
            Vertex ID
        """
        return r * self.cols + c
    
    def get_coordinates(self, vertex_id: int) -> Tuple[int, int]:
        """Convert vertex ID to 2D coordinates.
        
        Args:
            vertex_id: Vertex ID
            
        Returns:
            (row, column)
        """
        return divmod(vertex_id, self.cols)
    
    def is_valid(self, r: int, c: int) -> bool:
        """Check if coordinates are valid.
        
        Args:
            r: Row
            c: Column
            
        Returns:
            True if coordinates are valid, False otherwise
        """
        return 0 <= r < self.rows and 0 <= c < self.cols
    
    def get_neighbors(self, r: int, c: int) -> List[Tuple[int, int]]:
        """Get all valid neighbors of a cell.
        
        Args:
            r: Row
            c: Column
            
        Returns:
            List of (row, column) tuples for valid neighbors
        """
        neighbors = []
        
        # 4-directional neighbors
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if self.is_valid(nr, nc):
                neighbors.append((nr, nc))
        
        # Diagonal neighbors
        if self.diagonal:
            for dr, dc in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                nr, nc = r + dr, c + dc
                if self.is_valid(nr, nc):
                    neighbors.append((nr, nc))
        
        return neighbors
    
    def to_graph(self, connect_same_value: bool = False) -> Graph:
        """Convert grid to a Graph object.
        
        Args:
            connect_same_value: Whether to only connect cells with the same value
            
        Returns:
            Graph object
        """
        graph = Graph(self.rows * self.cols)
        
        for r in range(self.rows):
            for c in range(self.cols):
                curr_id = self.get_vertex_id(r, c)
                curr_value = self.grid[r][c]
                
                for nr, nc in self.get_neighbors(r, c):
                    neighbor_id = self.get_vertex_id(nr, nc)
                    
                    if connect_same_value:
                        # Only connect if they have the same value
                        if self.grid[nr][nc] == curr_value:
                            graph.add_edge(curr_id, neighbor_id)
                    else:
                        # Connect all valid neighbors
                        graph.add_edge(curr_id, neighbor_id)
        
        return graph
    
    def dfs(self, start_r: int, start_c: int, visit_fn: Optional[Callable[[int, int], None]] = None) -> List[List[bool]]:
        """Perform DFS traversal on the grid.
        
        Args:
            start_r: Starting row
            start_c: Starting column
            visit_fn: Function to call when visiting a cell, takes (row, col) as parameters
            
        Returns:
            2D grid of booleans indicating which cells were visited
        """
        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        
        def _dfs(r: int, c: int) -> None:
            visited[r][c] = True
            if visit_fn:
                visit_fn(r, c)
            
            for nr, nc in self.get_neighbors(r, c):
                if not visited[nr][nc]:
                    _dfs(nr, nc)
        
        _dfs(start_r, start_c)
        return visited
    
    def find_connected_components(self, connect_same_value: bool = True) -> List[List[Tuple[int, int]]]:
        """Find all connected components in the grid.
        
        Args:
            connect_same_value: Whether to only connect cells with the same value
            
        Returns:
            List of connected components, where each component is a list of (row, column) tuples
        """
        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        components = []
        
        for r in range(self.rows):
            for c in range(self.cols):
                if not visited[r][c]:
                    component = []
                    value = self.grid[r][c]
                    
                    # BFS to find all cells in the component
                    queue = deque([(r, c)])
                    visited[r][c] = True
                    component.append((r, c))
                    
                    while queue:
                        curr_r, curr_c = queue.popleft()
                        
                        for nr, nc in self.get_neighbors(curr_r, curr_c):
                            if not visited[nr][nc]:
                                if not connect_same_value or self.grid[nr][nc] == value:
                                    visited[nr][nc] = True
                                    component.append((nr, nc))
                                    queue.append((nr, nc))
                    
                    components.append(component)
        
        return components
    
    def count_connected_components(self, connect_same_value: bool = True) -> int:
        """Count the number of connected components in the grid.
        
        Args:
            connect_same_value: Whether to only connect cells with the same value
            
        Returns:
            Number of connected components
        """
        return len(self.find_connected_components(connect_same_value))


def read_graph(n: int, m: int, directed: bool = False, weighted: bool = False, one_indexed: bool = True) -> Graph:
    """Read a graph from standard input.
    
    Args:
        n: Number of vertices
        m: Number of edges
        directed: Whether the graph is directed
        weighted: Whether the graph has weighted edges
        one_indexed: Whether the vertices are 1-indexed
        
    Returns:
        Graph object
    """
    g = Graph(n, directed, weighted)
    offset = 1 if one_indexed else 0
    
    for _ in range(m):
        if weighted:
            args = list(map(int, input().split()))
            u, v = args[0], args[1]
            w = args[2] if len(args) > 2 else 1
            
            if one_indexed:
                u -= offset
                v -= offset
            g.add_edge(u, v, w)
        else:
            u, v = map(int, input().split())
            if one_indexed:
                u -= offset
                v -= offset
            g.add_edge(u, v)
    
    return g


def read_grid() -> List[str]:
    """Read a grid from standard input.
    
    Returns:
        2D grid as a list of strings
    """
    rows, cols = map(int, input().split())
    grid = []
    
    for _ in range(rows):
        grid.append(input())
    
    return grid


def check_cycle_undirected(n: int, edges: List[Tuple[int, int]]) -> bool:
    """Check if an undirected graph has a cycle using DSU.
    
    Args:
        n: Number of vertices
        edges: List of edges (u, v)
        
    Returns:
        True if the graph has a cycle, False otherwise
    """
    dsu = DSU(n)
    
    for u, v in edges:
        if dsu.is_same_set(u, v):
            return True
        dsu.union(u, v)
    
    return False


def dfs(graph: List[List[int]], start: int, visited: Optional[List[bool]] = None) -> List[bool]:
    """Simple DFS function for adjacency list representation.
    
    Args:
        graph: Adjacency list representation of the graph
        start: Starting vertex
        visited: List indicating which vertices were visited (initialized if None)
        
    Returns:
        List indicating which vertices were visited
    """
    if visited is None:
        visited = [False] * len(graph)
    
    stack = [start]
    if not visited[start]:
        visited[start] = True
    
    while stack:
        u = stack.pop()
        
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
    
    return visited


def bfs(graph: List[List[int]], start: int) -> List[bool]:
    """Simple BFS function for adjacency list representation.
    
    Args:
        graph: Adjacency list representation of the graph
        start: Starting vertex
        
    Returns:
        List indicating which vertices were visited
    """
    n = len(graph)
    visited = [False] * n
    queue = deque([start])
    visited[start] = True
    
    while queue:
        u = queue.popleft()
        
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
    
    return visited


def find_connected_components(graph: List[List[int]]) -> List[List[int]]:
    """Find all connected components in the graph.
    
    Args:
        graph: Adjacency list representation of the graph
        
    Returns:
        List of connected components, where each component is a list of vertices
    """
    n = len(graph)
    visited = [False] * n
    components = []
    
    for i in range(n):
        if not visited[i]:
            component = []
            
            stack = [i]
            visited[i] = True
            component.append(i)
            
            while stack:
                u = stack.pop()
                for v in graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        component.append(v)
                        stack.append(v)
            
            components.append(component)
    
    return components


def count_connected_components(graph: List[List[int]]) -> int:
    """Count the number of connected components in the graph.
    
    Args:
        graph: Adjacency list representation of the graph
        
    Returns:
        Number of connected components
    """
    return len(find_connected_components(graph))


def is_cyclic_component(graph: List[List[int]], component: List[int]) -> bool:
    """Check if a component is cyclic (all vertices have degree 2).
    
    Args:
        graph: Adjacency list representation of the graph
        component: List of vertices in the component
        
    Returns:
        True if the component is cyclic, False otherwise
    """
    if not component:
        return False
    
    # Check if all vertices in the component have degree 2
    for vertex in component:
        if len(graph[vertex]) != 2:
            return False
    
    return True


def find_cyclic_components(graph: List[List[int]]) -> List[List[int]]:
    """Find all cyclic components in the graph.
    
    Args:
        graph: Adjacency list representation of the graph
        
    Returns:
        List of cyclic components, where each component is a list of vertices
    """
    components = find_connected_components(graph)
    return [comp for comp in components if is_cyclic_component(graph, comp)]


def count_cyclic_components(graph: List[List[int]]) -> int:
    """Count the number of cyclic components in the graph.
    
    Args:
        graph: Adjacency list representation of the graph
        
    Returns:
        Number of cyclic components
    """
    return len(find_cyclic_components(graph))


def is_bipartite(graph: List[List[int]]) -> bool:
    """Check if the graph is bipartite (can be colored with 2 colors).
    
    Args:
        graph: Adjacency list representation of the graph
        
    Returns:
        True if the graph is bipartite, False otherwise
    """
    n = len(graph)
    color = [-1] * n  # -1: uncolored, 0: color 0, 1: color 1
    
    for start in range(n):
        if color[start] == -1:
            queue = deque([start])
            color[start] = 0
            
            while queue:
                u = queue.popleft()
                
                for v in graph[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return False
    
    return True