"""
Library file for cluster3.
This contains shared code that can be imported by problems in this cluster.
"""
import os
import sys
from io import BytesIO, IOBase
from types import GeneratorType
from collections import defaultdict, deque
import heapq

# Fast IO for improved performance
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


def enable_fast_io():
    """
    Enable fast IO by replacing standard input/output and setting recursion limit.
    """
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    global input
    input = lambda: sys.stdin.readline().rstrip("\r\n")
    sys.setrecursionlimit(10**5)

# Recursion optimization with trampolining
def bootstrap(f, stack=[]):
    """
    Decorator that enables trampolining for recursive functions to avoid stack overflow.
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

# IO utilities
def read_int():
    """Read a single integer."""
    return int(input())

def read_ints():
    """Read multiple integers on a single line."""
    return list(map(int, input().split()))

def read_int_tuple():
    """Read multiple integers as a tuple."""
    return tuple(map(int, input().split()))

def read_matrix(n, convert=int):
    """Read n lines as a matrix with optional conversion."""
    return [list(map(convert, input().split())) for _ in range(n)]

# Tree utilities
def build_tree(n, edges=None, one_indexed=True):
    """
    Build a tree as an adjacency list.
    If edges is None, read (n-1) edges from input.
    """
    adj = [[] for _ in range(n + (1 if one_indexed else 0))]
    
    if edges is None:
        for _ in range(n - 1):
            u, v = read_int_tuple()
            if one_indexed:
                u -= 1
                v -= 1
            adj[u].append(v)
            adj[v].append(u)
    else:
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
    return adj

def dfs_iterative(graph, start=0, visited=None):
    """
    Iterative DFS traversal of a graph/tree.
    """
    if visited is None:
        visited = [False] * len(graph)
    
    stack = [start]
    visited[start] = True
    result = []
    
    while stack:
        node = stack.pop()
        result.append(node)
        
        for neighbor in reversed(graph[node]):
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
                
    return result

def dfs_postorder_iterative(graph, start=0):
    """
    Iterative post-order DFS traversal of a graph/tree.
    """
    n = len(graph)
    visited = [False] * n
    stack = [start]
    visited[start] = True
    result = []
    
    while stack:
        node = stack[-1]
        is_leaf = True
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
                is_leaf = False
                break
                
        if is_leaf:
            result.append(stack.pop())
            
    return result

def bfs(graph, start=0):
    """
    BFS traversal of a graph/tree.
    """
    n = len(graph)
    visited = [False] * n
    queue = deque([start])
    visited[start] = True
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                
    return result

def subtree_size(graph, root=0, parent=-1):
    """
    Calculate the size of each subtree rooted at each node.
    """
    n = len(graph)
    size = [1] * n
    
    def dfs(node, parent):
        for child in graph[node]:
            if child != parent:
                dfs(child, node)
                size[node] += size[child]
    
    dfs(root, parent)
    return size

def subtree_size_iterative(graph, root=0):
    """
    Calculate the size of each subtree rooted at each node using iterative approach.
    """
    n = len(graph)
    size = [1] * n
    visited = [False] * n
    stack = [root]
    parent = [-1] * n
    
    # First pass: assign parents
    visited[root] = True
    while stack:
        node = stack.pop()
        for child in graph[node]:
            if not visited[child]:
                parent[child] = node
                visited[child] = True
                stack.append(child)
    
    # Second pass: calculate sizes from bottom up
    visited = [False] * n
    stack = []
    
    # Add leaf nodes to the stack
    for i in range(n):
        if all(child == parent[i] or not visited[child] for child in graph[i]):
            stack.append(i)
            visited[i] = True
    
    while stack:
        node = stack.pop()
        if parent[node] != -1:
            size[parent[node]] += size[node]
            # If all children of parent are processed, add parent to stack
            if all(child == node or visited[child] for child in graph[parent[node]]):
                if not visited[parent[node]]:
                    stack.append(parent[node])
                    visited[parent[node]] = True
    
    return size

@bootstrap
def subtree_size_trampolined(graph, node=0, parent=-1):
    """
    Calculate the size of each subtree using trampolining to avoid stack overflow.
    """
    n = len(graph)
    size = [1] * n
    
    for child in graph[node]:
        if child != parent:
            yield subtree_size_trampolined(graph, child, node)
            size[node] += size[child]
            
    yield size

def tree_diameter(graph):
    """
    Calculate the diameter of a tree.
    Returns both the diameter and the endpoints.
    """
    n = len(graph)
    
    # First BFS to find the farthest node from any starting point
    dist = [-1] * n
    dist[0] = 0
    queue = deque([0])
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    
    # Find the farthest node
    farthest = dist.index(max(dist))
    
    # Second BFS from the farthest node
    dist = [-1] * n
    dist[farthest] = 0
    queue = deque([farthest])
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    
    # The diameter is the maximum distance and the endpoints are farthest and the node with max dist
    diameter = max(dist)
    endpoint = dist.index(diameter)
    
    return diameter, (farthest, endpoint)

def rerooting_dp(graph, node_values, combine_func, update_func=lambda x: x):
    """
    Dynamic programming with rerooting technique for trees.
    compute_dp is a function that computes the dp value for a node with its children
    update_func is a function that updates the dp value when rerooting
    """
    n = len(graph)
    
    # First pass: compute dp values from leaves to root
    dp = [0] * n
    
    def dfs1(node, parent):
        dp[node] = node_values[node]
        
        for child in graph[node]:
            if child != parent:
                dfs1(child, node)
                dp[node] = combine_func(dp[node], dp[child])
    
    # Second pass: reroot and recalculate dp values
    result = [0] * n
    
    def dfs2(node, parent, parent_result):
        result[node] = dp[node]
        
        if parent != -1:
            result[node] = combine_func(result[node], update_func(parent_result))
        
        for child in graph[node]:
            if child != parent:
                new_parent_result = combine_func(result[node] - dp[child], update_func(dp[child]))
                dfs2(child, node, new_parent_result)
    
    dfs1(0, -1)
    dfs2(0, -1, 0)
    
    return result

# Maximum white-black subtree problem functions
@bootstrap
def white_black_subtree_dp(graph, colors, node=1, parent=0):
    """
    First DFS to compute maximum subtree sum (white-black) rooted at each node.
    
    Args:
        graph: Adjacency list representation of the tree
        colors: Array of node colors (1 for white, 0 for black)
        node: Current node
        parent: Parent of current node
    
    Returns:
        Array of maximum subtree sums for each node
    """
    n = len(graph)
    dp = [0] * n
    
    # Convert colors to +1/-1
    color_values = [0] * n
    for i in range(1, n):
        color_values[i] = 1 if colors[i] == 1 else -1
    
    def dfs(node, parent):
        # Initialize with node's own value
        dp[node] = color_values[node]
        
        for child in graph[node]:
            if child != parent:
                yield dfs(child, node)
                # Only include positive contributions
                dp[node] += max(0, dp[child])
        
        yield
    
    yield dfs(node, parent)
    yield dp

@bootstrap
def white_black_subtree_reroot(graph, dp, node=1, parent=0, parent_contribution=0):
    """
    Second DFS to reroot the tree and compute final answers.
    
    Args:
        graph: Adjacency list representation of the tree
        dp: Array of maximum subtree sums computed by white_black_subtree_dp
        node: Current node
        parent: Parent of current node
        parent_contribution: Contribution from parent's subtree
    
    Returns:
        Array of maximum subtree sums for each node after rerooting
    """
    n = len(graph)
    result = [0] * n
    
    def dfs(node, parent, parent_contribution):
        # Calculate result for current node
        result[node] = dp[node]
        if parent_contribution > 0:
            result[node] += parent_contribution
        
        for child in graph[node]:
            if child != parent:
                # Calculate contribution excluding current child
                new_parent_contribution = dp[node]
                if dp[child] > 0:
                    new_parent_contribution -= dp[child]
                
                # Add parent's contribution if positive
                if parent_contribution > 0:
                    new_parent_contribution += parent_contribution
                
                yield dfs(child, node, new_parent_contribution)
        
        yield
    
    yield dfs(node, parent, parent_contribution)
    yield result

# Subtree operations
def count_leaves(graph, root=0):
    """
    Count the number of leaf nodes in a tree.
    """
    n = len(graph)
    is_leaf = [True] * n
    
    for node in range(n):
        for neighbor in graph[node]:
            if neighbor != node:  # Avoid self-loops
                is_leaf[node] = False
    
    # Root is not a leaf if it has any children
    if graph[root]:
        is_leaf[root] = False
        
    return sum(is_leaf)

def tree_centers(graph):
    """
    Find the center(s) of a tree.
    """
    n = len(graph)
    degree = [0] * n
    leaves = []
    
    # Count degrees and find leaves
    for i in range(n):
        degree[i] = len(graph[i])
        if degree[i] <= 1:
            leaves.append(i)
    
    remaining_nodes = n
    
    # Remove leaf nodes layer by layer
    while remaining_nodes > 2:
        remaining_nodes -= len(leaves)
        new_leaves = []
        
        for leaf in leaves:
            for neighbor in graph[leaf]:
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    new_leaves.append(neighbor)
        
        leaves = new_leaves
    
    return leaves  # Contains 1 or 2 center nodes

def tree_traversal_preorder(graph, start=0, parent=-1):
    """
    Preorder traversal of a tree.
    """
    result = [start]
    
    for child in graph[start]:
        if child != parent:
            result.extend(tree_traversal_preorder(graph, child, start))
    
    return result

def tree_traversal_postorder(graph, start=0, parent=-1):
    """
    Postorder traversal of a tree.
    """
    result = []
    
    for child in graph[start]:
        if child != parent:
            result.extend(tree_traversal_postorder(graph, child, start))
    
    result.append(start)
    return result

def level_order_traversal(graph, start=0):
    """
    Level order traversal of a tree.
    """
    n = len(graph)
    visited = [False] * n
    queue = deque([start])
    visited[start] = True
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    return result

def lowest_common_ancestor(graph, u, v, root=0):
    """
    Find the lowest common ancestor of nodes u and v.
    """
    n = len(graph)
    
    # Create parent and depth arrays
    parent = [-1] * n
    depth = [-1] * n
    
    def dfs(node, p, d):
        parent[node] = p
        depth[node] = d
        
        for child in graph[node]:
            if child != p:
                dfs(child, node, d + 1)
    
    dfs(root, -1, 0)
    
    # Make u the deeper node
    if depth[u] < depth[v]:
        u, v = v, u
    
    # Move u up to the same depth as v
    while depth[u] > depth[v]:
        u = parent[u]
    
    # Move both up until they meet
    while u != v:
        u = parent[u]
        v = parent[v]
    
    return u

def build_tree_with_parent(graph, root=0):
    """
    Build a tree with parent pointers.
    Returns parent array where parent[i] is the parent of node i.
    """
    n = len(graph)
    parent = [-1] * n
    visited = [False] * n
    stack = [root]
    visited[root] = True
    
    while stack:
        node = stack.pop()
        for child in graph[node]:
            if not visited[child]:
                parent[child] = node
                visited[child] = True
                stack.append(child)
    
    return parent

def tree_depth(graph, root=0):
    """
    Calculate the depth of each node from the root.
    """
    n = len(graph)
    depth = [-1] * n
    depth[root] = 0
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        for child in graph[node]:
            if depth[child] == -1:
                depth[child] = depth[node] + 1
                queue.append(child)
    
    return depth

def find_tree_distances(graph, root=0):
    """
    Find distances from each node to every other node in the tree.
    Returns a matrix where dist[i][j] is the distance from node i to node j.
    """
    n = len(graph)
    dist = [[-1] * n for _ in range(n)]
    
    # Initialize with 0 for self-distance
    for i in range(n):
        dist[i][i] = 0
    
    # Perform BFS from each node
    for start in range(n):
        queue = deque([start])
        visited = [False] * n
        visited[start] = True
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dist[start][neighbor] = dist[start][node] + 1
                    queue.append(neighbor)
    
    return dist

def find_kth_ancestor(parent, node, k):
    """
    Find the k-th ancestor of a node.
    
    Args:
        parent: Parent array where parent[i] is the parent of node i
        node: The node to find the ancestor for
        k: The number of steps to go up
        
    Returns:
        The k-th ancestor or -1 if it doesn't exist
    """
    for _ in range(k):
        if node == -1:
            break
        node = parent[node]
    return node

def compute_tree_dp_postorder(graph, node_values, combine_func, root=0, parent=-1):
    """
    Compute dynamic programming values on a tree using post-order traversal.

    Args:
        graph: Adjacency list representation of the tree
        node_values: Initial values for each node
        combine_func: Function to combine DP values
        root: Root node
        parent: Parent of root (usually -1)

    Returns:
        Array of DP values for each node
    """
    n = len(graph)
    dp = node_values.copy()

    def dfs(node, parent):
        for child in graph[node]:
            if child != parent:
                dfs(child, node)
                dp[node] = combine_func(dp[node], dp[child])

    dfs(root, parent)
    return dp

def parsas_tree_max_beauty(graph, bounds):
    """
    Solve Parsa's Humongous Tree problem using tree DP.

    Args:
        graph: Adjacency list representation of the tree
        bounds: List of (l, r) bounds for each vertex

    Returns:
        Maximum possible beauty of the tree
    """
    n = len(graph)
    root = 0

    # dp[node][0] = max beauty if node gets l_node
    # dp[node][1] = max beauty if node gets r_node
    dp = [[0, 0] for _ in range(n)]

    # We'll use an iterative approach with a stack to avoid stack overflow
    par = [-1] * n
    stack = []
    stack.append(~0)  # Use complement to mark nodes for post-processing
    stack.append(0)

    while stack:
        v = stack.pop()

        if v >= 0:
            # First visit: push all children to stack
            for u in graph[v]:
                if u == par[v]:
                    continue
                par[u] = v
                stack.append(~u)  # Mark for post-processing
                stack.append(u)
        else:
            # Post-processing: update DP values
            u = ~v  # Child node
            v = par[u]  # Parent node

            if v == -1:
                continue  # Root node

            l_v, r_v = bounds[v]
            l_u, r_u = bounds[u]

            # If parent chooses l_v, max beauty from this child
            zero = max(dp[u][0] + abs(l_v - l_u), dp[u][1] + abs(l_v - r_u))

            # If parent chooses r_v, max beauty from this child
            one = max(dp[u][0] + abs(r_v - l_u), dp[u][1] + abs(r_v - r_u))

            dp[v][0] += zero
            dp[v][1] += one

    # Return the maximum of the two possibilities for the root
    return max(dp[0])

def min_max_depth_leaves(graph, root=0):
    """
    Find the minimum and maximum depth of leaves in a tree.
    Returns (min_depth, max_depth)
    """
    n = len(graph)
    min_depth = float('inf')
    max_depth = 0

    def dfs(node, parent, depth):
        nonlocal min_depth, max_depth

        is_leaf = True
        for child in graph[node]:
            if child != parent:
                is_leaf = False
                dfs(child, node, depth + 1)

        if is_leaf and node != root:
            min_depth = min(min_depth, depth)
            max_depth = max(max_depth, depth)

    dfs(root, -1, 0)
    return min_depth, max_depth

def max_product_components(graph):
    """
    Calculate the maximum product of components after removing some edges.

    This function implements a dynamic programming approach to find the
    maximum possible product of connected component sizes after removing
    some edges from a tree.

    Args:
        graph: Adjacency list representation of the tree

    Returns:
        Maximum possible product of connected component sizes
    """
    from fractions import Fraction

    n = len(graph)

    # Initialize arrays
    H = [0] * n  # Maximum product ending at node i
    F = [0] * n  # Product of H values of children
    FoH = [[] for _ in range(n)]  # List of F[v]/H[v] for each child

    # Perform DFS to get a post-order traversal
    order = []
    parent = [-1] * n

    def dfs(node, p=-1):
        parent[node] = p
        for neighbor in graph[node]:
            if neighbor != p:
                dfs(neighbor, node)
        order.append(node)

    dfs(0)

    # Process nodes in post-order
    for node in order:
        p = parent[node]
        F[node] = 1

        # Calculate F[node] and collect F[child]/H[child] ratios
        for child in graph[node]:
            if child != p:
                F[node] *= H[child]
                FoH[node].append(Fraction(F[child], H[child]))

        # Initial answer is just F[node]
        answer = F[node]

        # Sort the ratios in descending order
        FoH[node].sort(reverse=True)

        # Try keeping some subtrees together
        product = 1
        subtree_count = 0

        for ratio in FoH[node]:
            product *= ratio
            subtree_count += 1
            # Calculate new answer with (subtree_count + 1) components
            # (the +1 is for the current node itself)
            answer = max(answer, int(product * F[node]) * (subtree_count + 1))

        # Try merging with a child's subtree
        for child in graph[node]:
            if child != p:
                product = 1
                subtree_count = 0

                for ratio in FoH[child]:
                    product *= ratio
                    subtree_count += 1
                    # Calculate new answer with (subtree_count + 2) components
                    # (the +2 is for the current node and the current child)
                    new_answer = int(product * F[node] * F[child]) // H[child] * (subtree_count + 2)
                    answer = max(answer, new_answer)

        # Store the maximum product for this node
        H[node] = answer

    return H[0]

def dog_snacks_min_k(graph, with_1_indexing=True):
    """
    Calculate the minimum k for Dog Snacks problem.
    Returns the minimum k value.

    This function solves the problem where:
    - Dog Badugi needs to eat all snacks starting from node 1
    - Badugi can only sense snacks within k distance
    - We want to find the minimum k to complete the mission

    Args:
        graph: Adjacency list representation of the tree (0-indexed or 1-indexed)
        with_1_indexing: Whether the input graph uses 1-indexed nodes

    Returns:
        Minimum possible value of k
    """
    if with_1_indexing:
        # Create a 1-indexed copy of the adjacency list (exact copy)
        n = len(graph) - 1  # Actual number of nodes
        tree = graph
        root = 1
    else:
        # Convert to 1-indexed for our implementation
        n = len(graph)
        tree = [[] for _ in range(n + 1)]
        for node in range(n):
            for neighbor in graph[node]:
                tree[node + 1].append(neighbor + 1)
        root = 1

    # Track degree of each node
    degree = [0] * (n + 1)
    degree[root] = 1  # Root starts with degree 1

    # Track parent of each node
    parent = [0] * (n + 1)

    # DFS to build parent relationships and count degrees
    stack = [root]
    leaf_nodes = []

    while stack:
        node = stack.pop()
        for child in tree[node]:
            if child != parent[node]:
                degree[node] += 1
                parent[child] = node
                stack.append(child)

        if degree[node] == 0:  # Leaf node
            leaf_nodes.append(node)

    # Tracks (distance_to_leaf, max_path)
    subtree_data = [[] for _ in range(n + 1)]

    # Bottom-up DP calculation
    while leaf_nodes:
        node = leaf_nodes.pop()
        p = parent[node]

        if not subtree_data[node]:  # Node is a leaf
            subtree_data[p].append((1, 0))
        elif len(subtree_data[node]) == 1:  # Node has one child
            d, k = subtree_data[node][0]
            subtree_data[p].append((d + 1, k))
        else:  # Node has multiple children
            d = min(data[0] for data in subtree_data[node]) + 1
            k = max(
                max(data[1] for data in subtree_data[node]),  # Max of child paths
                max(data[0] for data in subtree_data[node]) + 1  # Max dist + 1
            )
            subtree_data[p].append((d, k))

        degree[p] -= 1
        if degree[p] == 0:
            leaf_nodes.append(p)

    # Calculate result for root (node 1)
    if len(subtree_data[root]) == 1:
        return max(subtree_data[root][0])
    else:
        k = max(data[1] for data in subtree_data[root])
        distances = [data[0] for data in subtree_data[root]]
        m = max(distances)
        distances.remove(m)
        return max(max(distances)+1, m, k)

def rooted_tree_game_theory(graph, node_values, k, root=0):
    """
    Compute dynamic programming for tree game theory problems with rerooting.
    
    Args:
        graph: Adjacency list representation of the tree
        node_values: Values for each node
        k: Parameter for game rules
        root: Root node
        
    Returns:
        Array with the game result for each possible root
    """
    n = len(graph)
    dp = [[0] * (2*k) for _ in range(n)]
    
    # Build a tree with BFS to get vertices in level-order
    vertices = []
    queue = deque([root])
    visited = [False] * n
    visited[root] = True
    parent = [-1] * n
    
    while queue:
        node = queue.popleft()
        vertices.append(node)
        
        for child in graph[node]:
            if not visited[child]:
                visited[child] = True
                parent[child] = node
                queue.append(child)
    
    # First DP pass - bottom-up
    for i in range(n-1, -1, -1):
        node = vertices[i]
        dp[node][0] ^= node_values[node]
        
        for child in graph[node]:
            if child != parent[node]:
                for j in range(2*k):
                    dp[node][(j+1) % (2*k)] ^= dp[child][j]
    
    # Second DP pass - rerooting
    result = [0] * n
    
    for v in vertices:
        if v == root:
            # Compute result for root
            result[v] = 0
            for i in range(k, 2*k):
                result[v] ^= dp[v][i]
            result[v] = min(result[v], 1)
        else:
            # Reroot to v
            p = parent[v]
            pcopy = dp[p].copy()
            
            # Remove v's contribution from p
            for i in range(2*k):
                pcopy[(i+1) % (2*k)] ^= dp[v][i]
            
            # Add p's contribution to v
            for i in range(2*k):
                dp[v][(i+1) % (2*k)] ^= pcopy[i]
            
            # Compute result for v
            result[v] = 0
            for i in range(k, 2*k):
                result[v] ^= dp[v][i]
            result[v] = min(result[v], 1)
    
    return result

def diameter_cuts(graph, k, root=0):
    """
    Calculate the number of ways to cut a tree into subtrees, each with diameter <= k.

    This is a dynamic programming approach where:
    - We process nodes in bottom-up order (post-order traversal)
    - For each node, we compute ways to arrange cuts for its subtree
    - We merge child DP values into parent DP values

    Args:
        graph: Adjacency list representation of the tree
        k: Maximum allowed diameter
        root: Root node (default 0)

    Returns:
        Number of valid sets of edges mod 998244353
    """
    n = len(graph)
    MOD = 998244353

    # BFS to get nodes in level order and build parent array
    parent = [-1] * n
    queue = deque([root])
    nodes_order = []

    while queue:
        node = queue.popleft()
        nodes_order.append(node)
        for neighbor in graph[node]:
            if neighbor != parent[node]:
                parent[neighbor] = node
                queue.append(neighbor)

    # DP array: dp[node][i] = number of ways to cut with diameter i
    dp = [[1] for _ in range(n)]

    # Merge function to combine DP values of node v with its child nv
    def merge(v, nv):
        # Create a new DP array for node v after merging with child nv
        max_len = max(len(dp[v]), len(dp[nv]) + 1)
        new_dp = [0] * max_len

        for i in range(len(dp[v])):
            for j in range(len(dp[nv])):
                # Case 1: We include the edge to child (diameter = max(j+1, i))
                if j + 1 + i <= k:
                    new_dp[max(j + 1, i)] = (new_dp[max(j + 1, i)] + dp[v][i] * dp[nv][j]) % MOD

                # Case 2: We cut the edge to child (diameter = i)
                new_dp[i] = (new_dp[i] + dp[v][i] * dp[nv][j]) % MOD

        dp[v] = new_dp

    # Process nodes in reverse order (bottom-up)
    for node in reversed(nodes_order):
        for child in graph[node]:
            if child != parent[node]:
                merge(node, child)

    # Calculate final answer (sum of ways with diameter <= k)
    result = sum(dp[root][i] for i in range(min(k + 1, len(dp[root])))) % MOD
    return result