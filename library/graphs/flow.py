"""
Network flow algorithms.
"""

from collections import deque
from typing import List, Optional, Tuple


class FlowGraph:
    """Graph representation for flow algorithms."""

    def __init__(self, n: int):
        """Initialize a flow graph with n vertices.

        Args:
            n: Number of vertices (0 to n-1)
        """
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.flow = {}  # Maps (u, v) to flow
        self.capacity = {}  # Maps (u, v) to capacity

    def add_edge(self, u: int, v: int, cap: int) -> None:
        """Add a directed edge from u to v with capacity cap.

        Args:
            u: Source vertex
            v: Target vertex
            cap: Edge capacity
        """
        self.graph[u].append(v)
        self.graph[v].append(u)  # Add reverse edge for residual graph
        self.capacity[(u, v)] = cap
        self.capacity[(v, u)] = 0  # Reverse edge has 0 capacity initially
        self.flow[(u, v)] = 0
        self.flow[(v, u)] = 0

    def ford_fulkerson_dfs(self, source: int, sink: int) -> int:
        """Compute maximum flow using Ford-Fulkerson method with DFS.

        Args:
            source: Source vertex
            sink: Sink vertex

        Returns:
            Maximum flow from source to sink
        """

        def dfs(u: int, flow: int) -> int:
            if u == sink:
                return flow

            for v in self.graph[u]:
                residual = self.capacity[(u, v)] - self.flow[(u, v)]

                if residual > 0 and v not in visited:
                    visited.add(v)
                    curr_flow = dfs(v, min(flow, residual))

                    if curr_flow > 0:
                        self.flow[(u, v)] += curr_flow
                        self.flow[(v, u)] -= curr_flow
                        return curr_flow

            return 0

        max_flow = 0
        while True:
            visited = {source}
            path_flow = dfs(source, float("inf"))

            if path_flow == 0:
                break

            max_flow += path_flow

        return max_flow

    def edmonds_karp(self, source: int, sink: int) -> int:
        """Compute maximum flow using Edmonds-Karp algorithm (BFS).

        Args:
            source: Source vertex
            sink: Sink vertex

        Returns:
            Maximum flow from source to sink
        """

        def bfs() -> Optional[List[Tuple[int, int, int]]]:
            """Find an augmenting path using BFS.

            Returns:
                List of (u, v, flow) triples or None if no path found
            """
            queue = deque([source])
            parent = {source: -1}

            while queue and sink not in parent:
                u = queue.popleft()

                for v in self.graph[u]:
                    residual = self.capacity[(u, v)] - self.flow[(u, v)]

                    if residual > 0 and v not in parent:
                        parent[v] = u
                        queue.append(v)

            if sink not in parent:
                return None

            # Reconstruct path
            path = []
            curr = sink
            flow = float("inf")

            while curr != source:
                prev = parent[curr]
                residual = self.capacity[(prev, curr)] - self.flow[(prev, curr)]
                flow = min(flow, residual)
                path.append((prev, curr, flow))
                curr = prev

            path.reverse()
            return path

        max_flow = 0

        while True:
            path = bfs()

            if path is None:
                break

            for u, v, flow in path:
                self.flow[(u, v)] += flow
                self.flow[(v, u)] -= flow

            max_flow += path[-1][2]

        return max_flow

    def dinic(self, source: int, sink: int) -> int:
        """Compute maximum flow using Dinic's algorithm.

        Args:
            source: Source vertex
            sink: Sink vertex

        Returns:
            Maximum flow from source to sink
        """

        def bfs() -> bool:
            """Build level graph and check if more flow is possible.

            Returns:
                True if more flow is possible, False otherwise
            """
            self.level = [-1] * self.n
            self.level[source] = 0

            queue = deque([source])

            while queue:
                u = queue.popleft()

                for v in self.graph[u]:
                    residual = self.capacity[(u, v)] - self.flow[(u, v)]

                    if residual > 0 and self.level[v] == -1:
                        self.level[v] = self.level[u] + 1
                        queue.append(v)

            return self.level[sink] != -1

        def dfs(u: int, flow: int) -> int:
            """Find augmenting paths in the level graph.

            Args:
                u: Current vertex
                flow: Current flow

            Returns:
                Flow sent through the path
            """
            if u == sink:
                return flow

            while self.next[u] < len(self.graph[u]):
                v = self.graph[u][self.next[u]]
                residual = self.capacity[(u, v)] - self.flow[(u, v)]

                if residual > 0 and self.level[v] == self.level[u] + 1:
                    curr_flow = dfs(v, min(flow, residual))

                    if curr_flow > 0:
                        self.flow[(u, v)] += curr_flow
                        self.flow[(v, u)] -= curr_flow
                        return curr_flow

                self.next[u] += 1

            return 0

        max_flow = 0

        while bfs():
            self.next = [0] * self.n

            while True:
                flow = dfs(source, float("inf"))

                if flow == 0:
                    break

                max_flow += flow

        return max_flow

    def min_cut(
        self, source: int, sink: int
    ) -> Tuple[List[int], List[Tuple[int, int]]]:
        """Find the minimum cut after computing the maximum flow.

        Args:
            source: Source vertex
            sink: Sink vertex

        Returns:
            Tuple (vertices, edges) where:
            - vertices is the list of vertices in the source side of the cut
            - edges is the list of edges crossing the cut
        """
        # Compute max flow if not already done
        if all(f == 0 for f in self.flow.values()):
            self.dinic(source, sink)

        # Find vertices reachable from source in the residual graph
        reachable = set()
        queue = deque([source])
        reachable.add(source)

        while queue:
            u = queue.popleft()

            for v in self.graph[u]:
                residual = self.capacity[(u, v)] - self.flow[(u, v)]

                if residual > 0 and v not in reachable:
                    reachable.add(v)
                    queue.append(v)

        # Find edges crossing the cut
        cut_edges = []

        for u in reachable:
            for v in self.graph[u]:
                if v not in reachable and self.capacity[(u, v)] > 0:
                    cut_edges.append((u, v))

        return list(reachable), cut_edges


def min_cost_max_flow(
    n: int, edges: List[Tuple[int, int, int, int]], source: int, sink: int
) -> Tuple[int, int]:
    """Compute minimum cost maximum flow using successive shortest paths.

    Args:
        n: Number of vertices (0 to n-1)
        edges: List of (u, v, cap, cost) tuples
        source: Source vertex
        sink: Sink vertex

    Returns:
        Tuple (max_flow, min_cost) where:
        - max_flow is the maximum flow from source to sink
        - min_cost is the minimum cost of the maximum flow
    """
    # Build graph
    graph = [[] for _ in range(n)]
    capacity = {}
    cost = {}
    flow = {}

    for u, v, cap, c in edges:
        graph[u].append(v)
        graph[v].append(u)  # Add reverse edge for residual graph
        capacity[(u, v)] = cap
        capacity[(v, u)] = 0
        cost[(u, v)] = c
        cost[(v, u)] = -c  # Reverse edge has negative cost
        flow[(u, v)] = 0
        flow[(v, u)] = 0

    # Bellman-Ford to find shortest paths
    def find_path() -> Optional[Tuple[List[int], int]]:
        """Find shortest path from source to sink in the residual graph.

        Returns:
            Tuple (path, flow) or None if no path exists
        """
        dist = [float("inf")] * n
        dist[source] = 0
        parent = [-1] * n
        flow_on_edge = [0] * n

        # Bellman-Ford
        for _ in range(n - 1):
            for u in range(n):
                for v in graph[u]:
                    residual = capacity[(u, v)] - flow[(u, v)]

                    if residual > 0 and dist[u] + cost[(u, v)] < dist[v]:
                        dist[v] = dist[u] + cost[(u, v)]
                        parent[v] = u
                        flow_on_edge[v] = min(
                            flow_on_edge[u] if u != source else float("inf"), residual
                        )

        if dist[sink] == float("inf"):
            return None

        # Reconstruct path
        path = []
        curr = sink

        while curr != source:
            path.append(curr)
            curr = parent[curr]

        path.append(source)
        path.reverse()

        return path, flow_on_edge[sink]

    max_flow = 0
    min_cost = 0

    while True:
        result = find_path()

        if result is None:
            break

        path, path_flow = result
        max_flow += path_flow

        # Update flow and cost
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            flow[(u, v)] += path_flow
            flow[(v, u)] -= path_flow
            min_cost += path_flow * cost[(u, v)]

    return max_flow, min_cost
