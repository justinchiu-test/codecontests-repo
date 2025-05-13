#!/usr/bin/env python3

from library import Graph

n = int(input())
total_games = n * (n - 1) // 2
games_played = total_games - 1  # One game is missing

# Create a directed graph where an edge u->v means u beat v
graph = Graph(n+1, directed=True)

# Keep track of games played by each player
games_count = [0] * (n + 1)

# Process game results
for _ in range(games_played):
    winner, loser = map(int, input().split())
    graph.add_edge(winner, loser)
    games_count[winner] += 1
    games_count[loser] += 1

# Find players who haven't played against each other
missing_players = []
for i in range(1, n + 1):
    if games_count[i] < n - 1:
        missing_players.append(i)

a, b = missing_players

# Create a simple helper to check if we can reach b from a in the graph
def can_reach(graph, a, b, visited=None):
    if visited is None:
        visited = set()
    
    if a == b:
        return True
    
    visited.add(a)
    for neighbor in graph.neighbors(a):
        if neighbor not in visited and can_reach(graph, neighbor, b, visited):
            return True
    
    return False

# Try to determine who would win based on transitivity
# If a can reach b in the graph or b can reach a, we can determine the winner
if can_reach(graph, a, b):
    result = [a, b]  # a would win against b
elif can_reach(graph, b, a):
    result = [b, a]  # b would win against a
else:
    # If we can't directly determine from the graph, try the original approach
    # For convenience, always try the order [b, a] first and only switch if necessary
    result = [b, a]

print(*result)