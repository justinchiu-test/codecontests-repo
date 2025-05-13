"""
Library file for cluster2.
This contains shared code that can be imported by problems in this cluster.
"""
import sys
import math
import heapq
import bisect
from collections import Counter, defaultdict, deque
from io import BytesIO, IOBase


# Fast I/O Operations
class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        import os
        self.os = os
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
        self.BUFSIZE = 8192

    def read(self):
        while True:
            b = self.os.read(self._fd, max(self.os.fstat(self._fd).st_size, self.BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = self.os.read(self._fd, max(self.os.fstat(self._fd).st_size, self.BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            self.os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


def setup_io():
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    return lambda: sys.stdin.readline().rstrip("\r\n")


# Input Functions
def get_int(input_func=None):
    if input_func is None:
        input_func = input
    return int(input_func())


def get_ints(input_func=None):
    if input_func is None:
        input_func = input
    return list(map(int, input_func().split()))


def get_int_grid(n, input_func=None):
    if input_func is None:
        input_func = input
    return [get_ints(input_func) for _ in range(n)]


def get_str(input_func=None):
    if input_func is None:
        input_func = input
    return input_func().split()


def yes_no(b):
    return "YES" if b else "NO"


# Binary Search
def binary_search(good, left, right, delta=1, right_true=False):
    """
    Performs binary search
    ----------
    Parameters
    ----------
    :param good: Function used to perform the binary search
    :param left: Starting value of left limit
    :param right: Starting value of the right limit
    :param delta: Margin of error, defaults value of 1 for integer binary search
    :param right_true: Boolean, for whether the right limit is the true invariant
    :return: Returns the most extremal value interval [left, right] which is good function evaluates to True,
            alternatively returns False if no such value found
    """
    limits = [left, right]
    while limits[1] - limits[0] > delta:
        if delta == 1:
            mid = sum(limits) // 2
        else:
            mid = sum(limits) / 2
        if good(mid):
            limits[int(right_true)] = mid
        else:
            limits[int(~right_true)] = mid
    if good(limits[int(right_true)]):
        return limits[int(right_true)]
    else:
        return False


# Prefix Calculations
def prefix_sums(a, drop_zero=False):
    p = [0]
    for x in a:
        p.append(p[-1] + x)
    if drop_zero:
        return p[1:]
    else:
        return p


def prefix_mins(a, drop_zero=False):
    p = [float('inf')]
    for x in a:
        p.append(min(p[-1], x))
    if drop_zero:
        return p[1:]
    else:
        return p


# Graph Algorithms

# Disjoint Set Union (DSU) Implementation
class DSU:
    def __init__(self, nodes):
        # Parents
        self.p = list(range(nodes))
        # Ranks
        self.r = [0] * nodes
        # Sizes
        self.s = [1] * nodes

    def get(self, u):
        # Find with path compression
        if u != self.p[u]:
            self.p[u] = self.get(self.p[u])
        return self.p[u]

    def union(self, u, v):
        # Union by rank
        u = self.get(u)
        v = self.get(v)
        if u != v:
            if self.r[u] > self.r[v]:
                u, v = v, u
            self.p[u] = v
            if self.r[u] == self.r[v]:
                self.r[v] += 1
            self.s[v] += self.s[u]
            return True
        return False

    def get_size(self, u):
        # Get size of component
        u = self.get(u)
        return self.s[u]

    def count_components(self):
        # Count number of connected components
        roots = set()
        for i in range(len(self.p)):
            roots.add(self.get(i))
        return len(roots)
    
    def get_components(self):
        # Get all components as a dict: root -> [nodes]
        components = defaultdict(list)
        for i in range(len(self.p)):
            components[self.get(i)].append(i)
        return components


# DFS Implementations
def dfs(graph, start, visited=None):
    """Recursive DFS implementation"""
    if visited is None:
        visited = set()
    visited.add(start)
    for next_node in graph[start]:
        if next_node not in visited:
            dfs(graph, next_node, visited)
    return visited


def iterative_dfs(graph, start):
    """Iterative DFS implementation for adjacency list"""
    visited = set()
    stack = [start]
    path = []
    
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            path.append(v)
            # Add neighbors in reverse order to simulate recursion
            stack.extend(reversed(graph[v]))
    
    return path, visited


def dfs_grid(grid, i, j, visited=None, valid_check=None):
    """DFS on a 2D grid"""
    if visited is None:
        visited = set()
    rows, cols = len(grid), len(grid[0])
    if i < 0 or i >= rows or j < 0 or j >= cols:
        return visited
    if (i, j) in visited:
        return visited
    if valid_check and not valid_check(grid, i, j):
        return visited
    
    visited.add((i, j))
    # Explore 4 directions: up, right, down, left
    dfs_grid(grid, i-1, j, visited, valid_check)
    dfs_grid(grid, i, j+1, visited, valid_check)
    dfs_grid(grid, i+1, j, visited, valid_check)
    dfs_grid(grid, i, j-1, visited, valid_check)
    return visited


# BFS Implementations
def bfs(graph, start):
    """BFS implementation for adjacency list"""
    visited = {start}
    queue = deque([start])
    path = [start]
    
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                path.append(neighbor)
    
    return path, visited


def bfs_grid(grid, start_i, start_j, valid_check=None):
    """BFS on a 2D grid"""
    rows, cols = len(grid), len(grid[0])
    visited = set([(start_i, start_j)])
    queue = deque([(start_i, start_j)])
    path = [(start_i, start_j)]
    
    while queue:
        i, j = queue.popleft()
        # Check 4 directions: up, right, down, left
        for ni, nj in [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]:
            if 0 <= ni < rows and 0 <= nj < cols and (ni, nj) not in visited:
                if valid_check is None or valid_check(grid, ni, nj):
                    visited.add((ni, nj))
                    queue.append((ni, nj))
                    path.append((ni, nj))
    
    return path, visited


# Graph Construction
def build_graph(n, edges, directed=False, one_indexed=True):
    """Build adjacency list from edges"""
    graph = [[] for _ in range(n + (1 if one_indexed else 0))]
    for u, v in edges:
        graph[u].append(v)
        if not directed:
            graph[v].append(u)
    return graph


def read_graph(m, directed=False, one_indexed=True, input_func=None):
    """Read graph edges from input and build adjacency list"""
    if input_func is None:
        input_func = input
    edges = []
    for _ in range(m):
        u, v = get_ints(input_func)
        edges.append((u, v))
    return edges


def build_adjacency_matrix(n, edges, directed=False):
    """Build adjacency matrix from edges"""
    graph = [[0] * n for _ in range(n)]
    for u, v in edges:
        graph[u][v] = 1
        if not directed:
            graph[v][u] = 1
    return graph


# Connected Components
def count_connected_components(graph):
    """Count connected components in a graph (adjacency list)"""
    n = len(graph)
    visited = [False] * n
    count = 0
    
    for i in range(n):
        if not visited[i]:
            count += 1
            dfs_component(graph, i, visited)
    
    return count


def dfs_component(graph, node, visited):
    """DFS helper for counting components"""
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs_component(graph, neighbor, visited)


def get_connected_components(graph, start_idx=0):
    """Get all connected components in a graph (adjacency list)"""
    n = len(graph)
    visited = [False] * n
    components = []
    
    for i in range(start_idx, n):
        if not visited[i]:
            component = []
            dfs_collect(graph, i, visited, component)
            components.append(component)
    
    return components


def dfs_collect(graph, node, visited, component):
    """DFS helper for collecting components"""
    visited[node] = True
    component.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs_collect(graph, neighbor, visited, component)


# Cycle Detection
def detect_cycle(graph, start=1, one_indexed=True):
    """Detect if there's a cycle in an undirected graph from a given start node"""
    start_idx = start if not one_indexed else start
    visited = set()
    return dfs_cycle_check(graph, start_idx, -1, visited)


def dfs_cycle_check(graph, node, parent, visited):
    """DFS helper for cycle detection in undirected graph"""
    visited.add(node)
    
    for neighbor in graph[node]:
        if neighbor == parent:
            continue
        if neighbor in visited:
            return True
        if dfs_cycle_check(graph, neighbor, node, visited):
            return True
    
    return False


def detect_directed_cycle(graph):
    """Detect if there's a cycle in a directed graph (adjacency list)"""
    n = len(graph)
    visited = [False] * n
    rec_stack = [False] * n
    
    for i in range(n):
        if not visited[i]:
            if is_cyclic_util(graph, i, visited, rec_stack):
                return True
    
    return False


def is_cyclic_util(graph, node, visited, rec_stack):
    """Helper for directed cycle detection"""
    visited[node] = True
    rec_stack[node] = True
    
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if is_cyclic_util(graph, neighbor, visited, rec_stack):
                return True
        elif rec_stack[neighbor]:
            return True
    
    rec_stack[node] = False
    return False


# Check if component is cyclic (all vertices have exactly 2 neighbors)
def is_cyclic_component(graph, start):
    """Check if a component is a cycle (all vertices have degree 2)"""
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        visited.add(node)
        
        # If not exactly 2 neighbors, not a cycle
        if len(graph[node]) != 2:
            return False
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
    
    return True


# Count cyclic components
def count_cyclic_components(graph):
    """Count components where all vertices have exactly 2 neighbors"""
    n = len(graph)
    visited = [False] * n
    count = 0
    
    for i in range(n):
        if not visited[i]:
            if bfs_check_cyclic(graph, i, visited):
                count += 1
    
    return count


def bfs_check_cyclic(graph, start, visited):
    """BFS to check if a component is cyclic"""
    queue = deque([start])
    component_visited = set([start])
    is_cyclic = True
    
    while queue:
        node = queue.popleft()
        visited[node] = True
        
        # If not exactly 2 neighbors, not a cycle
        if len(graph[node]) != 2:
            is_cyclic = False
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                component_visited.add(neighbor)
    
    return is_cyclic and len(component_visited) >= 3  # Cycles have at least 3 vertices


# Common Graph Problem Solutions
def count_bridges(graph):
    """Count bridges in an undirected graph"""
    n = len(graph)
    visited = [False] * n
    disc = [-1] * n  # Discovery time
    low = [-1] * n   # Earliest visited vertex reachable from subtree
    parent = [-1] * n
    bridges = []
    
    def dfs_bridges(u, time):
        visited[u] = True
        disc[u] = low[u] = time
        time += 1
        
        for v in graph[u]:
            if not visited[v]:
                parent[v] = u
                time = dfs_bridges(v, time)
                
                # Check if subtree rooted with v has a connection
                # to one of the ancestors of u
                low[u] = min(low[u], low[v])
                
                # If the lowest vertex reachable from subtree under v is below u
                # in DFS tree, then u-v is a bridge
                if low[v] > disc[u]:
                    bridges.append((u, v))
            
            elif v != parent[u]:  # Update low value of u for parent function calls
                low[u] = min(low[u], disc[v])
        
        return time
    
    for i in range(n):
        if not visited[i]:
            dfs_bridges(i, 0)
    
    return bridges


def check_graph_property(graph, property_func, start_idx=0):
    """Check if a property holds for all connected components"""
    n = len(graph)
    visited = [False] * n
    
    for i in range(start_idx, n):
        if not visited[i]:
            component = []
            dfs_collect(graph, i, visited, component)
            if not property_func(graph, component):
                return False
    
    return True