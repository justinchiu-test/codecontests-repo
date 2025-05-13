#!/usr/bin/env python3

from library import fast_int, fast_int_list

t = fast_int()
for _ in range(t):
    n = fast_int()
    nums = fast_int_list()
    max_val = max(nums)
    found_k = False
    
    for k in range(1, 2*max_val+1):
        xor_nums = [num ^ k for num in nums]
        if all(x in nums for x in xor_nums):
            print(k)
            found_k = True
            break
    
    if not found_k:
        print(-1)