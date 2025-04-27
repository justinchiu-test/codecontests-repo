"""
Graph search algorithms and utilities.
"""

import heapq
from collections import deque
from typing import Callable, Dict, List, Optional, Tuple, TypeVar

T = TypeVar("T")


def bfs_grid(
    grid: List[str],
    start: Tuple[int, int],
    is_valid: Callable[[int, int], bool] = None,
    directions: List[Tuple[int, int]] = None,
) -> Dict[Tuple[int, int], int]:
    """Breadth-first search on a 2D grid.

    Args:
        grid: The 2D grid (list of strings)
        start: Starting position (row, col)
        is_valid: Function that takes (row, col) and returns whether the position is valid.
                 If None, all non-wall cells in the grid are valid.
        directions: List of (dr, dc) tuples for allowed directions.
                   If None, default to 4 directions (up, down, left, right).

    Returns:
        Dictionary mapping (row, col) positions to distances from start
    """
    if not grid:
        return {}

    n, m = len(grid), len(grid[0])

    if directions is None:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    if is_valid is None:

        def is_valid(r: int, c: int) -> bool:
            return 0 <= r < n and 0 <= c < m and grid[r][c] != "#"

    queue = deque([start])
    distances = {start: 0}

    while queue:
        r, c = queue.popleft()
        dist = distances[(r, c)]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if is_valid(nr, nc) and (nr, nc) not in distances:
                distances[(nr, nc)] = dist + 1
                queue.append((nr, nc))

    return distances


def dijkstra_grid(
    grid: List[str],
    start: Tuple[int, int],
    is_valid: Callable[[int, int], bool] = None,
    cost_fn: Callable[[int, int, int, int], int] = None,
    directions: List[Tuple[int, int]] = None,
) -> Dict[Tuple[int, int], int]:
    """Dijkstra's algorithm on a 2D grid with custom edge costs.

    Args:
        grid: The 2D grid (list of strings)
        start: Starting position (row, col)
        is_valid: Function that takes (row, col) and returns whether the position is valid.
                 If None, all non-wall cells in the grid are valid.
        cost_fn: Function that takes (r1, c1, r2, c2) and returns the cost of moving
                from (r1, c1) to (r2, c2). If None, all costs are 1.
        directions: List of (dr, dc) tuples for allowed directions.
                   If None, default to 4 directions (up, down, left, right).

    Returns:
        Dictionary mapping (row, col) positions to shortest distances from start
    """
    if not grid:
        return {}

    n, m = len(grid), len(grid[0])

    if directions is None:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    if is_valid is None:

        def is_valid(r: int, c: int) -> bool:
            return 0 <= r < n and 0 <= c < m and grid[r][c] != "#"

    if cost_fn is None:

        def cost_fn(r1: int, c1: int, r2: int, c2: int) -> int:
            return 1

    pq = [(0, start)]  # (distance, position)
    distances = {start: 0}

    while pq:
        dist, (r, c) = heapq.heappop(pq)

        if dist > distances.get((r, c), float("inf")):
            continue

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if is_valid(nr, nc):
                new_dist = dist + cost_fn(r, c, nr, nc)

                if new_dist < distances.get((nr, nc), float("inf")):
                    distances[(nr, nc)] = new_dist
                    heapq.heappush(pq, (new_dist, (nr, nc)))

    return distances


def multi_source_bfs(
    n: int, edges: List[Tuple[int, int]], sources: List[int]
) -> List[int]:
    """BFS from multiple source vertices.

    Args:
        n: Number of vertices (0 to n-1)
        edges: List of (u, v) edges
        sources: List of source vertices

    Returns:
        List of distances from the closest source to each vertex
        (float('inf') if unreachable)
    """
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Initialize distances
    dist = [float("inf")] * n
    queue = deque()

    # Add all sources to the queue
    for s in sources:
        dist[s] = 0
        queue.append(s)

    # BFS
    while queue:
        u = queue.popleft()

        for v in adj[u]:
            if dist[v] == float("inf"):
                dist[v] = dist[u] + 1
                queue.append(v)

    return dist


def a_star(
    start: T,
    goal_fn: Callable[[T], bool],
    neighbors_fn: Callable[[T], List[Tuple[T, int]]],
    heuristic_fn: Callable[[T], int],
) -> Tuple[Optional[List[T]], int]:
    """A* search algorithm for finding shortest path.

    Args:
        start: Starting state
        goal_fn: Function that takes a state and returns True if it's a goal state
        neighbors_fn: Function that takes a state and returns list of (neighbor, cost) tuples
        heuristic_fn: Function that takes a state and returns an estimate of the cost to goal

    Returns:
        Tuple (path, cost) where path is the shortest path from start to goal
        (None if no path exists) and cost is the total cost of the path
    """
    open_set = []
    closed_set = set()

    # g_score[state] is the cost from start to state
    g_score = {start: 0}

    # f_score[state] = g_score[state] + heuristic(state)
    f_score = {start: heuristic_fn(start)}

    # For reconstructing the path
    came_from = {}

    # Add start to open set
    heapq.heappush(open_set, (f_score[start], id(start), start))

    while open_set:
        _, _, current = heapq.heappop(open_set)

        if goal_fn(current):
            # Reconstruct path
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path, g_score[path[-1]]

        closed_set.add(current)

        for neighbor, cost in neighbors_fn(current):
            if neighbor in closed_set:
                continue

            tentative_g_score = g_score[current] + cost

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                # This path to neighbor is better than any previous one
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic_fn(neighbor)

                if neighbor not in [item[2] for item in open_set]:
                    heapq.heappush(
                        open_set, (f_score[neighbor], id(neighbor), neighbor)
                    )

    # No path found
    return None, float("inf")
