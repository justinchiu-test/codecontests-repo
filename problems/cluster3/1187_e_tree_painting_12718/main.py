#!/usr/bin/env python3
from sys import path
path.append("/home/justinchiu_cohere_com/codecontests-repo/problems/cluster3")
from library import read_int, calculate_subtree_sizes

def main():
    n = read_int()
    
    # Read the tree (convert to 0-indexed)
    adj = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    
    # Step 1: Calculate subtree sizes
    subtree_sizes = calculate_subtree_sizes(adj, 0)
    
    # Step 2: Calculate initial DP value (score when rooted at the initial root)
    dp = [0] * n
    
    def dfs_dp(node, parent):
        dp[node] = subtree_sizes[node]  # Initial score is the subtree size
        for child in adj[node]:
            if child != parent:
                dfs_dp(child, node)
                dp[node] += dp[child]  # Add scores from all children
    
    dfs_dp(0, -1)
    
    # Step 3: Reroot and find maximum score
    max_score = dp[0]
    answer = [0] * n
    answer[0] = dp[0]
    
    def dfs_reroot(node, parent):
        for child in adj[node]:
            if child != parent:
                # When rerooting to child, we:
                # 1. Lose the subtree rooted at child
                # 2. Gain the rest of the tree
                answer[child] = answer[node] + n - 2 * subtree_sizes[child]
                nonlocal max_score
                max_score = max(max_score, answer[child])
                dfs_reroot(child, node)
    
    dfs_reroot(0, -1)
    
    print(max_score)

if __name__ == "__main__":
    main()