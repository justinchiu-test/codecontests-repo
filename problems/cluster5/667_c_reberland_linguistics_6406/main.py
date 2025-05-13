#!/usr/bin/env python3

def main():
    # Read input and preprocess
    s = input().strip()
    
    # Skip the "bereb" prefix and reverse the string for easier processing
    s = s[5:][::-1]
    n = len(s)
    
    # Set of all suffixes that can be added to the language
    mu = set()
    
    # can2[i] = whether we can add a 2-letter suffix ending at position i
    # can3[i] = whether we can add a 3-letter suffix ending at position i
    can2 = [0] * (n + 1)
    can3 = [0] * (n + 1)
    
    # Handle base cases
    if n >= 2:
        mu.add(s[0:2][::-1])
        can2[2] = 1
        
    if n >= 3:
        mu.add(s[0:3][::-1])
        can3[3] = 1
        
    if n >= 4 and s[0:2] != s[2:4]:
        mu.add(s[2:4][::-1])
        can2[4] = 1
        
    if n >= 5:
        mu.add(s[2:5][::-1])
        mu.add(s[3:5][::-1])
        can2[5] = 1
        can3[5] = 1
    
    # Fill the DP arrays and build the set of suffixes
    for i in range(6, n + 1):
        # Add 3-letter suffix using a 2-letter suffix that ends 3 positions back
        if can2[i - 3]:
            mu.add(s[i - 3:i][::-1])
            can3[i] = 1
        
        # Add 2-letter suffix using a 2-letter suffix that ends 2 positions back
        if can2[i - 2]:
            if s[i - 2:i] != s[i - 4:i - 2]:
                mu.add(s[i - 2:i][::-1])
                can2[i] = 1
        
        # Add 2-letter suffix using a 3-letter suffix that ends 2 positions back
        if can3[i - 2]:
            mu.add(s[i - 2:i][::-1])
            can2[i] = 1
        
        # Add 3-letter suffix using a 3-letter suffix that ends 3 positions back
        if can3[i - 3]:
            if s[i - 3:i] != s[i - 6:i - 3]:
                mu.add(s[i - 3:i][::-1])
                can3[i] = 1
    
    # Print results
    print(len(mu))
    print('\n'.join(sorted(list(mu))))

if __name__ == "__main__":
    main()