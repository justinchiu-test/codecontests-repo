#!/usr/bin/env python3

from library import read_int, read_int_tuple

# Read input
n = read_int()
G = [[] for _ in range(n)]

for _ in range(n-1):
    a, b = read_int_tuple()
    G[a-1].append(b-1)
    G[b-1].append(a-1)

# First DFS to calculate subtree sizes F
F = [0] * n
stk = [0]
visited = [0] * n

while stk:
    x = stk[-1]
    if not visited[x]:
        visited[x] = 1
        for y in G[x]:
            if not visited[y]:
                stk.append(y)
    else:
        x = stk.pop()
        F[x] = 1  # Count current node
        for y in G[x]:                
            if visited[y] and stk.count(y) == 0:  # y is a child if it's visited but not in stack
                F[x] += F[y]  # Add child's subtree size

# Second DFS to calculate DP (sum of subtree sizes)
DP = [0] * n
stk = [0]
visited = [0] * n

while stk:
    x = stk[-1]
    if not visited[x]:
        visited[x] = 1
        for y in G[x]:
            if not visited[y]:
                stk.append(y)
    else:
        x = stk.pop()
        DP[x] = F[x]  # Start with own subtree size
        for y in G[x]:
            if visited[y] and stk.count(y) == 0:  # y is a child
                DP[x] += DP[y]  # Add child's DP value

# Third phase: Rerooting to find maximum
ans = [0] * n
ans[0] = DP[0]  # Initial value for root
stk = [0]
visited = [0] * n
visited[0] = 1
Z = DP[0]  # Maximum answer

while stk:
    x = stk.pop()
    for y in G[x]:
        if not visited[y]:
            # Rerooting formula: ans[y] = ans[x] + n - 2*F[y]
            # This formula updates the answer when we reroot from x to y
            ay = ans[x] + n - 2 * F[y]
            ans[y] = ay
            Z = max(Z, ay)  # Update maximum
            visited[y] = 1
            stk.append(y)

print(Z)