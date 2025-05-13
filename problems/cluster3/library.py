"""
Library file for cluster3.
This contains shared code that can be imported by problems in this cluster.
"""
import os
import sys
from io import BytesIO, IOBase
from types import GeneratorType
from collections import defaultdict, deque
import math


###################
# Fast I/O        #
###################

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


###################
# Tree Utilities  #
###################

def build_tree(n, edges=None, one_indexed=True):
    """
    Build adjacency list representation of a tree.

    Args:
        n: Number of nodes
        edges: List of edge tuples (u, v) or None to read from input
        one_indexed: Whether node indices start from 1 (True) or 0 (False)

    Returns:
        Adjacency list representation of the tree
    """
    adj = [[] for _ in range(n + (1 if one_indexed else 0))]

    if edges is None:
        for _ in range(n - 1):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
    else:
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

    return adj


def build_weighted_tree(n, weighted=False, one_indexed=True):
    """
    Build adjacency list representation of a tree with optional weights.

    Args:
        n: Number of nodes
        weighted: Whether edges have weights
        one_indexed: Whether node indices start from 1 (True) or 0 (False)

    Returns:
        Adjacency list representation of the tree
    """
    offset = 1 if one_indexed else 0
    adj = [[] for _ in range(n + offset)]

    for _ in range(n - 1):
        if weighted:
            u, v, w = map(int, input().split())
            if one_indexed:
                u -= offset
                v -= offset
            adj[u].append((v, w))
            adj[v].append((u, w))
        else:
            u, v = map(int, input().split())
            if one_indexed:
                u -= offset
                v -= offset
            adj[u].append(v)
            adj[v].append(u)

    return adj


def build_directed_tree(n, edges=None, one_indexed=True):
    """
    Build adjacency list representation of a directed tree (e.g., rooted tree).

    Args:
        n: Number of nodes
        edges: List of edge tuples (parent, child) or None to read from input
        one_indexed: Whether node indices start from 1 (True) or 0 (False)

    Returns:
        Adjacency list representation of the directed tree
    """
    offset = 1 if one_indexed else 0
    adj = [[] for _ in range(n + offset)]

    if edges is None:
        parents = list(map(int, input().split()))
        for i, p in enumerate(parents, start=2 if one_indexed else 1):
            adj[p].append(i)
            # Note: no reverse edge added for directed tree
    else:
        for p, c in edges:
            adj[p].append(c)

    return adj


def read_tree_parent_format(n, one_indexed=True):
    """
    Read tree in parent array format (common in competitive programming).
    Parent array format: [p_2, p_3, ..., p_n] where p_i is the parent of node i.

    Args:
        n: Number of nodes
        one_indexed: Whether node indices start from 1 (True) or 0 (False)

    Returns:
        Adjacency list representation of the tree
    """
    offset = 1 if one_indexed else 0
    adj = [[] for _ in range(n + offset)]

    if n <= 1:
        return adj

    parents = list(map(int, input().split()))

    for i, p in enumerate(parents, start=2 if one_indexed else 1):
        adj[p].append(i)
        adj[i].append(p)  # Add reverse edge for undirected tree

    return adj


def read_tree_values(n, one_indexed=True):
    """
    Read values for tree nodes

    Args:
        n: Number of nodes
        one_indexed: Whether node indices start from 1 (True) or 0 (False)

    Returns:
        List of values for each node
    """
    values = list(map(int, input().split()))
    if one_indexed:
        return [0] + values  # Add dummy value at index 0
    return values


def get_parent_array(adj, root=0):
    """
    Convert adjacency list to parent array.

    Args:
        adj: Adjacency list representation of the tree
        root: Root node

    Returns:
        Parent array where parent[i] is the parent of node i
    """
    n = len(adj)
    parent = [-1] * n
    visited = [False] * n

    queue = deque([root])
    visited[root] = True

    while queue:
        node = queue.popleft()
        for neighbor in adj[node]:
            if not visited[neighbor]:
                parent[neighbor] = node
                visited[neighbor] = True
                queue.append(neighbor)

    return parent


def get_children_array(parent, start_idx=0):
    """
    Convert parent array to children lists.

    Args:
        parent: Parent array where parent[i] is the parent of node i
        start_idx: Starting index for result (0 or 1 for 0/1-indexed)

    Returns:
        List of lists where children[i] contains all children of node i
    """
    n = len(parent)
    children = [[] for _ in range(n)]

    for i in range(start_idx, n):
        if parent[i] != -1:  # Not the root
            children[parent[i]].append(i)

    return children


###################
# Tree Traversal  #
###################

def dfs(adj, start=1, visited=None):
    """
    Iterative DFS traversal

    Args:
        adj: Adjacency list representation of the tree
        start: Starting node
        visited: Visited array or None to create a new one

    Returns:
        List of visited nodes in DFS order
    """
    if visited is None:
        visited = [False] * len(adj)

    result = []
    stack = [start]

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            result.append(node)

            # Add neighbors in reverse order to process them in original order
            for neighbor in reversed(adj[node]):
                if not visited[neighbor]:
                    stack.append(neighbor)

    return result


def dfs_with_parent(adj, start=0):
    """
    DFS traversal returning visit order and parent array

    Args:
        adj: Adjacency list representation of the tree
        start: Starting node (root)

    Returns:
        Tuple of (visit order, parent array)
    """
    n = len(adj)
    visited = [False] * n
    parent = [-1] * n
    order = []

    stack = [start]
    visited[start] = True

    while stack:
        node = stack.pop()
        order.append(node)

        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = node
                stack.append(neighbor)

    return order, parent


def bfs(adj, start=1):
    """
    BFS traversal

    Args:
        adj: Adjacency list representation of the tree
        start: Starting node

    Returns:
        List of visited nodes in BFS order
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


def bfs_with_depth(adj, start=0):
    """
    BFS traversal that also calculates depths

    Args:
        adj: Adjacency list representation of the tree
        start: Starting node (root)

    Returns:
        List of depths for each node
    """
    n = len(adj)
    visited = [False] * n
    depth = [-1] * n
    depth[start] = 0

    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()

        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                depth[neighbor] = depth[node] + 1
                queue.append(neighbor)

    return depth


def bootstrap(f, stack=[]):
    """
    Decorator to make a recursive function non-recursive (trampoline)
    Useful for deep recursion in competitive programming

    Args:
        f: Function to be wrapped
        stack: Stack for trampolining

    Returns:
        Wrapped non-recursive function
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


###################
# Tree Algorithms #
###################

def calculate_subtree_sizes(adj, root=1):
    """
    Calculate subtree sizes for each node

    Args:
        adj: Adjacency list representation of the tree
        root: Root node

    Returns:
        List of subtree sizes for each node
    """
    n = len(adj)
    sizes = [0] * n
    visited = [False] * n

    def dfs_subtree(node):
        visited[node] = True
        sizes[node] = 1

        for child in adj[node]:
            if not visited[child]:
                dfs_subtree(child)
                sizes[node] += sizes[child]

    dfs_subtree(root)
    return sizes


def calculate_subtree_sizes_iterative(adj, root=1):
    """
    Calculate subtree sizes using iterative approach

    Args:
        adj: Adjacency list representation of the tree
        root: Root node

    Returns:
        List of subtree sizes for each node
    """
    n = len(adj)
    sizes = [0] * n
    visited = [False] * n
    parent = [-1] * n

    # First DFS to establish parent-child relationships
    stack = [root]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            for child in adj[node]:
                if not visited[child]:
                    parent[child] = node
                    stack.append(child)

    # Reset visited array for second DFS
    visited = [False] * n

    # Post-order traversal (from leaves to root)
    stack = [root]
    post_order = []

    while stack:
        node = stack[-1]
        if not visited[node]:
            visited[node] = True
            for child in adj[node]:
                if child != parent[node] and not visited[child]:
                    stack.append(child)
        else:
            post_order.append(stack.pop())

    # Calculate subtree sizes
    sizes = [1] * n  # Initialize with 1 (every node counts itself)

    # Process nodes in post-order (from leaves to root)
    for node in post_order:
        if parent[node] != -1:  # If not root
            sizes[parent[node]] += sizes[node]

    return sizes


def tree_diameter(adj):
    """
    Calculate the diameter of a tree (longest path between any two nodes)

    Args:
        adj: Adjacency list representation of the tree

    Returns:
        The diameter of the tree (length of the longest path)
    """
    # Step 1: Find the farthest node from any arbitrary node
    def bfs_farthest(start):
        n = len(adj)
        dist = [-1] * n
        dist[start] = 0
        queue = deque([start])

        while queue:
            node = queue.popleft()

            for neighbor in adj[node]:
                if dist[neighbor] == -1:
                    dist[neighbor] = dist[node] + 1
                    queue.append(neighbor)

        farthest_node = dist.index(max(dist))
        return farthest_node, dist[farthest_node]

    # Find farthest node from node 1 (or 0 if 0-indexed)
    node1, _ = bfs_farthest(1 if len(adj) > 1 else 0)
    # Find farthest node from node1
    _, diameter = bfs_farthest(node1)

    return diameter


def count_subtree_leaves(adj, root=1):
    """
    Count the number of leaves in each subtree

    Args:
        adj: Adjacency list representation of the tree
        root: Root node

    Returns:
        List with count of leaves in subtree rooted at each node
    """
    n = len(adj)
    leaf_count = [0] * n
    visited = [False] * n

    # Find all leaves first
    leaves = []
    for i in range(1, n):
        # If a node has only one neighbor and is not the root, it's a leaf
        if i != root and len(adj[i]) == 1:
            leaves.append(i)
            leaf_count[i] = 1

    # Special case for single node tree
    if n <= 2:
        return leaf_count

    # DFS to calculate leaf counts for internal nodes
    def dfs(node, parent):
        visited[node] = True
        for child in adj[node]:
            if child != parent and not visited[child]:
                dfs(child, node)
                leaf_count[node] += leaf_count[child]

        # If this node is not a leaf but has no leaves in its subtree,
        # mark it as having 1 leaf (itself)
        if leaf_count[node] == 0:
            leaf_count[node] = 1

    dfs(root, -1)
    return leaf_count


def rerooting(adj, values=None, one_indexed=True):
    """
    Tree rerooting technique - prepare for rerooting and DP on trees

    Args:
        adj: Adjacency list representation of the tree
        values: Values for each node or None
        one_indexed: Whether node indices start from 1 (True) or 0 (False)

    Returns:
        Subtree sizes, DP array and a function to reroot
    """
    n = len(adj) - (1 if one_indexed else 0)
    offset = 1 if one_indexed else 0

    if values is None:
        values = [1] * (n + offset)

    subtree_size = [0] * (n + offset)
    dp = [0] * (n + offset)

    @bootstrap
    def dfs1(node, parent=None):
        subtree_size[node] = values[node]
        for child in adj[node]:
            if child != parent:
                yield dfs1(child, node)
                subtree_size[node] += subtree_size[child]
                dp[node] += dp[child] + subtree_size[child]
        yield

    @bootstrap
    def dfs2(node, parent=None):
        for child in adj[node]:
            if child != parent:
                dp[child] = dp[node] - subtree_size[child] + (n - subtree_size[child])
                yield dfs2(child, node)
        yield

    dfs1(offset)

    def get_reroot_dp():
        """
        Calculate DP values for all possible roots
        """
        dfs2(offset)
        return dp

    return subtree_size, dp, get_reroot_dp


###################
# Specialized     #
# Tree Algorithms #
###################

def tree_painting_rerooting(adj, root=0):
    """
    Specialized rerooting technique for tree painting problem (Codeforces 1187E)

    Args:
        adj: Adjacency list representation of the tree (0-indexed)
        root: Root node

    Returns:
        Maximum score achievable
    """
    n = len(adj)

    # Calculate subtree sizes
    subtree_size = calculate_subtree_sizes_iterative(adj, root)

    # Calculate initial DP values (sum of subtree sizes for the subtree rooted at each node)
    dp = [0] * n
    visited = [False] * n
    stack = [root]

    while stack:
        node = stack[-1]
        if not visited[node]:
            visited[node] = True
            for child in adj[node]:
                if not visited[child]:
                    stack.append(child)
        else:
            node = stack.pop()
            dp[node] = subtree_size[node]
            for child in adj[node]:
                if visited[child] and child not in stack:
                    dp[node] += dp[child]

    # Reroot and find maximum score
    max_score = dp[root]
    ans = [0] * n
    ans[root] = dp[root]
    stack = [root]
    visited = [False] * n
    visited[root] = True

    while stack:
        node = stack.pop()
        for child in adj[node]:
            if not visited[child]:
                # Recalculate score for child as root
                child_score = ans[node] + n - 2 * subtree_size[child]
                ans[child] = child_score
                max_score = max(max_score, child_score)
                visited[child] = True
                stack.append(child)

    return max_score


def maximum_white_subtree(adj, colors, root=0):
    """
    Calculate maximum white-black difference for subtrees containing each node
    (Codeforces 1324F)

    Args:
        adj: Adjacency list representation of the tree (0-indexed)
        colors: List of node colors (0 for black, 1 for white)
        root: Root node

    Returns:
        List of maximum white-black differences for each node
    """
    n = len(adj)

    # Convert colors: 0 (black) -> -1 for easier white-black difference calculation
    values = colors.copy()
    for i in range(n):
        if values[i] == 0:
            values[i] = -1

    # First pass: calculate the maximum score for each subtree rooted at each node
    dp = [0] * n

    @bootstrap
    def dfs1(node, parent):
        # Initialize DP with current node color
        dp[node] = values[node]

        # Process all children
        for child in adj[node]:
            if child != parent:
                # Recursively process child subtree
                yield dfs1(child, node)

                # Only include child subtree if it increases our score
                if dp[child] > 0:
                    dp[node] += dp[child]
        yield

    # Second pass: rerooting to calculate answer for each node
    ans = [0] * n

    @bootstrap
    def dfs2(node, parent):
        # For each child, we need to calculate what the parent would contribute if we reroot at child
        for child in adj[node]:
            if child != parent:
                # Save original values
                orig_dp_node = dp[node]
                orig_dp_child = dp[child]

                # Remove child's contribution from parent
                if dp[child] > 0:
                    dp[node] -= dp[child]

                # Add parent's contribution to child (if positive)
                if dp[node] > 0:
                    dp[child] += dp[node]

                # Recursively process child
                yield dfs2(child, node)

                # Restore original values
                dp[node] = orig_dp_node
                dp[child] = orig_dp_child

        # Record answer for current node
        ans[node] = dp[node]
        yield

    # Run the DP calculations
    dfs1(root, -1)
    dfs2(root, -1)

    return ans


def best_path_max_gasoline(adj, values):
    """
    Find the maximum amount of gasoline at the end of a path (Codeforces 1083A)

    Args:
        adj: Weighted adjacency list, each edge is a tuple (target_node, weight)
        values: List of values (gas) for each node

    Returns:
        Maximum amount of gasoline possible
    """
    n = len(values)
    best = [0] * n  # Best path ending at each node
    max_gasoline = 0

    def dfs(node, parent=-1):
        nonlocal max_gasoline

        # For each child, calculate best path ending at it
        candidates = []
        for child, weight in adj[node]:
            if child != parent:
                dfs(child, node)
                # Calculate potential contribution: best ending at child + value - cost
                contribution = best[child] + values[child] - weight
                if contribution > 0:
                    candidates.append(contribution)

        # Sort candidates in descending order (best first)
        candidates.sort(reverse=True)

        # Calculate total for current node
        current = values[node]
        # Add up to two best paths (if available and positive)
        for i in range(min(2, len(candidates))):
            if candidates[i] > 0:
                current += candidates[i]

        # Update global max
        max_gasoline = max(max_gasoline, current)

        # Update best ending at current node (use at most 1 child)
        best[node] = candidates[0] if candidates and candidates[0] > 0 else 0

    dfs(0)
    return max_gasoline


def max_kingdom_happiness(adj, n, k, root=1, one_indexed=True):
    """
    Calculate maximum happiness in the Linova's Kingdom problem (Codeforces 1336A)

    Args:
        adj: Adjacency list representation of the tree
        n: Number of nodes
        k: Number of industrial cities
        root: Root node (capital)
        one_indexed: Whether indices are 1-based (True) or 0-based (False)

    Returns:
        Maximum sum of happiness
    """
    offset = 1 if one_indexed else 0
    root_idx = root - offset  # Convert to 0-based internally

    # Arrays to store depth and subtree size
    depths = [0] * n
    subtree_sizes = [0] * n
    visited = [False] * n

    # DFS to calculate depths and subtree sizes
    def dfs(node, depth=0, parent=None):
        visited[node] = True
        depths[node] = depth
        subtree_size = 0

        for child in adj[node]:
            if not visited[child] and child != parent:
                subtree_size += dfs(child, depth + 1, node) + 1

        subtree_sizes[node] = subtree_size
        return subtree_size

    # Run DFS
    dfs(root_idx)

    # Calculate scores for each node: subtree_size - depth
    # This represents the benefit of making a city industrial
    scores = [subtree_sizes[i] - depths[i] for i in range(n)]

    # Sort scores in descending order
    scores.sort(reverse=True)

    # Choose n-k cities with highest scores to be tourism cities
    # The remaining k cities will be industrial
    return sum(scores[:n-k])


def min_max_soulmate_paths(adj, k):
    """
    Calculate min and max soulmate path sums (Codeforces 1281E)

    Args:
        adj: Weighted adjacency list representation of tree
             Each edge is (target_node, weight)
        k: Number of pairs of soulmates (total nodes = 2*k)

    Returns:
        Tuple (min_sum, max_sum) for minimum and maximum soulmate path sums
    """
    n = 2 * k

    # Compute parent array and BFS ordering using iterative DFS
    parent = [-1] * n
    bfs_order = []
    visited = [False] * n

    # Use node 0 as root
    queue = [0]
    visited[0] = True

    while queue:
        node = queue.pop()
        bfs_order.append(node)

        for neighbor, _ in adj[node]:
            if not visited[neighbor]:
                parent[neighbor] = node
                visited[neighbor] = True
                queue.append(neighbor)

    # Calculate subtree data
    subtree_odd = [False] * n  # Whether subtree has odd number of nodes
    subtree_size = [0] * n     # Size of subtree

    min_sum = 0  # Minimum path sum
    max_sum = 0  # Maximum path sum

    # Process nodes in reverse BFS order (bottom-up)
    for i in range(len(bfs_order) - 1, -1, -1):
        node = bfs_order[i]

        # Each node starts as its own subtree of size 1
        subtree_odd[node] = True
        subtree_size[node] = 1

        for neighbor, weight in adj[node]:
            if neighbor != parent[node]:
                # If subtree has odd parity, we can make a soulmate pair
                # This greedily pairs nodes within subtrees for min sum
                if subtree_odd[neighbor]:
                    min_sum += weight

                # Update subtree properties
                subtree_odd[node] = subtree_odd[node] ^ subtree_odd[neighbor]
                subtree_size[node] += subtree_size[neighbor]

                # For max sum, calculate weight * min(size, n-size)
                # This represents placing soulmates across the edge optimally
                max_sum += weight * min(subtree_size[neighbor], n - subtree_size[neighbor])

    return min_sum, max_sum


def game_on_tree_minimax(adj, root=1):
    """
    Calculate min and max leaves for a game on a tree (CF 538E)

    Args:
        adj: Adjacency list representation of the tree
        root: Root node (typically 1)

    Returns:
        Tuple (min_leaves, max_leaves) representing min/max leaves player can reach
    """
    # Compute depth and remove parent edges to get children only
    depth = bfs_with_depth(adj, root)

    # Identify leaf nodes
    leaves = []
    for i in range(1, len(adj)):
        if i != root and len(adj[i]) == 1:
            leaves.append(i)

    leaf_count = len(leaves)

    # Child-only adjacency list
    child_adj = [[] for _ in range(len(adj))]

    # Create child-only adjacency list
    for i in range(1, len(adj)):
        for j in adj[i]:
            if depth[j] > depth[i]:
                child_adj[i].append(j)

    # Initialize DP arrays for min and max
    min_dp = [0] * len(adj)
    max_dp = [0] * len(adj)

    # Process nodes in reverse BFS order (from leaves to root)
    for i in range(len(adj) - 1, 0, -1):
        if not child_adj[i]:  # Leaf node
            min_dp[i] = 1
            max_dp[i] = 1
        elif depth[i] % 2 == 0:  # Max player (even depth)
            # Max player wants to maximize
            total_min = 0
            min_of_max = float('inf')

            for child in child_adj[i]:
                total_min += min_dp[child]
                min_of_max = min(min_of_max, max_dp[child])

            min_dp[i] = total_min
            max_dp[i] = min_of_max if min_of_max < float('inf') else 0
        else:  # Min player (odd depth)
            # Min player wants to minimize
            min_of_min = float('inf')
            total_max = 0

            for child in child_adj[i]:
                min_of_min = min(min_of_min, min_dp[child])
                total_max += max_dp[child]

            min_dp[i] = min_of_min if min_of_min < float('inf') else 0
            max_dp[i] = total_max

    return max_dp[root], min_dp[root]


def zero_tree_operations(adj, values, root=1):
    """
    Calculate operations to make a tree have all zero values (Codeforces 275D)

    Args:
        adj: Adjacency list representation of the tree
        values: Array of node values
        root: Root node

    Returns:
        Minimum number of operations to make all values zero
    """
    n = len(adj)
    # Positive and negative operations that propagate up the tree
    plus = [0] * n
    minus = [0] * n

    # Calculate parent for each node using BFS
    parent = [-1] * n
    visited = [False] * n
    queue = deque([root])
    visited[root] = True

    while queue:
        node = queue.popleft()
        for child in adj[node]:
            if not visited[child]:
                parent[child] = node
                visited[child] = True
                queue.append(child)

    # Process nodes from leaves to root (postorder traversal)
    # Get postorder traversal
    postorder = []
    visited = [False] * n
    stack = [root]

    while stack:
        node = stack[-1]
        if not visited[node]:
            visited[node] = True
            for neighbor in adj[node]:
                if neighbor != parent[node] and not visited[neighbor]:
                    stack.append(neighbor)
        else:
            postorder.append(stack.pop())

    # Process nodes in postorder
    for node in postorder:
        # Balance needed at this node
        balance = minus[node] - plus[node]
        # Current value + balance should be 0
        target = values[node-1] + balance

        if node != root:
            p = parent[node]
            # Propagate operations up to parent
            minus[p] = max(minus[p], minus[node])
            plus[p] = max(plus[p], plus[node])

            if target > 0:
                plus[p] = max(plus[p], plus[node] + target)
            elif target < 0:
                minus[p] = max(minus[p], minus[node] - target)

    # Total operations needed
    return plus[root] + minus[root]