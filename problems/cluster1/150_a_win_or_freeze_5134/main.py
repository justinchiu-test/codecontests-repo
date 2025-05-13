#!/usr/bin/env python3

from library import read_int, win_or_freeze, prime_factors

n = read_int()

# For this game:
# - If n = 1, player 1 can't make a move, so player 1 wins (print 0)
# - If n is prime, player 1 can't make a move, so player 1 wins (print 0)
# - If n has exactly 2 prime factors, player 2 wins
# - If n has more than 2 prime factors, player 1 can win by taking a suitable first move

# Get all prime factors
factors = prime_factors(n)

if n == 1 or len(factors) == 1:
    # Player 1 wins (can't make a move)
    print(1)
    print(0)
elif len(factors) == 2:
    # Player 2 wins
    print(2)
else:
    # Player 1 wins by taking first two prime factors
    first_move = factors[0] * factors[1]
    print(1)
    print(first_move)