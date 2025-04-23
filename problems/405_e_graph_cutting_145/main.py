#!/usr/bin/env python3

import sys

input = sys.stdin.readline
print = sys.stdout.write


def get_input():
    n, m = [int(x) for x in input().split(' ')]

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        c1, c2 = [int(x) for x in input().split(' ')]
        graph[c1].append(c2)
        graph[c2].append(c1)

    if m % 2 != 0:
        print("No solution")
        exit(0)

    return graph


def partitions_bottom_up(graph):
    n = len(graph)
    w = [0] * n
    pi = [None] * n
    visited = [False] * n
    finished = [False] * n
    adjacency = [[] for _ in range(n)]

    stack = [1]
    while stack:
        current_node = stack[-1]

        if visited[current_node]:
            stack.pop()
            if finished[current_node]:
                w[current_node] = 0
                continue

            finished[current_node] = True
            unpair = []
            for adj in adjacency[current_node]:
                if w[adj] == 0:
                    unpair.append(adj)
                else:
                    print(' '.join([str(current_node), str(adj), str(w[adj]), '\n']))

            while len(unpair) > 1:
                print(' '.join([str(unpair.pop()), str(current_node), str(unpair.pop()), '\n']))
            w[current_node] = unpair.pop() if unpair else 0
            continue

        visited[current_node] = True
        not_blocked_neighbors = [x for x in graph[current_node] if not visited[x]]
        stack += not_blocked_neighbors
        adjacency[current_node] = not_blocked_neighbors


def partitions_top_down(graph):
    n = len(graph)
    visited = [False] * n

    for node in range(1, n):
        if not visited[node]:
            prev_node = None
            current_node = node
            while current_node is not None:
                visited[current_node] = True

                leafs = [prev_node] if prev_node is not None else []
                adjacency = []
                for adj in graph[current_node]:
                    if not visited[adj]:
                        if len(graph[adj]) == 1:
                            leafs.append(adj)
                        else:
                            adjacency.append(adj)

                while len(leafs) > 1:
                    print(' '.join([str(leafs.pop()), str(current_node), str(leafs.pop()), '\n']))

                if leafs:
                    adjacency.append(leafs.pop())

                while len(adjacency) > 1:
                    print(' '.join([str(adjacency.pop()), str(current_node), str(adjacency.pop()), '\n']))

                if adjacency:
                    current_node, prev_node = adjacency.pop(), current_node
                else:
                    current_node = None


if __name__ == "__main__":
    graph = get_input()
    partitions_bottom_up(graph)
