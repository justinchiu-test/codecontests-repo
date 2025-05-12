"""
Library file for cluster3.
This contains shared code that can be imported by problems in this cluster.
"""
import sys
from collections import defaultdict, deque
from types import GeneratorType
import os
from io import BytesIO, IOBase

# Fast I/O
BUFSIZE = 8192

class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
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
    """Set up fast I/O"""
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    return lambda: sys.stdin.readline().rstrip("\r\n")

# Tail recursion optimization
def bootstrap(f, stack=[]):
    """
    Decorator for tail-recursion optimization.
    Used in tree traversal algorithms to prevent stack overflow.
    """
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

# Input reading utilities
def read_int():
    """Read a single integer from input"""
    return int(input())

def read_ints():
    """Read multiple integers from a single line"""
    return list(map(int, input().split()))

def read_array(n=None):
    """Read an array of integers"""
    if n is None:
        return list(map(int, input().split()))
    return list(map(int, input().split()))[:n]

# Tree utilities
def read_tree(n, indexed_from=1, directed=False):
    """
    Read a tree from input.
    Returns adjacency list.
    """
    adj = [[] for _ in range(n + 1)] if indexed_from == 1 else [[] for _ in range(n)]
    
    for _ in range(n - 1):
        a, b = map(int, input().split())
        if indexed_from == 1:
            adj[a].append(b)
            if not directed:
                adj[b].append(a)
        else:  # indexed_from = 0
            a -= 1  # Convert to 0-indexed
            b -= 1
            adj[a].append(b)
            if not directed:
                adj[b].append(a)
            
    return adj

def read_tree_with_values(n, indexed_from=1, directed=False):
    """
    Read a tree with values from input.
    Returns adjacency list and values.
    """
    adj = [[] for _ in range(n + 1)] if indexed_from == 1 else [[] for _ in range(n)]
    values = list(map(int, input().split()))
    
    if indexed_from == 1:
        values = [0] + values
    
    for _ in range(n - 1):
        a, b = map(int, input().split())
        if indexed_from == 1:
            adj[a].append(b)
            if not directed:
                adj[b].append(a)
        else:  # indexed_from = 0
            a -= 1  # Convert to 0-indexed
            b -= 1
            adj[a].append(b)
            if not directed:
                adj[b].append(a)
            
    return adj, values

def read_tree_with_parents(n, indexed_from=1):
    """
    Read a tree where input is given as parent list.
    Returns adjacency list.
    """
    adj = [[] for _ in range(n + 1)] if indexed_from == 1 else [[] for _ in range(n)]
    parents = list(map(int, input().split()))
    
    for i in range(len(parents)):
        child = i + 2 if indexed_from == 1 else i + 1
        parent = parents[i]
        
        adj[child].append(parent)
        adj[parent].append(child)
            
    return adj

def get_tree_parent_pointers(graph, root=1):
    """
    Get parent pointers for a tree.
    Returns an array where parents[i] is the parent of node i.
    """
    n = len(graph)
    parents = [0] * n
    queue = [root]
    visited = [False] * n
    visited[root] = True
    
    while queue:
        node = queue.pop(0)
        for child in graph[node]:
            if not visited[child]:
                parents[child] = node
                visited[child] = True
                queue.append(child)
                
    return parents

def get_leaf_nodes(graph, root=1):
    """
    Get leaf nodes of a tree.
    A leaf node is a node with only one neighbor (its parent).
    """
    leaves = []
    for node in range(1, len(graph)):
        if len(graph[node]) == 1 and node != root:
            leaves.append(node)
    return leaves

def get_subtree_size(graph, root=1, parent=None):
    """
    Calculate the size of each subtree.
    Returns an array where result[i] is the size of the subtree rooted at node i.
    """
    n = len(graph)
    result = [1] * n  # Initialize each node's subtree size to 1 (counting itself)
    
    def dfs(node, parent):
        for child in graph[node]:
            if child != parent:
                dfs(child, node)
                result[node] += result[child]
    
    dfs(root, parent)
    return result

def get_tree_depths(graph, root=1):
    """
    Calculate the depth of each node in a tree.
    Returns an array where depths[i] is the depth of node i.
    """
    n = len(graph)
    depths = [0] * n
    visited = [False] * n
    
    def dfs(node, depth, parent):
        depths[node] = depth
        visited[node] = True
        
        for child in graph[node]:
            if child != parent:
                dfs(child, depth + 1, node)
    
    dfs(root, 0, -1)
    return depths

def dfs(graph, start, visited=None):
    """
    Depth-first search using a stack.
    Returns visited nodes.
    """
    if visited is None:
        visited = set()
    
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(set(graph[vertex]) - visited)
    
    return visited

def iterative_dfs(graph, start):
    """
    Iterative DFS that mimics recursive behavior for tree traversal
    Returns visited and ordering (pre-order, post-order)
    """
    stack = [start]
    visited = [0] * len(graph)
    pre_order = []
    post_order = []
    
    while stack:
        node = stack[-1]
        
        if not visited[node]:
            visited[node] = 1
            pre_order.append(node)
            
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    stack.append(neighbor)
        else:
            post_order.append(stack.pop())
    
    return visited, pre_order, post_order

def iterative_dfs_with_parent(graph, start, parent=None):
    """
    Iterative DFS with parent tracking, useful for tree algorithms
    """
    stack = [(start, parent)]  # (node, parent)
    visited = [0] * len(graph)
    result = []
    
    while stack:
        node, parent = stack[-1]
        
        if not visited[node]:
            visited[node] = 1
            result.append((node, parent))
            
            for neighbor in graph[node]:
                if neighbor != parent and not visited[neighbor]:
                    stack.append((neighbor, node))
        else:
            stack.pop()
    
    return result

def bfs(graph, start):
    """
    Breadth-first search.
    Returns distances from start.
    """
    distances = {start: 0}
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in distances:
                distances[neighbor] = distances[vertex] + 1
                queue.append(neighbor)
    
    return distances

def count_subtree_leaves(graph, root):
    """
    Counts the number of leaves in each subtree.
    Used for problems like 1056D - Decorate Apple Tree.
    """
    n = len(graph)
    counts = [0] * n
    visited = [False] * n

    def dfs(node):
        if visited[node]:
            return counts[node]
        
        visited[node] = True
        is_leaf = True
        
        for child in graph[node]:
            if not visited[child]:
                dfs(child)
                counts[node] += counts[child]
                is_leaf = False
        
        if is_leaf:
            counts[node] = 1
        
        return counts[node]

    dfs(root)
    return counts

def tree_dp_postorder(graph, start, values=None, parent=None):
    """
    Tree DP in post-order traversal.
    Returns results in post-order.
    """
    if parent is None:
        parent = [-1] * len(graph)
        
    stack = [start]
    visited = [0] * len(graph)
    result = [0] * len(graph)
    
    while stack:
        node = stack[-1]
        
        if not visited[node]:
            visited[node] = 1
            for neighbor in graph[node]:
                if neighbor != parent[node] and not visited[neighbor]:
                    parent[neighbor] = node
                    stack.append(neighbor)
        else:
            node = stack.pop()
            result[node] = values[node] if values else 1
            
            for neighbor in graph[node]:
                if neighbor != parent[node]:
                    result[node] += result[neighbor]
                    
    return result, parent

def tree_rerooting(graph, root=1, values=None):
    """
    Re-rooting a tree to find optimal values for each node as root.
    Uses DP approach.
    """
    n = len(graph)
    
    # First pass: compute subtree values bottom-up
    subtree_sum = [0] * n
    
    def dfs1(node, parent):
        subtree_sum[node] = values[node] if values else 1
        for child in graph[node]:
            if child != parent:
                dfs1(child, node)
                subtree_sum[node] += subtree_sum[child]
    
    dfs1(root, -1)
    
    # Second pass: re-root DP calculation
    result = [0] * n
    result[root] = subtree_sum[root]
    
    def dfs2(node, parent):
        for child in graph[node]:
            if child != parent:
                # Re-root formula depends on problem-specific calculation
                # Typically something like:
                # result[child] = result[node] - subtree_sum[child] + (n - subtree_sum[child])
                # Or more generally:
                result[child] = result[node] + (subtree_sum[root] - 2 * subtree_sum[child])
                dfs2(child, node)
    
    dfs2(root, -1)
    return result

def find_tree_diameter(graph):
    """
    Find the diameter of a tree (the longest path between any two nodes).
    Returns the diameter length.
    """
    # Run BFS from any node to find the farthest node
    distances = bfs(graph, 1)
    farthest_node = max(distances, key=distances.get)
    
    # Run BFS from the farthest node to find the diameter
    distances = bfs(graph, farthest_node)
    diameter = max(distances.values())
    
    return diameter

def binary_lift(graph, root=1, log_n=20):
    """
    Precompute the 2^i-th ancestor for each node using binary lifting.
    Useful for LCA and other tree queries.
    """
    n = len(graph)
    parent = [-1] * n
    depth = [0] * n
    
    # Compute the parent and depth for each node
    def dfs(node, prev, d):
        parent[node] = prev
        depth[node] = d
        for child in graph[node]:
            if child != prev:
                dfs(child, node, d + 1)
    
    dfs(root, -1, 0)
    
    # Binary lifting preprocessing
    up = [[-1] * log_n for _ in range(n)]
    for i in range(n):
        up[i][0] = parent[i]
    
    for j in range(1, log_n):
        for i in range(n):
            if up[i][j - 1] != -1:
                up[i][j] = up[up[i][j - 1]][j - 1]
    
    return up, depth

def lca(up, depth, u, v, log_n=20):
    """
    Find the lowest common ancestor of two nodes using binary lifting.
    """
    # Make u the deeper node
    if depth[u] < depth[v]:
        u, v = v, u
    
    # Bring u to the same depth as v
    for i in range(log_n - 1, -1, -1):
        if depth[u] - (1 << i) >= depth[v]:
            u = up[u][i]
    
    if u == v:
        return u
    
    # Find the LCA
    for i in range(log_n - 1, -1, -1):
        if up[u][i] != -1 and up[u][i] != up[v][i]:
            u = up[u][i]
            v = up[v][i]
    
    return up[u][0]

def tree_rerooting_with_edge_values(graph, edge_values, root=1):
    """
    Re-rooting technique for trees with values on edges.
    """
    n = len(graph)
    
    # Adjacency list with edge values
    adj = [[] for _ in range(n)]
    for u, v, w in edge_values:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # First pass: compute subtree values bottom-up
    subtree_sum = [0] * n
    
    def dfs1(node, parent):
        subtree_sum[node] = 0
        for child, weight in adj[node]:
            if child != parent:
                dfs1(child, node)
                subtree_sum[node] += subtree_sum[child] + weight
    
    dfs1(root, -1)
    
    # Second pass: re-root DP calculation
    result = [0] * n
    result[root] = subtree_sum[root]
    
    def dfs2(node, parent):
        for child, weight in adj[node]:
            if child != parent:
                # Re-root formula:
                result[child] = result[node] - subtree_sum[child] - weight + (subtree_sum[root] - subtree_sum[child] - weight)
                dfs2(child, node)
    
    dfs2(root, -1)
    return result

def max_independent_set_tree(graph, root=1):
    """
    Calculate the maximum independent set in a tree using DP.
    """
    n = len(graph)
    
    # dp[node][0] = max independent set if node is not in the set
    # dp[node][1] = max independent set if node is in the set
    dp = [[0, 0] for _ in range(n)]
    
    def dfs(node, parent):
        # If node is not in the set, children can be in the set or not
        dp[node][0] = 0
        dp[node][1] = 1  # Node is in the set
        
        for child in graph[node]:
            if child != parent:
                dfs(child, node)
                # Node not in set, children can be in set or not
                dp[node][0] += max(dp[child][0], dp[child][1])
                # Node in set, children must not be in set
                dp[node][1] += dp[child][0]
    
    dfs(root, -1)
    return max(dp[root][0], dp[root][1])

def heavy_light_decomposition(graph, root=1):
    """
    Heavy-light decomposition of a tree.
    Useful for path queries.
    """
    n = len(graph)
    parent = [-1] * n
    depth = [0] * n
    subtree_size = [1] * n
    
    # DFS to compute subtree sizes
    def dfs_size(node, par):
        parent[node] = par
        for child in graph[node]:
            if child != par:
                depth[child] = depth[node] + 1
                dfs_size(child, node)
                subtree_size[node] += subtree_size[child]
    
    dfs_size(root, -1)
    
    # HLD decomposition
    chain_heads = [-1] * n  # Head of the chain containing node i
    chain_size = [0]  # Size of each chain
    chain_id = [-1] * n  # Chain ID for each node
    chain_pos = [-1] * n  # Position of node in its chain
    
    def dfs_hld(node, par, chain):
        chain_id[node] = chain
        chain_pos[node] = chain_size[chain]
        chain_size[chain] += 1
        
        # Find the heavy child
        heavy_child = -1
        for child in graph[node]:
            if child != par and (heavy_child == -1 or subtree_size[child] > subtree_size[heavy_child]):
                heavy_child = child
        
        # Process the heavy child first to extend the current chain
        if heavy_child != -1:
            dfs_hld(heavy_child, node, chain)
        
        # Process other children, each forming a new chain
        for child in graph[node]:
            if child != par and child != heavy_child:
                chain_heads.append(child)
                dfs_hld(child, node, len(chain_heads) - 1)
    
    chain_heads[0] = root
    dfs_hld(root, -1, 0)
    
    return chain_heads, chain_id, chain_pos, parent, depth

def tree_center(graph):
    """
    Find the center(s) of a tree.
    The center is the node(s) that minimizes the maximum distance to any other node.
    """
    n = len(graph)
    degree = [0] * n
    leaves = []
    
    # Count degree of each node
    for i in range(n):
        degree[i] = len(graph[i])
        if degree[i] == 1 and i != 0:  # Ignore the dummy node 0
            leaves.append(i)
    
    remaining_nodes = n
    
    # Remove leaves level by level
    while remaining_nodes > 2:
        remaining_nodes -= len(leaves)
        new_leaves = []
        
        # Remove current leaves
        for leaf in leaves:
            for neighbor in graph[leaf]:
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    new_leaves.append(neighbor)
        
        leaves = new_leaves
    
    return leaves  # Contains 1 or 2 centers