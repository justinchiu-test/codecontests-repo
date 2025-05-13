#!/usr/bin/env python3

from library import Graph

# Tournament problem: need to find the missing game between players
n = int(input())

# Create two directed graphs to track who beat whom and who played against whom
graph = Graph(n + 1, directed=True)
played_against = [set() for _ in range(n + 1)]

# Read the matches that have been played
for _ in range(n * (n - 1) // 2 - 1):  # One match is missing
    winner, loser = map(int, input().split())
    graph.add_edge(winner, loser)
    played_against[winner].add(loser)
    played_against[loser].add(winner)

# Find the two players who didn't play against each other
missing_match = []
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if j not in played_against[i]:
            missing_match = [i, j]
            break

# Now we need to determine who would win in the missing match
# We'll use a tournament ranking
scores = [0] * (n + 1)
for i in range(1, n + 1):
    scores[i] = len(graph.adj[i])

# Player with more wins should be ranked higher
# If scores[missing_match[0]] > scores[missing_match[1]], then missing_match[0] should win
# Otherwise, missing_match[1] should win
if scores[missing_match[0]] > scores[missing_match[1]]:
    print(missing_match[0], missing_match[1])
else:
    print(missing_match[1], missing_match[0])