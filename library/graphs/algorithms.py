"""
Common graph algorithms.
"""

import heapq
from typing import List, Tuple

from library.graphs.graph import Graph


def prim_mst(g: Graph) -> List[Tuple[int, int, int]]:
    """Find minimum spanning tree using Prim's algorithm.

    Args:
        g: Graph object

    Returns:
        List of (u, v, w) tuples representing MST edges
    """
    if not g.weighted:
        raise ValueError("Prim's algorithm requires a weighted graph")

    if g.directed:
        raise ValueError("Prim's algorithm is for undirected graphs")

    n = g.n
    visited = [False] * n
    mst = []

    # Start from vertex 0
    pq = [(0, 0, -1)]  # (weight, vertex, parent)

    while pq and len(mst) < n - 1:
        weight, v, parent = heapq.heappop(pq)

        if visited[v]:
            continue

        visited[v] = True

        if parent != -1:
            mst.append((parent, v, weight))

        for neighbor, edge_weight in g.adj[v]:
            if not visited[neighbor]:
                heapq.heappush(pq, (edge_weight, neighbor, v))

    return mst


def floyd_warshall(g: Graph) -> List[List[float]]:
    """Find all-pairs shortest paths using Floyd-Warshall algorithm.

    Args:
        g: Graph object

    Returns:
        2D array where dist[i][j] is the shortest distance from i to j
    """
    n = g.n

    # Initialize distance matrix
    dist = [[float("inf")] * n for _ in range(n)]

    # Set diagonal to 0
    for i in range(n):
        dist[i][i] = 0

    # Set direct edge weights
    if g.weighted:
        for u in range(n):
            for v, w in g.adj[u]:
                dist[u][v] = min(dist[u][v], w)
    else:
        for u in range(n):
            for v in g.adj[u]:
                dist[u][v] = 1

    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float("inf") and dist[k][j] != float("inf"):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


def bellman_ford(g: Graph, start: int) -> Tuple[List[float], bool]:
    """Find single-source shortest paths using Bellman-Ford algorithm.

    This algorithm works with negative weights and can detect negative cycles.

    Args:
        g: Graph object
        start: Starting vertex

    Returns:
        Tuple (dist, has_negative_cycle) where:
        - dist is a list where dist[i] is the shortest distance from start to i
        - has_negative_cycle is True if there's a negative cycle reachable from start
    """
    if not g.weighted:
        raise ValueError("Bellman-Ford algorithm requires a weighted graph")

    n = g.n
    dist = [float("inf")] * n
    dist[start] = 0

    # Get all edges
    edges = []
    for u in range(n):
        for v, w in g.adj[u]:
            edges.append((u, v, w))

    # Relax edges n-1 times
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Check for negative cycles
    has_negative_cycle = False
    for u, v, w in edges:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            has_negative_cycle = True
            break

    return dist, has_negative_cycle


def bipartite_matching(g: Graph) -> List[Tuple[int, int]]:
    """Find maximum bipartite matching using Ford-Fulkerson algorithm.

    Args:
        g: Bipartite graph where edges go from left to right

    Returns:
        List of (left, right) matched pairs
    """
    n = g.n
    matches = [-1] * n  # matches[right] = left

    def dfs(left: int, visited: List[bool]) -> bool:
        for right in g.adj[left]:
            if visited[right]:
                continue

            visited[right] = True

            if matches[right] == -1 or dfs(matches[right], visited):
                matches[right] = left
                return True

        return False

    # Find augmenting paths
    match_count = 0
    for left in range(n):
        visited = [False] * n
        if dfs(left, visited):
            match_count += 1

    # Collect matched pairs
    result = []
    for right in range(n):
        if matches[right] != -1:
            result.append((matches[right], right))

    return result


def tarjan_scc(g: Graph) -> List[List[int]]:
    """Find strongly connected components using Tarjan's algorithm.

    Args:
        g: Graph object

    Returns:
        List of SCCs, where each SCC is a list of vertices
    """
    n = g.n
    disc = [-1] * n  # Discovery time
    low = [-1] * n  # Earliest visited vertex reachable
    on_stack = [False] * n
    stack = []

    time = [0]  # Use list to allow modification in recursive function
    sccs = []

    def dfs(u: int) -> None:
        disc[u] = low[u] = time[0]
        time[0] += 1
        stack.append(u)
        on_stack[u] = True

        for v in g.adj[u] if not g.weighted else [v for v, _ in g.adj[u]]:
            if disc[v] == -1:  # If v is not visited
                dfs(v)
                low[u] = min(low[u], low[v])
            elif on_stack[v]:  # Back edge to a vertex in current SCC
                low[u] = min(low[u], disc[v])

        # If u is the root of an SCC
        if low[u] == disc[u]:
            scc = []

            while True:
                v = stack.pop()
                on_stack[v] = False
                scc.append(v)

                if v == u:
                    break

            sccs.append(scc)

    # DFS for all unvisited vertices
    for u in range(n):
        if disc[u] == -1:
            dfs(u)

    return sccs


def is_eulerian(g: Graph) -> Tuple[bool, bool]:
    """Check if a graph has an Eulerian path or cycle.

    Args:
        g: Graph object

    Returns:
        Tuple (has_path, has_cycle) where:
        - has_path is True if the graph has an Eulerian path
        - has_cycle is True if the graph has an Eulerian cycle
    """
    if g.directed:
        # Check for directed graph
        in_degree = [0] * g.n
        out_degree = [0] * g.n

        for u in range(g.n):
            neighbors = g.adj[u] if not g.weighted else [v for v, _ in g.adj[u]]
            out_degree[u] = len(neighbors)

            for v in neighbors:
                in_degree[v] += 1

        # Check for Eulerian cycle
        has_cycle = all(in_degree[u] == out_degree[u] for u in range(g.n))

        # Check for Eulerian path
        diff_count = 0
        start_end = 0

        for u in range(g.n):
            diff = out_degree[u] - in_degree[u]

            if diff == 1:  # Potential start
                diff_count += 1
                start_end += 1
            elif diff == -1:  # Potential end
                diff_count += 1
                start_end -= 1
            elif diff != 0:
                return False, False

        has_path = diff_count == 0 or (diff_count == 2 and start_end == 0)

        return has_path, has_cycle
    else:
        # Check for undirected graph
        odd_degree_count = 0

        for u in range(g.n):
            neighbors = g.adj[u] if not g.weighted else [v for v, _ in g.adj[u]]
            if len(neighbors) % 2 == 1:
                odd_degree_count += 1

        has_cycle = odd_degree_count == 0
        has_path = odd_degree_count == 0 or odd_degree_count == 2

        return has_path, has_cycle


def bridge_finding(g: Graph) -> List[Tuple[int, int]]:
    """Find all bridges in an undirected graph.

    A bridge is an edge whose removal increases the number of connected components.

    Args:
        g: Graph object (undirected)

    Returns:
        List of (u, v) tuples representing bridge edges
    """
    if g.directed:
        raise ValueError("Bridge finding is for undirected graphs")

    n = g.n
    disc = [-1] * n  # Discovery time
    low = [-1] * n  # Earliest visited vertex reachable
    parent = [-1] * n  # Parent in DFS tree

    time = [0]  # Use list to allow modification in recursive function
    bridges = []

    def dfs(u: int) -> None:
        disc[u] = low[u] = time[0]
        time[0] += 1

        neighbors = g.adj[u] if not g.weighted else [v for v, _ in g.adj[u]]
        for v in neighbors:
            if disc[v] == -1:  # If v is not visited
                parent[v] = u
                dfs(v)
                low[u] = min(low[u], low[v])

                # If v cannot reach u or ancestors of u, (u,v) is a bridge
                if low[v] > disc[u]:
                    bridges.append((u, v))
            elif v != parent[u]:  # Back edge, but not to parent
                low[u] = min(low[u], disc[v])

    # DFS for all unvisited vertices
    for u in range(n):
        if disc[u] == -1:
            dfs(u)

    return bridges


def articulation_points(g: Graph) -> List[int]:
    """Find all articulation points in an undirected graph.

    An articulation point (or cut vertex) is a vertex whose removal increases
    the number of connected components.

    Args:
        g: Graph object (undirected)

    Returns:
        List of vertices that are articulation points
    """
    if g.directed:
        raise ValueError("Articulation point finding is for undirected graphs")

    n = g.n
    disc = [-1] * n  # Discovery time
    low = [-1] * n  # Earliest visited vertex reachable
    parent = [-1] * n  # Parent in DFS tree
    ap = [False] * n  # Is vertex an articulation point?

    time = [0]  # Use list to allow modification in recursive function

    def dfs(u: int) -> None:
        children = 0
        disc[u] = low[u] = time[0]
        time[0] += 1

        neighbors = g.adj[u] if not g.weighted else [v for v, _ in g.adj[u]]
        for v in neighbors:
            if disc[v] == -1:  # If v is not visited
                parent[v] = u
                children += 1
                dfs(v)
                low[u] = min(low[u], low[v])

                # Check if u is an articulation point
                if parent[u] == -1 and children > 1:
                    ap[u] = True
                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True
            elif v != parent[u]:  # Back edge, but not to parent
                low[u] = min(low[u], disc[v])

    # DFS for all unvisited vertices
    for u in range(n):
        if disc[u] == -1:
            dfs(u)

    return [u for u in range(n) if ap[u]]
