#!/usr/bin/env python3

from library import read_int_tuple, read_strs

def main():
    n, q = read_int_tuple()
    
    # Read the compression rules
    compression_rules = []
    for _ in range(q):
        compression_rules.append(read_strs())
    
    # Group rules by the second character (result of compression)
    rules_by_result = [[] for _ in range(6)]  # 'a' to 'f'
    alphabet = "abcdef"
    
    for rule in compression_rules:
        result_char = rule[1]
        source_char = rule[0]
        result_idx = alphabet.index(result_char)
        rules_by_result[result_idx].append(source_char)
    
    # DP approach: R[i] = number of strings of length i that compress to 'a'
    # Start with one valid string 'a' of length 1
    R = [1, 0, 0, 0, 0, 0]  # R[0] represents 'a'
    
    # Build up strings of length n
    for i in range(1, n):
        # For each iteration, we're building strings of length i+1
        next_R = [0, 0, 0, 0, 0, 0]
        
        # For each possible resulting character
        for j in range(6):
            # For each rule that produces this character
            for source in rules_by_result[j]:
                # The first character of the source
                first_char_idx = alphabet.index(source[0])
                # Add the count of strings that end with first_char_idx
                next_R[first_char_idx] += R[j]
        
        R = next_R[:]
    
    # The answer is the number of strings that compress to 'a'
    print(sum(R))

if __name__ == "__main__":
    main()