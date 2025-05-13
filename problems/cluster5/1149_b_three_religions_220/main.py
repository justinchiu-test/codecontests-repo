#!/usr/bin/env python3

from library import build_next_occurrence, read_int_tuple

def main():
    n, q = read_int_tuple()
    s = '!' + input()  # 1-indexed with sentinel
    
    # Build next occurrence array
    nxt = build_next_occurrence(s)
    
    # Initialize DP state
    w = [[-1], [-1], [-1]]  # Religions words (represented as character codes)
    
    # Helper function to calculate the index in the flat DP array
    idx = lambda i, j, k: i * 65536 + j * 256 + k
    
    # Initialize DP array
    dp = [0] * (256 * 256 * 256)
    
    def calc(fix=None):
        """
        Calculate DP states, optionally fixing one religion's characters.
        
        Args:
            fix: If provided, only update DP states for the fixed religion's newest character
        """
        r = list(map(range, (len(w[0]), len(w[1]), len(w[2]))))
        if fix is not None: 
            r[fix] = range(len(w[fix]) - 1, len(w[fix]))
        
        for i in r[0]:
            for j in r[1]:
                for k in r[2]:
                    dp[idx(i, j, k)] = min(
                        nxt[w[0][i]][dp[idx(i - 1, j, k)]] if i else n + 1,
                        nxt[w[1][j]][dp[idx(i, j - 1, k)]] if j else n + 1,
                        nxt[w[2][k]][dp[idx(i, j, k - 1)]] if k else n + 1
                    )
                    if i == j == k == 0: 
                        dp[idx(i, j, k)] = 0
    
    results = []
    for _ in range(q):
        t, *r = input().split()
        if t == '+':
            i, c = int(r[0]) - 1, ord(r[1]) - 97
            w[i].append(c)
            calc(i)
        else:
            i = int(r[0]) - 1
            w[i].pop()
        
        # Check if all religions can coexist
        req = dp[idx(len(w[0]) - 1, len(w[1]) - 1, len(w[2]) - 1)]
        results.append('YES' if req <= n else 'NO')
    
    return results

if __name__ == "__main__":
    print(*main(), sep='\n')