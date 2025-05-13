#!/usr/bin/env python3

import sys
sys.path.append('..')
from library import INF, char_to_idx

def main():
    # Read input strings
    newspaper = input().strip()
    headline = input().strip()
    
    n_newspaper = len(newspaper)
    n_headline = len(headline)
    
    # Create a next occurrence array for each character in newspaper
    # dp[i][c] = next position of character c after position i in newspaper
    dp = [[-1 for _ in range(26)] for _ in range(n_newspaper + 1)]
    
    # Fill the next occurrence array from right to left
    for i in range(n_newspaper - 1, -1, -1):
        # Copy the next occurrences from the right position
        for j in range(26):
            dp[i][j] = dp[i + 1][j]
        # Update for the current character
        dp[i][char_to_idx(newspaper[i])] = i
    
    current_pos = 0  # Current position in newspaper
    copies_used = 1  # Number of newspaper copies used
    i = 0  # Index in headline
    
    # Iterate through each character in headline
    while i < n_headline:
        # If we've reached the end of the current newspaper, start new copy
        if current_pos == n_newspaper:
            copies_used += 1
            current_pos = 0
        
        # Character not found in current position, try from the beginning of a new copy
        if dp[current_pos][char_to_idx(headline[i])] == -1:
            copies_used += 1
            current_pos = 0
            
            # If still not found from the beginning, it's impossible to form the headline
            if dp[current_pos][char_to_idx(headline[i])] == -1:
                copies_used = INF
                break
        
        # Move to the position after the found character
        current_pos = dp[current_pos][char_to_idx(headline[i])] + 1
        i += 1
    
    print(copies_used if copies_used != INF else -1)

if __name__ == "__main__":
    main()