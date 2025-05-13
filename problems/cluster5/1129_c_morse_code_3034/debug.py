#!/usr/bin/env python3

import sys
sys.path.append("/home/justinchiu_cohere_com/codecontests-repo/problems/cluster5")
from library import z_function

def main():
    # Test case: 3, 1, 1, 1
    nums = [3, 1, 1, 1]
    
    MOD = 10 ** 9 + 7
    BAD = ([0, 0, 1, 1], [0, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1])
    
    n = nums[0]
    s = []
    sm = 0
    ans = []
    
    for i in range(1, n + 1):
        s.append(nums[i])
        print(f"\nIteration {i}:")
        print(f"s = {s}")
        
        cur = 0
        f = [0] * (i + 1)
        f[i] = 1
        print(f"Initial f = {f}")
        
        for j in range(i - 1, -1, -1):
            print(f"  j = {j}")
            for k in range(j, min(j + 4, i)):
                print(f"    k = {k}, checking s[{j}:{k+1}] = {s[j:k+1]}")
                if tuple(s[j:k+1]) not in BAD:  # Fixed: convert to tuple for comparison
                    f[j] = (f[j] + f[k + 1]) % MOD
                    print(f"      Not in BAD, f[{j}] += f[{k+1}] = {f[j]}")
                else:
                    print(f"      In BAD, skipping")
        
        print(f"Final f = {f}")
        
        rev_s = s.copy()
        rev_s.reverse()
        z = z_function(rev_s)
        print(f"z of reversed s {rev_s} = {z}")
        
        max_z = max(z)
        new = i - max_z
        print(f"new = {i} - max({z}) = {i} - {max_z} = {new}")
        
        partial_sum = sum(f[:new]) % MOD
        sm = (sm + partial_sum) % MOD
        print(f"sm += sum(f[:new]) = {sm} + {partial_sum} = {sm}")
        
        ans.append(sm)
        print(f"Current answer: {ans}")
    
    print("\nFinal answer:")
    print(*ans, sep='\n')

if __name__ == "__main__":
    main()