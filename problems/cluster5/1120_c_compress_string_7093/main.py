#!/usr/bin/env python3

from library import z_function, read_ints, read_str

def main():
    n, a, b = read_ints()
    s = read_str()
    dp = [0] * n
    dp[0] = a
    
    for i in range(1, n):
        t = s[:i+1]
        dp[i] = dp[i-1] + a  # Default: encode as single character
        
        # Calculate Z function for the reversed prefix
        q = z_function(t[::-1])
        
        # Find maximum matches for each position
        maxs = [0] * (i+1)
        maxs[0] = q[i]
        for j in range(1, i):
            maxs[j] = max(maxs[j-1], q[i-j])
        
        # Check if we can encode current suffix using previous characters
        for j in range(i):
            if maxs[j] >= i-j:  # Complete match found
                dp[i] = min(dp[i], dp[j] + b)
    
    print(dp[-1])

if __name__ == "__main__":
    main()