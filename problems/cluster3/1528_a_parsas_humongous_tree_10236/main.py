#!/usr/bin/env python3

from library import setup_io

# Set up fast I/O
input = setup_io()

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())

        # Read value ranges for each node
        l_values = []
        r_values = []
        for _ in range(n):
            l, r = map(int, input().split())
            l_values.append(l)
            r_values.append(r)

        # Build tree as adjacency list (0-indexed)
        adj = [[] for _ in range(n)]
        for _ in range(n-1):
            a, b = map(int, input().split())
            a -= 1  # Convert to 0-indexed
            b -= 1
            adj[a].append(b)
            adj[b].append(a)

        # DP approach: post-order traversal to calculate max sum
        # dp[node][0] = max sum when node has value l_values[node]
        # dp[node][1] = max sum when node has value r_values[node]
        parent = [-1] * n
        stack = []
        stack.append(~0)
        stack.append(0)
        dp = [[0, 0] for _ in range(n)]

        # Iterative post-order traversal
        while stack:
            node = stack.pop()

            if node >= 0:
                # First visit: process children
                for child in adj[node]:
                    if child == parent[node]:
                        continue
                    parent[child] = node
                    # Push complement for post-processing after all children
                    stack.append(~child)
                    # Push child for processing
                    stack.append(child)
            else:
                # Post-processing after all children are processed
                child = ~node  # Get actual child node
                node = parent[child]  # Get parent node

                if node == -1:
                    continue

                # Calculate max sum for each possible value of the parent
                # When parent has l_values[node]:
                dp_l = max(
                    dp[child][0] + abs(l_values[node] - l_values[child]),  # Child has l_value
                    dp[child][1] + abs(l_values[node] - r_values[child])   # Child has r_value
                )

                # When parent has r_values[node]:
                dp_r = max(
                    dp[child][0] + abs(r_values[node] - l_values[child]),  # Child has l_value
                    dp[child][1] + abs(r_values[node] - r_values[child])   # Child has r_value
                )

                # Update parent's DP values
                dp[node][0] += dp_l
                dp[node][1] += dp_r

        # Answer is the maximum of the two possible values for the root
        print(max(dp[0]))

if __name__ == "__main__":
    main()