"""
Library file for cluster3.
This contains shared code that can be imported by problems in this cluster.
"""
import sys
import threading
from collections import defaultdict, deque
from functools import wraps
from typing import List, Dict, Callable, Any, Tuple, Set, Optional, Union, Generator

# I/O Optimizations
def fast_io():
    """Set up fast I/O optimizations."""
    sys.setrecursionlimit(10**6)
    try:
        threading.stack_size(10**8)
    except:
        pass

# Input parsing
def read_int():
    """Read a single integer from stdin."""
    return int(input())

def read_ints():
    """Read integers from a line of stdin."""
    return list(map(int, input().split()))

def read_tree(n: int, directed: bool = False, zero_indexed: bool = True, weighted: bool = False) -> List[List[Any]]:
    """
    Read a tree with n nodes (n-1 edges) from stdin.
    
    Args:
        n: Number of nodes
        directed: Whether the tree is directed
        zero_indexed: Whether node indices start from 0 or 1
        weighted: Whether edges have weights
        
    Returns:
        Adjacency list representation of the tree
    """
    offset = 0 if zero_indexed else 1
    adj = [[] for _ in range(n + (0 if zero_indexed else 1))]
        
    for _ in range(n - 1):
        if weighted:
            u, v, w = read_ints()
            if not zero_indexed:
                u -= 1
                v -= 1
            adj[u + offset].append((v + offset, w))
            if not directed:
                adj[v + offset].append((u + offset, w))
        else:
            u, v = read_ints()
            if not zero_indexed:
                u -= 1
                v -= 1
            adj[u + offset].append(v + offset)
            if not directed:
                adj[v + offset].append(u + offset)
            
    return adj

def read_tree_from_parent_array(parent_array: List[int], root_value: int, one_indexed: bool = True) -> List[List[int]]:
    """
    Build adjacency list from parent array.
    
    Args:
        parent_array: List where parent_array[i] is the parent of node i
        root_value: The value indicating root node (typically 0 or 1)
        one_indexed: Whether node indices start from 1
        
    Returns:
        Adjacency list representation of the tree
    """
    n = len(parent_array)
    offset = 1 if one_indexed else 0
    adj = [[] for _ in range(n + offset)]
    
    for i in range(len(parent_array)):
        if parent_array[i] != root_value:
            parent = parent_array[i]
            child = i + offset
            adj[parent].append(child)
            adj[child].append(parent)
            
    return adj

# Tree algorithms
def dfs(adj: List[List[int]], start: int = 0, parent: int = -1) -> List[int]:
    """
    Perform DFS traversal of a tree.
    
    Args:
        adj: Adjacency list representation of the tree
        start: Starting node
        parent: Parent of the starting node
        
    Returns:
        List of nodes in DFS order
    """
    n = len(adj)
    visited = [False] * n
    result = []
    
    def _dfs(node: int, parent: int):
        visited[node] = True
        result.append(node)
        for neighbor in adj[node]:
            if neighbor != parent and not visited[neighbor]:
                _dfs(neighbor, node)
    
    _dfs(start, parent)
    return result

def calculate_subtree_sizes(adj: List[List[int]], root: int = 0) -> List[int]:
    """
    Calculate subtree sizes for each node in a tree.
    
    Args:
        adj: Adjacency list representation of the tree
        root: Root node
        
    Returns:
        List of subtree sizes
    """
    n = len(adj)
    subtree_sizes = [1] * n  # Initialize with 1 (count self)
    
    def _dfs(node: int, parent: int):
        for child in adj[node]:
            if child != parent:
                _dfs(child, node)
                subtree_sizes[node] += subtree_sizes[child]
    
    _dfs(root, -1)
    return subtree_sizes

def calculate_depths(adj: List[List[int]], root: int = 0) -> List[int]:
    """
    Calculate depths for each node in a tree.
    
    Args:
        adj: Adjacency list representation of the tree
        root: Root node
        
    Returns:
        List of depths
    """
    n = len(adj)
    depths = [0] * n
    
    def _dfs(node: int, parent: int, depth: int):
        depths[node] = depth
        for child in adj[node]:
            if child != parent:
                _dfs(child, node, depth + 1)
    
    _dfs(root, -1, 0)
    return depths

def tree_dp_bottom_up(adj: List[List[Any]], process_node: Callable[[int, int, List[Any]], Any], root: int = 0, weighted: bool = False) -> List[Any]:
    """
    Bottom-up dynamic programming on a tree.

    Args:
        adj: Adjacency list
        process_node: Function that processes a node; args: node, parent, child_results
        root: Root node
        weighted: Whether the adjacency list contains weighted edges

    Returns:
        DP results for each node
    """
    n = len(adj)
    dp = [None] * n

    def _dfs(node: int, parent: int) -> Any:
        child_results = []
        for neighbor in adj[node]:
            if weighted:
                child, _ = neighbor  # Unpack (child, weight)
            else:
                child = neighbor

            if child != parent:
                child_results.append(_dfs(child, node))

        dp[node] = process_node(node, parent, child_results)
        return dp[node]

    _dfs(root, -1)
    return dp

def tree_dp_top_down(adj: List[List[int]], dp_bottom_up: List[Any], 
                     process_node: Callable[[int, int, Any, Any], Any], root: int = 0) -> List[Any]:
    """
    Top-down dynamic programming on a tree, after bottom-up pass.
    
    Args:
        adj: Adjacency list
        dp_bottom_up: Results from bottom-up DP
        process_node: Function that processes a node; args: node, parent, parent_result, bottom_up_result
        root: Root node
        
    Returns:
        DP results for each node
    """
    n = len(adj)
    dp = [None] * n
    
    def _dfs(node: int, parent: int, parent_result: Any):
        dp[node] = process_node(node, parent, parent_result, dp_bottom_up[node])
        
        for child in adj[node]:
            if child != parent:
                _dfs(child, node, dp[node])
    
    dp[root] = process_node(root, -1, None, dp_bottom_up[root])
    
    for child in adj[root]:
        _dfs(child, root, dp[root])
    
    return dp

def rerooting(adj: List[List[Any]], compute_subtree: Callable, merge_subtrees: Callable, 
             add_root_value: Callable, root: int = 0, weighted: bool = False) -> List[Any]:
    """
    Tree rerooting algorithm to efficiently calculate a result for each possible root.
    
    Args:
        adj: Adjacency list
        compute_subtree: Function to compute value for a subtree; args: node, parent
        merge_subtrees: Function to merge values from multiple subtrees; args: node, subtree_values
        add_root_value: Function to add value for current node as root; args: node, merged_value
        root: Initial root node
        weighted: Whether the adjacency list contains weighted edges
        
    Returns:
        List of results for each node as root
    """
    n = len(adj)
    subtree_results = [None] * n
    final_results = [None] * n
    
    # First pass: compute subtree results rooted at initial root
    def dfs1(node, parent):
        children_results = []
        
        for child_info in adj[node]:
            if weighted:
                child, weight = child_info
            else:
                child = child_info
                weight = 1
                
            if child != parent:
                child_result = dfs1(child, node)
                children_results.append(child_result)
        
        subtree_result = compute_subtree(node, children_results)
        subtree_results[node] = subtree_result
        return subtree_result
    
    dfs1(root, -1)
    
    # Second pass: reroot and calculate final results
    def dfs2(node, parent, parent_subtree):
        children_subtrees = []
        
        # Add contribution from parent
        if parent != -1:
            children_subtrees.append(parent_subtree)
        
        # Add contributions from children
        for child_info in adj[node]:
            if weighted:
                child, weight = child_info
            else:
                child = child_info
                weight = 1
                
            if child != parent:
                children_subtrees.append(subtree_results[child])
        
        # Merge results and add root value
        merged_result = merge_subtrees(node, children_subtrees)
        final_results[node] = add_root_value(node, merged_result)
        
        # Calculate parent subtree for children
        for child_info in adj[node]:
            if weighted:
                child, weight = child_info
            else:
                child = child_info
                weight = 1
                
            if child != parent:
                # Remove this child's subtree from parent's perspective
                new_parent_subtrees = children_subtrees.copy()
                new_parent_subtrees.remove(subtree_results[child])
                
                # Calculate new parent subtree for this child
                parent_subtree_for_child = merge_subtrees(node, new_parent_subtrees)
                dfs2(child, node, parent_subtree_for_child)
    
    dfs2(root, -1, None)
    return final_results

def iterative_dfs(adj: List[List[int]], start: int = 0) -> List[int]:
    """
    Perform iterative DFS traversal of a tree.
    
    Args:
        adj: Adjacency list representation of the tree
        start: Starting node
        
    Returns:
        List of nodes in DFS order
    """
    n = len(adj)
    visited = [False] * n
    result = []
    stack = [(start, -1)]  # (node, parent)
    
    while stack:
        node, parent = stack.pop()
        if not visited[node]:
            visited[node] = True
            result.append(node)
            
            for neighbor in reversed(adj[node]):
                if neighbor != parent and not visited[neighbor]:
                    stack.append((neighbor, node))
    
    return result

def iterative_postorder_dfs(adj: List[List[int]], start: int = 0) -> List[int]:
    """
    Perform iterative post-order DFS traversal of a tree.
    
    Args:
        adj: Adjacency list representation of the tree
        start: Starting node
        
    Returns:
        List of nodes in post-order
    """
    n = len(adj)
    visited = [False] * n
    result = []
    stack = [(start, -1, False)]  # (node, parent, is_processed)
    
    while stack:
        node, parent, is_processed = stack.pop()
        
        if is_processed:
            result.append(node)
        else:
            stack.append((node, parent, True))
            for neighbor in reversed(adj[node]):
                if neighbor != parent and not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append((neighbor, node, False))
    
    return result

# BFS traversal
def bfs(adj: List[List[int]], start: int = 0) -> List[int]:
    """
    Perform BFS traversal of a tree.
    
    Args:
        adj: Adjacency list representation of the tree
        start: Starting node
        
    Returns:
        List of nodes in BFS order
    """
    n = len(adj)
    visited = [False] * n
    result = []
    queue = deque([start])
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    return result

# Utility function for tail recursion optimization
def bootstrap(f):
    """
    Decorator for optimizing tail recursion.
    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        gen = f(*args, **kwargs)
        value = next(gen)
        while isinstance(value, Generator):
            value = next(value)
        return value
    return wrapper

def get_leaves(adj: List[List[int]]) -> List[int]:
    """
    Get all leaf nodes in a tree.
    
    Args:
        adj: Adjacency list representation of the tree
        
    Returns:
        List of leaf nodes
    """
    n = len(adj)
    leaves = []
    
    for i in range(n):
        if len(adj[i]) == 1 and i != 0:  # Assuming node 0 is root
            leaves.append(i)
    
    return leaves

def find_tree_diameter(adj: List[List[int]]) -> Tuple[int, List[int]]:
    """
    Find the diameter of a tree.
    
    Args:
        adj: Adjacency list representation of the tree
        
    Returns:
        Tuple containing the diameter length and the path
    """
    n = len(adj)
    
    # First BFS to find the farthest node from an arbitrary node
    def bfs_farthest(start):
        distances = [-1] * n
        parent = [-1] * n
        distances[start] = 0
        
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if distances[neighbor] == -1:
                    distances[neighbor] = distances[node] + 1
                    parent[neighbor] = node
                    queue.append(neighbor)
        
        # Find the farthest node
        farthest_node = 0
        for i in range(n):
            if distances[i] > distances[farthest_node]:
                farthest_node = i
        
        return farthest_node, distances, parent
    
    # Run first BFS from node 0
    farthest1, _, _ = bfs_farthest(0)
    
    # Run second BFS from the farthest node
    farthest2, distances, parent = bfs_farthest(farthest1)
    
    # Reconstruct the path
    path = []
    node = farthest2
    while node != -1:
        path.append(node)
        node = parent[node]
    
    return distances[farthest2], path

def tree_distance_calculator(adj: List[List[int]], root: int = 0):
    """
    Calculate distances between any two nodes in a tree efficiently.
    
    Args:
        adj: Adjacency list representation of the tree
        root: Root node
        
    Returns:
        Function that calculates distance between any two nodes
    """
    n = len(adj)
    
    # Calculate depths
    depths = [0] * n
    
    def calc_depths(node, parent, depth):
        depths[node] = depth
        for child in adj[node]:
            if child != parent:
                calc_depths(child, node, depth + 1)
    
    calc_depths(root, -1, 0)
    
    # Calculate ancestors for LCA
    log_n = 0
    while (1 << log_n) <= n:
        log_n += 1
    
    ancestors = [[-1] * log_n for _ in range(n)]
    
    def calc_ancestors(node, parent):
        ancestors[node][0] = parent
        for i in range(1, log_n):
            if ancestors[node][i-1] != -1:
                ancestors[node][i] = ancestors[ancestors[node][i-1]][i-1]
        
        for child in adj[node]:
            if child != parent:
                calc_ancestors(child, node)
    
    calc_ancestors(root, -1)
    
    # Function to find LCA
    def find_lca(u, v):
        if depths[u] < depths[v]:
            u, v = v, u
        
        # Bring u to the same depth as v
        diff = depths[u] - depths[v]
        for i in range(log_n):
            if diff & (1 << i):
                u = ancestors[u][i]
        
        if u == v:
            return u
        
        # Find LCA
        for i in range(log_n-1, -1, -1):
            if ancestors[u][i] != ancestors[v][i]:
                u = ancestors[u][i]
                v = ancestors[v][i]
        
        return ancestors[u][0]
    
    # Function to calculate distance
    def distance(u, v):
        lca = find_lca(u, v)
        return depths[u] + depths[v] - 2 * depths[lca]
    
    return distance

def tree_path_xor(adj: List[List[int]], values: List[int], root: int = 0):
    """
    Calculate XOR of values along any path in a tree.
    
    Args:
        adj: Adjacency list representation of the tree
        values: Value for each node
        root: Root node
        
    Returns:
        Function that calculates XOR along any path
    """
    n = len(adj)
    
    # Calculate prefix XORs
    prefix_xor = [0] * n
    
    def calc_prefix_xor(node, parent, current_xor):
        current_xor ^= values[node]
        prefix_xor[node] = current_xor
        
        for child in adj[node]:
            if child != parent:
                calc_prefix_xor(child, node, current_xor)
    
    calc_prefix_xor(root, -1, 0)
    
    # Get distance calculator for LCA
    dist_calc = tree_distance_calculator(adj, root)
    
    # Function to calculate path XOR
    def path_xor(u, v):
        lca = dist_calc(u, v)
        return prefix_xor[u] ^ prefix_xor[v] ^ values[lca]
    
    return path_xor

def identify_leaf_nodes(adj: List[List[int]]) -> List[int]:
    """
    Identify all leaf nodes in a tree.
    
    Args:
        adj: Adjacency list representation of the tree
        
    Returns:
        List of leaf node indices
    """
    n = len(adj)
    is_leaf = [False] * n
    
    for i in range(n):
        if len(adj[i]) == 1 and i != 0:  # Not root and has only one neighbor
            is_leaf[i] = True
    
    return is_leaf