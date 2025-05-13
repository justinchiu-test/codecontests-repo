#!/usr/bin/env python3

from library import MOD, mod_add

def main():
    s = input().strip()
    n = len(s)
    
    # a = number of ways to have no mine and no neighboring mine
    # b = number of ways to have no mine but neighboring mine
    # c = number of ways to have a mine with no forced neighboring mine
    # d = number of ways to have a mine with forced neighboring mine
    a, b, c, d = 1, 0, 0, 0
    
    for i in range(n):
        if s[i] == '*':
            # Cell has a mine, no numbers allowed
            t = (0, mod_add(mod_add(a, b, MOD), d, MOD), 0, 0)
        elif s[i] == '?':
            # Cell can be empty or have a mine
            t = (mod_add(a, mod_add(b, c, MOD), MOD), 
                 mod_add(a, mod_add(b, d, MOD), MOD), 
                 0, 0)
        elif s[i] == '0':
            # Cell has no mine and no neighboring mines
            t = (0, 0, mod_add(a, c, MOD), 0)
        elif s[i] == '1':
            # Cell has no mine but exactly one neighboring mine
            t = (0, 0, b, mod_add(a, c, MOD))
        else:  # s[i] == '2'
            # Cell has no mine but two neighboring mines
            t = (0, 0, 0, mod_add(b, d, MOD))
        
        a, b, c, d = t
    
    # The answer is the sum of valid arrangements ending with no mine or a mine
    # that doesn't force a neighboring mine
    result = mod_add(a, mod_add(b, c, MOD), MOD)
    print(result)

if __name__ == "__main__":
    main()