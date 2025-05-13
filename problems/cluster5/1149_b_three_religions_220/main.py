#!/usr/bin/env python3

from sys import path
path.append('..')
from library import read_ints, read_str, idx_3d, init_dp_1d

n, q = read_ints()
s = '!' + read_str()  # Add a dummy character at the beginning for 1-indexing

# Build next character positions table
# We'll implement this here directly since it's specific to this problem's needs
nxt = [[n + 1] * (n + 2) for _ in range(26)]
for i in range(n - 1, -1, -1):
    c = ord(s[i + 1]) - ord('a')
    for j in range(26):
        nxt[j][i] = nxt[j][i + 1]
    nxt[c][i] = i + 1

# Initialize religion words
w = [[-1], [-1], [-1]]

# Initialize DP array
dp = [0] * (256 * 256 * 256)

def calc(fix=None):
    """Calculate DP values for the given scenario."""
    # Generate ranges for each dimension
    r = list(map(range, (len(w[0]), len(w[1]), len(w[2]))))
    if fix is not None:
        r[fix] = range(len(w[fix]) - 1, len(w[fix]))
    
    # Update DP table
    for i in r[0]:
        for j in r[1]:
            for k in r[2]:
                idx_val = idx_3d(i, j, k)
                dp[idx_val] = min(
                    nxt[w[0][i]][dp[idx_3d(i - 1, j, k)]] if i else n + 1,
                    nxt[w[1][j]][dp[idx_3d(i, j - 1, k)]] if j else n + 1,
                    nxt[w[2][k]][dp[idx_3d(i, j, k - 1)]] if k else n + 1
                )
                if i == j == k == 0:
                    dp[idx_val] = 0

# Process queries
out = []
for _ in range(q):
    query = read_str().split()
    t = query[0]
    if t == '+':
        i, c = int(query[1]) - 1, ord(query[2]) - ord('a')  # Convert to 0-indexed
        w[i].append(c)
        calc(i)
    else:
        i = int(query[1]) - 1
        w[i].pop()
    
    # Check if religions can coexist
    req = dp[idx_3d(len(w[0]) - 1, len(w[1]) - 1, len(w[2]) - 1)]
    out.append('YES' if req <= n else 'NO')

print(*out, sep='\n')