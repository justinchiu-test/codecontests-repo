"""
Library file for cluster2.
This contains shared code that can be imported by problems in this cluster.
"""
import sys
from collections import defaultdict, deque, Counter
from typing import List, Dict, Set, Tuple, Optional, Any, Union, Callable, Iterator
from array import array

# IO module
class FastIO:
    def __init__(self, file=sys.stdin):
        self.buffer = ""
        self.pointer = 0
        self.file = file

    def readline(self) -> str:
        return self.file.readline().rstrip('\r\n')

    def read_int(self) -> int:
        return int(self.readline())

    def read_ints(self) -> List[int]:
        return list(map(int, self.readline().split()))

    def read_int_tuple(self) -> Tuple[int, ...]:
        return tuple(map(int, self.readline().split()))

# Shorthand IO functions
def readline() -> str:
    return sys.stdin.buffer.readline().decode('utf-8').rstrip()

def I() -> List[int]:
    return list(map(int, readline().split()))

# Graph module
class Graph:
    def __init__(self, n: int = 0, directed: bool = False, weighted: bool = False):
        self.n = n
        self.directed = directed
        self.weighted = weighted
        self.adj = defaultdict(list) if weighted else defaultdict(set)
        self.weights = {}

    def add_vertex(self, vertex: int) -> None:
        if vertex not in self.adj:
            self.adj[vertex] = [] if self.weighted else set()

    def add_edge(self, u: int, v: int, weight: int = 1) -> None:
        if self.weighted:
            self.adj[u].append(v)
            self.weights[(u, v)] = weight
            if not self.directed:
                self.adj[v].append(u)
                self.weights[(v, u)] = weight
        else:
            self.adj[u].add(v)
            if not self.directed:
                self.adj[v].add(u)

    def add_bidirectional_edge(self, u: int, v: int, weight: int = 1) -> None:
        self.add_edge(u, v, weight)
        if self.directed:
            self.add_edge(v, u, weight)

    def neighbors(self, vertex: int) -> Union[List[int], Set[int]]:
        return self.adj[vertex]

    def vertices(self) -> Set[int]:
        return set(self.adj.keys())

    def build_from_edges(self, edges: List[Tuple], zero_indexed: bool = True) -> None:
        for edge in edges:
            if len(edge) == 2:
                u, v = edge
                w = 1
            else:
                u, v, w = edge
            
            if not zero_indexed:
                u -= 1
                v -= 1
            
            self.add_edge(u, v, w)

    @classmethod
    def from_stdin(cls, directed: bool = False, weighted: bool = False, one_indexed: bool = True) -> 'Graph':
        n, m = map(int, input().split())
        g = cls(n, directed, weighted)
        
        for _ in range(m):
            line = list(map(int, input().split()))
            u, v = line[0], line[1]
            
            if one_indexed:
                u -= 1
                v -= 1
                
            if weighted and len(line) > 2:
                w = line[2]
                g.add_edge(u, v, w)
            else:
                g.add_edge(u, v)
                
        return g

    def get_complement(self, n: int) -> 'Graph':
        """Returns the complement graph where edges exist if they don't in the original graph."""
        complement = Graph(n, self.directed, self.weighted)
        
        for u in range(n):
            for v in range(n):
                if u != v and v not in self.neighbors(u):
                    complement.add_edge(u, v)
                    
        return complement

    def find_bridges(self) -> List[Tuple[int, int]]:
        """Finds all bridges in the graph using Tarjan's algorithm."""
        visited = {}
        disc = {}  # Discovery time
        low = {}   # Earliest visited vertex
        parent = {}
        time = [0]  # Use a list to allow modification in nested function
        bridges = []
        
        def dfs(u: int) -> None:
            visited[u] = True
            disc[u] = low[u] = time[0]
            time[0] += 1
            
            for v in self.neighbors(u):
                if v not in visited:
                    parent[v] = u
                    dfs(v)
                    
                    low[u] = min(low[u], low[v])
                    
                    if low[v] > disc[u]:
                        bridges.append((u, v))
                        
                elif v != parent.get(u, -1):
                    low[u] = min(low[u], disc[v])
                    
        for vertex in self.vertices():
            if vertex not in visited:
                parent[vertex] = -1
                dfs(vertex)
                
        return bridges

    def find_articulation_points(self) -> List[int]:
        """Finds all articulation points in the graph using Tarjan's algorithm."""
        visited = {}
        disc = {}  # Discovery time
        low = {}   # Earliest visited vertex
        parent = {}
        time = [0]  # Use a list to allow modification in nested function
        ap = set()  # Articulation points
        
        def dfs(u: int) -> None:
            children = 0
            visited[u] = True
            disc[u] = low[u] = time[0]
            time[0] += 1
            
            for v in self.neighbors(u):
                if v not in visited:
                    parent[v] = u
                    children += 1
                    dfs(v)
                    
                    low[u] = min(low[u], low[v])
                    
                    # Case 1: u is root and has at least two children
                    if parent[u] == -1 and children > 1:
                        ap.add(u)
                        
                    # Case 2: At least one component will be disconnected
                    if parent[u] != -1 and low[v] >= disc[u]:
                        ap.add(u)
                        
                elif v != parent.get(u, -1):
                    low[u] = min(low[u], disc[v])
                    
        for vertex in self.vertices():
            if vertex not in visited:
                parent[vertex] = -1
                dfs(vertex)
                
        return list(ap)

    def get_diameter(self) -> int:
        """Find the diameter of a tree (longest path between any two nodes)."""
        if not self.vertices():
            return 0
            
        # Step 1: Find the farthest node from any node
        def bfs_farthest(start: int) -> Tuple[int, int]:
            dist = {start: 0}
            queue = deque([start])
            
            while queue:
                node = queue.popleft()
                
                for neighbor in self.neighbors(node):
                    if neighbor not in dist:
                        dist[neighbor] = dist[node] + 1
                        queue.append(neighbor)
            
            if not dist:
                return start, 0
                
            # Return the farthest node and its distance
            farthest_node = max(dist.items(), key=lambda x: x[1])
            return farthest_node
        
        # Pick any node
        start_node = next(iter(self.vertices()))
        
        # Find the farthest node from the start node
        farthest, _ = bfs_farthest(start_node)
        
        # Find the farthest node from the previously found node
        _, diameter = bfs_farthest(farthest)
        
        return diameter

# Graph algorithms
def dfs(graph: Graph, start: int, visited: Optional[Dict[int, bool]] = None) -> Dict[int, bool]:
    if visited is None:
        visited = {}
    
    visited[start] = True
    
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return visited

def dfs_iterative(graph: Graph, start: int, visited: Optional[Dict[int, bool]] = None) -> Dict[int, bool]:
    if visited is None:
        visited = {}
    
    stack = [start]
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited[vertex] = True
            stack.extend(neighbor for neighbor in graph.neighbors(vertex) if neighbor not in visited)
    
    return visited

def bfs(graph: Graph, start: int, visited: Optional[Dict[int, bool]] = None) -> Dict[int, bool]:
    if visited is None:
        visited = {}
    
    visited[start] = True
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        for neighbor in graph.neighbors(vertex):
            if neighbor not in visited:
                visited[neighbor] = True
                queue.append(neighbor)
    
    return visited

def bfs_distances(graph: Graph, start: int) -> Dict[int, int]:
    """BFS that returns distances from start to all reachable nodes."""
    distances = {start: 0}
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        for neighbor in graph.neighbors(vertex):
            if neighbor not in distances:
                distances[neighbor] = distances[vertex] + 1
                queue.append(neighbor)
    
    return distances

def find_connected_components(graph: Graph) -> List[Set[int]]:
    visited = {}
    components = []
    
    for vertex in graph.vertices():
        if vertex not in visited:
            component = set(dfs(graph, vertex, {}).keys())
            components.append(component)
            visited.update({v: True for v in component})
    
    return components

def count_connected_components(graph: Graph) -> int:
    visited = {}
    count = 0
    
    for vertex in graph.vertices():
        if vertex not in visited:
            dfs(graph, vertex, visited)
            count += 1
    
    return count

def has_cycle(graph: Graph) -> bool:
    visited = {}
    rec_stack = {}
    
    def _dfs_cycle(v: int) -> bool:
        visited[v] = True
        rec_stack[v] = True
        
        for neighbor in graph.neighbors(v):
            if neighbor not in visited:
                if _dfs_cycle(neighbor):
                    return True
            elif rec_stack.get(neighbor, False):
                return True
        
        rec_stack[v] = False
        return False
    
    for vertex in graph.vertices():
        if vertex not in visited:
            if _dfs_cycle(vertex):
                return True
    
    return False

def has_cycle_undirected(graph: Graph) -> bool:
    visited = {}
    
    def _dfs_cycle(v: int, parent: int = -1) -> bool:
        visited[v] = True
        
        for neighbor in graph.neighbors(v):
            if neighbor not in visited:
                if _dfs_cycle(neighbor, v):
                    return True
            elif neighbor != parent:
                return True
        
        return False
    
    for vertex in graph.vertices():
        if vertex not in visited:
            if _dfs_cycle(vertex):
                return True
    
    return False

def find_cycle(graph: Graph) -> List[int]:
    """Find a cycle in a directed graph if one exists."""
    visited = {}
    rec_stack = {}
    cycle = []
    found = [False]  # Use a list to allow modification in nested function
    
    def _dfs_cycle(v: int) -> None:
        if found[0]:  # Stop recursion if cycle is already found
            return
            
        visited[v] = True
        rec_stack[v] = True
        
        for neighbor in graph.neighbors(v):
            if found[0]:
                return
                
            if neighbor not in visited:
                cycle.append(neighbor)
                _dfs_cycle(neighbor)
                if found[0]:
                    return
                cycle.pop()
            elif rec_stack.get(neighbor, False):
                cycle.append(neighbor)
                found[0] = True
                return
        
        rec_stack[v] = False
        
    for vertex in graph.vertices():
        if found[0]:
            break
            
        if vertex not in visited:
            cycle = [vertex]
            _dfs_cycle(vertex)
            if found[0]:
                # Trim the cycle to start from the repeated vertex
                start_idx = cycle.index(cycle[-1])
                return cycle[start_idx:]
    
    return []  # No cycle found

def find_cycle_undirected(graph: Graph) -> List[int]:
    """Find a cycle in an undirected graph if one exists."""
    visited = {}
    cycle = []
    found = [False]  # Use a list to allow modification in nested function
    
    def _dfs_cycle(v: int, parent: int = -1) -> None:
        if found[0]:  # Stop recursion if cycle is already found
            return
            
        visited[v] = True
        
        for neighbor in graph.neighbors(v):
            if found[0]:
                return
                
            if neighbor == parent:
                continue
                
            if neighbor in visited:
                cycle.append(neighbor)
                found[0] = True
                return
                
            cycle.append(neighbor)
            _dfs_cycle(neighbor, v)
            if found[0]:
                return
            cycle.pop()
        
    for vertex in graph.vertices():
        if found[0]:
            break
            
        if vertex not in visited:
            cycle = [vertex]
            _dfs_cycle(vertex)
            if found[0]:
                # Find the start of the cycle
                start_idx = cycle.index(cycle[-1])
                return cycle[start_idx:]
    
    return []  # No cycle found

def build_bridge_tree(v_count: int, edge_count: int, adj: List[List[int]], edge_index: List[List[int]]) -> List[List[int]]:
    """
    Build a bridge tree using an iterative approach.
    This implementation is optimized for performance.
    """
    from collections import deque
    
    preorder = [0]
    parent = [0] + [-1] * (v_count-1)
    order = [0] + [-1] * (v_count-1)
    low = [0] * v_count
    stack = [0]
    rem = [len(dests)-1 for dests in adj]
    pre_i = 1
    
    # Find bridges using a modified DFS algorithm
    while stack:
        v = stack.pop()
        
        while rem[v] >= 0:
            dest = adj[v][rem[v]]
            rem[v] -= 1
            
            if order[dest] == -1:
                preorder.append(dest)
                order[dest] = low[dest] = pre_i
                parent[dest] = v
                pre_i += 1
                stack.extend((v, dest))
                break
    
    is_bridge = array('b', [0]) * edge_count
    
    for v in reversed(preorder):
        for dest, ei in zip(adj[v], edge_index[v]):
            if dest != parent[v] and low[v] > low[dest]:
                low[v] = low[dest]
            if dest != parent[v] and order[v] < low[dest]:
                is_bridge[ei] = 1
    
    # Build the bridge tree
    bridge_tree = [[] for _ in range(v_count)]
    stack = [0]
    visited = array('b', [1] + [0]*(v_count-1))
    
    while stack:
        v = stack.pop()
        dq = deque([v])
        while dq:
            u = dq.popleft()
            for dest, ei in zip(adj[u], edge_index[u]):
                if visited[dest]:
                    continue
                visited[dest] = 1
                
                if is_bridge[ei]:
                    bridge_tree[v].append(dest)
                    bridge_tree[dest].append(v)
                    stack.append(dest)
                else:
                    dq.append(dest)
    
    return bridge_tree

def get_tree_diameter(adj: List[List[int]]) -> int:
    """
    Calculate the diameter of a tree represented as an adjacency list.
    Returns the length of the longest path in the tree.
    """
    from collections import deque
    n = len(adj)
    
    # Perform BFS to find the farthest node from an arbitrary starting point
    def bfs_farthest(start: int) -> Tuple[int, int]:
        dist = [-1] * n
        dist[start] = 0
        dq = deque([start])
        
        max_dist = 0
        farthest_node = start
        
        while dq:
            node = dq.popleft()
            
            for neighbor in adj[node]:
                if dist[neighbor] == -1:
                    dist[neighbor] = dist[node] + 1
                    dq.append(neighbor)
                    
                    if dist[neighbor] > max_dist:
                        max_dist = dist[neighbor]
                        farthest_node = neighbor
        
        return farthest_node, max_dist
    
    # Find the farthest node from node 0
    end1, _ = bfs_farthest(0)
    
    # Find the farthest node from end1 and get the distance (diameter)
    _, diameter = bfs_farthest(end1)
    
    return diameter

# DSU (Disjoint Set Union)
class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
        self.count = n  # Number of components

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
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
        
        self.count -= 1
        return True

    def size_of(self, x: int) -> int:
        return self.size[self.find(x)]

    def same_set(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def num_components(self) -> int:
        return self.count
        
    def get_components(self) -> Dict[int, List[int]]:
        """Returns all components as a dictionary mapping root to list of elements."""
        components = defaultdict(list)
        for i in range(len(self.parent)):
            root = self.find(i)
            components[root].append(i)
        return components

# Helper functions
def read_grid(rows: int, convert_to_int: bool = False) -> List[List]:
    grid = []
    for _ in range(rows):
        row = input().strip()
        if convert_to_int:
            row = list(map(int, row.split()))
        else:
            row = list(row)
        grid.append(row)
    return grid

def get_neighbors_grid(grid: List[List], r: int, c: int, diagonals: bool = False) -> Iterator[Tuple[int, int]]:
    """Returns neighboring cells in a grid."""
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    if diagonals:
        directions.extend([(1, 1), (1, -1), (-1, -1), (-1, 1)])
    
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            yield nr, nc

def grid_to_graph(grid: List[List], connect_same: bool = True, diagonals: bool = False) -> Graph:
    """Convert a grid to a graph where each cell is a node."""
    rows, cols = len(grid), len(grid[0])
    graph = Graph(rows * cols)
    
    def cell_to_node(r: int, c: int) -> int:
        return r * cols + c
    
    for r in range(rows):
        for c in range(cols):
            for nr, nc in get_neighbors_grid(grid, r, c, diagonals):
                if (connect_same and grid[r][c] == grid[nr][nc]) or not connect_same:
                    graph.add_edge(cell_to_node(r, c), cell_to_node(nr, nc))
    
    return graph