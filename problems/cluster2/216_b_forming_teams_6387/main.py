#!/usr/bin/env python3

from library import Graph

# Read input
n, m = map(int, input().split())
graph = Graph(n+1)  # 1-indexed students

# Read edges
for _ in range(m):
    a, b = map(int, input().split())
    graph.add_edge(a, b)

# Count students to exclude due to odd cycles
students_to_exclude = graph.count_odd_length_cycles()

# If remaining students are odd, exclude one more student
if (n - students_to_exclude) % 2 == 1:
    students_to_exclude += 1

print(students_to_exclude)