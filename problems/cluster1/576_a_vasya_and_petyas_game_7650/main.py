#!/usr/bin/env python3

from library import read_int, is_prime

def main():
    n = read_int()
    answer = []
    
    # For each prime number p <= n, add all powers of p that are <= n
    for p in range(2, n + 1):
        if is_prime(p):
            # Add all powers of p that are <= n
            power = p
            while power <= n:
                answer.append(power)
                power *= p
    
    # Output the result
    print(len(answer))
    print(' '.join(map(str, answer)))

if __name__ == '__main__':
    main()