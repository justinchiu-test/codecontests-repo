#!/usr/bin/env python3

from library import read_int, read_strs

def solve():
    n = read_int()
    # Read probabilities and sort in descending order
    a = sorted(list(map(float, read_strs())), reverse=True)
    
    # If there's a probability of 1, the answer is 1
    if max(a) == 1:
        return 1.0
    
    # Pre-compute the product of (1-p) for the first i elements
    pre = [1] * (n + 1)
    pre[0] = 1
    for i in range(n):
        pre[i+1] = pre[i] * (1 - a[i])
    
    ans = 0
    # Try all possible subset sizes
    for i in range(1, n + 1):
        # Calculate the probability of getting exactly one problem
        # from the first i bloggers
        prob_one = 0
        for j in range(i):
            # For each blogger j, calculate probability that only they
            # come up with a problem
            prob_j_succeeds = a[j]
            prob_others_fail = pre[i] / (1 - a[j]) if a[j] < 1 else 0
            prob_one += prob_j_succeeds * prob_others_fail
        
        ans = max(ans, prob_one)
    
    return ans

# Format the output with 10 decimal places
print("{:.10f}".format(solve()))