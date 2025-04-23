#!/usr/bin/env python3

from random import choice as _choice
import sys as _sys


def main():
    t = int(input())
    for i in range(t):
        n, = _read_ints()
        graph = [set() for v in range(n)]
        for i_edge in range(n-1):
            v1, v2 = _read_ints()
            v1 -= 1
            v2 -= 1
            graph[v1].add(v2)
            graph[v2].add(v1)
        operations = find_operations_necessary_to_remain_one_centroid(graph)
        for v1, v2 in operations:
            print(v1+1, v2+1)


def _read_line():
    result = _sys.stdin.readline()
    assert result[-1] == "\n"
    return result[:-1]


def _read_ints():
    return map(int, _read_line().split(" "))


def find_operations_necessary_to_remain_one_centroid(graph):
    assert len(graph) > 2
    graph = [set(neighbors) for neighbors in graph]

    centroids = find_centroids(graph)
    assert 0 < len(centroids) <= 2

    if len(centroids) == 1:
        operation_remove = (0, tuple(graph[0])[0])
        operation_add = operation_remove

    else:
        assert len(centroids) == 2
        centroid_1, centroid_2 = centroids

        vertex_to_move = centroid_1
        forbidden_vertex = centroid_2
        while len(graph[vertex_to_move]) != 1:
            neighbors = tuple(graph[vertex_to_move])
            new_vertex_to_move = neighbors[0]
            if new_vertex_to_move == forbidden_vertex:
                new_vertex_to_move = neighbors[1]
            forbidden_vertex = vertex_to_move
            vertex_to_move = new_vertex_to_move

        vertex_to_move_parent = tuple(graph[vertex_to_move])[0]
        operation_remove = (vertex_to_move, vertex_to_move_parent)
        graph[vertex_to_move].remove(vertex_to_move_parent)
        graph[vertex_to_move_parent].remove(vertex_to_move)
        assert len(graph[vertex_to_move]) == 0

        new_parent = centroid_2
        graph[vertex_to_move].add(new_parent)
        graph[new_parent].add(vertex_to_move)

        operation_add = (vertex_to_move, new_parent)

    return operation_remove, operation_add


def find_centroids(graph):
    vertices_n = len(graph)
    vertices_values = [None] * len(graph)

    leaves = [vertex for vertex in range(len(graph)) if len(graph[vertex]) == 1]
    vertices_accumulated = [None] * len(graph)
    for leave in leaves:
        vertices_accumulated[leave] = 1
        vertices_values[leave] = vertices_n - 1

    active = set().union(*(graph[leave] for leave in leaves))
    passed = set(leaves)
    active -= passed
    while len(passed) < len(graph):
        old_active = active
        active = set()
        for vertex in old_active:
            neighbors = graph[vertex]
            neighbors_not_passed = neighbors - passed
            if len(neighbors_not_passed) > 1:
                active.add(vertex)
                continue
            vertices_accumulated[vertex] = sum(
                vertices_accumulated[neighbor] for neighbor in neighbors if neighbor in passed
            ) + 1
            components_remain_sizes = []
            for neighbor in neighbors - neighbors_not_passed:
                components_remain_sizes.append(vertices_accumulated[neighbor])
            assert len(neighbors_not_passed) <= 1
            for neighbor in neighbors_not_passed:
                components_remain_sizes.append(vertices_n - vertices_accumulated[vertex])
            vertex_value = max(components_remain_sizes)
            vertices_values[vertex] = vertex_value
            passed.add(vertex)
            active.update(neighbors_not_passed)
        active = active - passed

    centroid_value = min(vertices_values)
    centroids = [vertex for vertex, value in enumerate(vertices_values) if value == centroid_value]
    return centroids


if __name__ == '__main__':
    main()
