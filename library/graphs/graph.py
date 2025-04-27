"""
Graph data structures and algorithms.
"""

import heapq
from collections import deque
from typing import List, Optional, Tuple


class Graph:
    """Graph representation with adjacency list."""

    def __init__(self, n: int, directed: bool = False, weighted: bool = False):
        """Initialize a graph with n vertices.

        Args:
            n: Number of vertices (0 to n-1)
            directed: Whether the graph is directed
            weighted: Whether the graph has weights
        """
        self.n = n
        self.directed = directed
        self.weighted = weighted

        if weighted:
            self.adj = [[] for _ in range(n)]  # (neighbor, weight)
        else:
            self.adj = [[] for _ in range(n)]  # neighbor

    def add_edge(self, u: int, v: int, w: int = 1) -> None:
        """Add an edge from u to v.

        Args:
            u: Source vertex
            v: Target vertex
            w: Edge weight (default: 1)
        """
        if self.weighted:
            self.adj[u].append((v, w))
            if not self.directed:
                self.adj[v].append((u, w))
        else:
            self.adj[u].append(v)
            if not self.directed:
                self.adj[v].append(u)

    def get_edges(self) -> List[Tuple[int, int, int]]:
        """Get all edges in the graph.

        Returns:
            List of (u, v, w) tuples representing edges
        """
        edges = []
        for u in range(self.n):
            if self.weighted:
                for v, w in self.adj[u]:
                    if self.directed or u < v:  # Avoid duplicates in undirected graphs
                        edges.append((u, v, w))
            else:
                for v in self.adj[u]:
                    if self.directed or u < v:  # Avoid duplicates in undirected graphs
                        edges.append((u, v, 1))
        return edges

    def bfs(self, start: int) -> List[int]:
        """Perform BFS from a starting vertex.

        Args:
            start: Starting vertex

        Returns:
            List of distances from start to each vertex (-1 if unreachable)
        """
        queue = deque([start])
        dist = [-1] * self.n
        dist[start] = 0

        while queue:
            u = queue.popleft()
            if self.weighted:
                neighbors = [v for v, _ in self.adj[u]]
            else:
                neighbors = self.adj[u]

            for v in neighbors:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    queue.append(v)

        return dist

    def dfs(self, start: int) -> List[bool]:
        """Perform DFS from a starting vertex.

        Args:
            start: Starting vertex

        Returns:
            List indicating whether each vertex is reachable from start
        """
        visited = [False] * self.n

        def _dfs(u: int) -> None:
            visited[u] = True
            if self.weighted:
                neighbors = [v for v, _ in self.adj[u]]
            else:
                neighbors = self.adj[u]

            for v in neighbors:
                if not visited[v]:
                    _dfs(v)

        _dfs(start)
        return visited

    def dijkstra(self, start: int) -> List[int]:
        """Perform Dijkstra's algorithm from a starting vertex.

        Args:
            start: Starting vertex

        Returns:
            List of shortest distances from start to each vertex (float('inf') if unreachable)
        """
        if not self.weighted:
            raise ValueError("Dijkstra requires a weighted graph")

        dist = [float("inf")] * self.n
        dist[start] = 0
        pq = [(0, start)]  # (distance, vertex)

        while pq:
            d, u = heapq.heappop(pq)

            if d > dist[u]:
                continue

            for v, w in self.adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))

        return dist

    def topo_sort(self) -> Optional[List[int]]:
        """Perform topological sort.

        Returns:
            List of vertices in topological order, or None if there's a cycle
        """
        if not self.directed:
            raise ValueError("Topological sort requires a directed graph")

        in_degree = [0] * self.n

        if self.weighted:
            for u in range(self.n):
                for v, _ in self.adj[u]:
                    in_degree[v] += 1
        else:
            for u in range(self.n):
                for v in self.adj[u]:
                    in_degree[v] += 1

        queue = deque([u for u in range(self.n) if in_degree[u] == 0])
        result = []

        while queue:
            u = queue.popleft()
            result.append(u)

            if self.weighted:
                for v, _ in self.adj[u]:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        queue.append(v)
            else:
                for v in self.adj[u]:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        queue.append(v)

        return result if len(result) == self.n else None

    def kruskal(self) -> List[Tuple[int, int, int]]:
        """Find minimum spanning tree using Kruskal's algorithm.

        Returns:
            List of (u, v, w) tuples representing MST edges
        """
        if self.directed:
            raise ValueError("Kruskal's algorithm is for undirected graphs")

        from library.graphs.dsu import DSU

        edges = self.get_edges()
        edges.sort(key=lambda e: e[2])  # Sort by weight

        dsu = DSU(self.n)
        mst = []

        for u, v, w in edges:
            if not dsu.connected(u, v):
                dsu.union(u, v)
                mst.append((u, v, w))

        return mst

    def find_cycle(self) -> Optional[List[int]]:
        """Find a cycle in the graph, if one exists.

        Returns:
            List of vertices forming a cycle, or None if no cycle exists
        """
        visited = [0] * self.n  # 0: unvisited, 1: in stack, 2: visited
        parent = [-1] * self.n
        cycle = []

        def dfs(u: int) -> bool:
            visited[u] = 1

            if self.weighted:
                neighbors = [v for v, _ in self.adj[u]]
            else:
                neighbors = self.adj[u]

            for v in neighbors:
                if visited[v] == 0:
                    parent[v] = u
                    if dfs(v):
                        return True
                elif visited[v] == 1:  # Found a cycle
                    # Reconstruct the cycle
                    cycle.append(v)
                    curr = u
                    while curr != v:
                        cycle.append(curr)
                        curr = parent[curr]
                    cycle.reverse()
                    return True

            visited[u] = 2
            return False

        for i in range(self.n):
            if visited[i] == 0:
                if dfs(i):
                    return cycle

        return None

    def bipartite_check(self) -> Tuple[bool, Optional[List[int]]]:
        """Check if the graph is bipartite.

        Returns:
            Tuple (is_bipartite, coloring) where coloring is a list of colors (0/1)
            or None if not bipartite
        """
        color = [-1] * self.n  # -1: uncolored, 0/1: colors

        for start in range(self.n):
            if color[start] != -1:
                continue

            color[start] = 0
            queue = deque([start])

            while queue:
                u = queue.popleft()

                if self.weighted:
                    neighbors = [v for v, _ in self.adj[u]]
                else:
                    neighbors = self.adj[u]

                for v in neighbors:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return False, None

        return True, color

    def components(self) -> List[List[int]]:
        """Find connected components of the graph.

        Returns:
            List of components, where each component is a list of vertices
        """
        visited = [False] * self.n
        components_list = []

        for i in range(self.n):
            if not visited[i]:
                component = []
                self._dfs_component(i, visited, component)
                components_list.append(component)

        return components_list

    def _dfs_component(self, u: int, visited: List[bool], component: List[int]) -> None:
        """Helper function for finding connected components."""
        visited[u] = True
        component.append(u)

        if self.weighted:
            neighbors = [v for v, _ in self.adj[u]]
        else:
            neighbors = self.adj[u]

        for v in neighbors:
            if not visited[v]:
                self._dfs_component(v, visited, component)

    def count_components(self) -> int:
        """Count the number of connected components.

        Returns:
            Number of connected components
        """
        return len(self.components())


def build_graph_from_edges(
    edges: List[Tuple[int, int, Optional[int]]],
    n: Optional[int] = None,
    directed: bool = False,
    weighted: bool = False,
    zero_indexed: bool = True,
) -> Graph:
    """Build a graph from a list of edges.

    Args:
        edges: List of (u, v, w) tuples (w can be None for unweighted graphs)
        n: Number of vertices (deduced from edges if None)
        directed: Whether the graph is directed
        weighted: Whether the graph has weights
        zero_indexed: Whether vertices are 0-indexed

    Returns:
        Graph object
    """
    if n is None:
        vertices = set()
        for edge in edges:
            vertices.add(edge[0])
            vertices.add(edge[1])
        n = max(vertices) + 1

    g = Graph(n, directed, weighted)

    for edge in edges:
        u, v = edge[0], edge[1]
        if not zero_indexed:
            u -= 1
            v -= 1

        w = edge[2] if len(edge) > 2 and edge[2] is not None else 1
        g.add_edge(u, v, w)

    return g
