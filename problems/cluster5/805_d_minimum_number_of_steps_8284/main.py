#!/usr/bin/env python3

from library import MOD, mod_add

def main():
    string = input().strip()
    count_a = 0
    result = 0

    for char in string:
        if char == 'a':
            # Double the number of previous 'a's since each 'a' can be paired with any 'b'
            count_a = (count_a * 2) % MOD
            # Add 1 for the current 'a'
            count_a = mod_add(count_a, 1, MOD)
        elif char == 'b':
            # Each 'b' can be paired with any accumulated 'a's
            result = mod_add(result, count_a, MOD)
    
    return result

if __name__ == "__main__":
    print(main() % MOD)