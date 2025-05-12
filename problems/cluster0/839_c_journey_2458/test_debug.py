#!/usr/bin/env python3

# Simple debug script for test case 6
n = 10
edges = [(8, 6), (9, 10), (8, 7), (1, 4), (1, 8), (9, 5), (9, 8), (2, 9), (3, 1)]

print(f"n = {n}, edges length = {len(edges)}")
print(f"First edge = {edges[0]}")
print(f"Second edge = {edges[1]}")
print(f"Last edge = {edges[-1]}")
print(f"n - 1 = {n - 1}")

# For test case 4
edges2 = [(8, 6), (9, 10), (8, 7), (1, 4), (1, 8), (9, 5), (9, 8), (2, 5), (3, 1)]
print("\nTest case 4:")
print(f"edges2[8] = {edges2[8]}")

# For test case 6
print("\nTest case 6:")
print(f"edges[8] = {edges[8]}")