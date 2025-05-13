"""
Library file for cluster6.
This contains shared code that can be imported by problems in this cluster.
"""
import sys
import math
from collections import defaultdict, Counter, deque
from functools import lru_cache
import heapq
from fractions import Fraction

# Common constants
MOD = 10**9 + 7
MOD_ALT = 998244353

# I/O utilities
def read_int():
    """Read a single integer from stdin."""
    return int(input())

def read_ints():
    """Read a line of space-separated integers from stdin."""
    return list(map(int, input().split()))

def read_int_tuple():
    """Read a line of space-separated integers as a tuple."""
    return tuple(map(int, input().split()))

def read_float_tuple():
    """Read a line of space-separated floats as a tuple."""
    return tuple(map(float, input().split()))

def read_str():
    """Read a string from stdin."""
    return input().strip()

def read_strs():
    """Read a line of space-separated strings from stdin."""
    return input().split()

def read_test_cases():
    """Read t test cases, each with a block of input."""
    t = read_int()
    for _ in range(t):
        yield _

# Fast I/O 
def set_fast_io():
    """Setup fast I/O for competitive programming."""
    sys.stdin = open(0)
    sys.stdout = open(1, 'w')
    
    def input():
        return sys.stdin.readline().rstrip()

# Number theory utilities
def gcd(a, b):
    """Compute greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Compute least common multiple of a and b."""
    return a * b // gcd(a, b)

def extended_gcd(a, b):
    """Extended Euclidean algorithm, returns (g, x, y) such that a*x + b*y = g = gcd(a, b)."""
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)

def mod_inverse(a, m=MOD):
    """Compute the modular multiplicative inverse of a modulo m."""
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

# Fraction utilities
def simplify_fraction(numerator, denominator):
    """Simplify a fraction and return it as a string in the format 'A/B'."""
    if denominator == 0:
        return "Undefined"
    if numerator == 0:
        return "0/1"
    
    g = gcd(abs(numerator), abs(denominator))
    numerator //= g
    denominator //= g
    
    if denominator < 0:
        numerator, denominator = -numerator, -denominator
    
    if denominator == 1:
        return f"{numerator}/1"
    
    return f"{numerator}/{denominator}"

# Probability utilities
def expected_value(probabilities, values):
    """Calculate expected value given probabilities and corresponding values."""
    return sum(p * v for p, v in zip(probabilities, values))

def bernoulli_trial(success_prob, trials):
    """Calculate probability of at least one success in n independent trials."""
    return 1 - (1 - success_prob) ** trials

def binomial_probability(n, k, p):
    """Calculate binomial probability: P(X = k) where X ~ B(n, p)."""
    comb = Combinatorics().combination(n, k)
    return comb * (p ** k) * ((1 - p) ** (n - k))

def conditional_probability(p_a_and_b, p_b):
    """Calculate conditional probability P(A|B) = P(A and B) / P(B)."""
    if p_b == 0:
        return 0
    return p_a_and_b / p_b

# Factorial and combinations
class Combinatorics:
    def __init__(self, max_n=200000, mod=MOD):
        self.mod = mod
        self.max_n = max_n
        self._precompute_factorials()
        
    def _precompute_factorials(self):
        """Precompute factorials and inverse factorials."""
        self.fact = [1] * (self.max_n + 1)
        self.inv = [0] * (self.max_n + 1)
        self.inv_fact = [1] * (self.max_n + 1)
        
        for i in range(1, self.max_n + 1):
            self.fact[i] = (self.fact[i - 1] * i) % self.mod
        
        self.inv[1] = 1
        for i in range(2, self.max_n + 1):
            self.inv[i] = self.mod - (self.mod // i) * self.inv[self.mod % i] % self.mod
        
        for i in range(1, self.max_n + 1):
            self.inv_fact[i] = (self.inv_fact[i - 1] * self.inv[i]) % self.mod
    
    def factorial(self, n):
        """Return n! % mod."""
        if n < 0:
            return 0
        if n > self.max_n:
            result = 1
            for i in range(1, n + 1):
                result = (result * i) % self.mod
            return result
        return self.fact[n]
    
    def inverse_factorial(self, n):
        """Return (n!)^-1 % mod."""
        if n < 0:
            return 0
        if n > self.max_n:
            return mod_inverse(self.factorial(n), self.mod)
        return self.inv_fact[n]
    
    def combination(self, n, k):
        """Return nCk % mod."""
        if k < 0 or k > n:
            return 0
        return (self.fact[n] * self.inv_fact[k] % self.mod * self.inv_fact[n - k]) % self.mod
    
    def permutation(self, n, k):
        """Return nPk % mod."""
        if k < 0 or k > n:
            return 0
        return (self.fact[n] * self.inv_fact[n - k]) % self.mod

# Modular arithmetic
def mod_pow(base, exponent, modulus=MOD):
    """Compute (base^exponent) % modulus efficiently."""
    if modulus == 1:
        return 0
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

def mod_add(a, b, mod=MOD):
    """Compute (a + b) % mod."""
    return (a + b) % mod

def mod_sub(a, b, mod=MOD):
    """Compute (a - b) % mod."""
    return (a - b) % mod

def mod_mul(a, b, mod=MOD):
    """Compute (a * b) % mod."""
    return (a * b) % mod

def mod_div(a, b, mod=MOD):
    """Compute (a / b) % mod."""
    return (a * mod_inverse(b, mod)) % mod

# Dynamic Programming
class DP:
    @staticmethod
    def memoize(f):
        """Simple memoization decorator."""
        memo = {}
        def helper(*args):
            if args not in memo:
                memo[args] = f(*args)
            return memo[args]
        return helper
    
    @staticmethod
    def create_dp_table(dimensions, default=0):
        """Create a DP table with the given dimensions."""
        if len(dimensions) == 1:
            return [default] * dimensions[0]
        return [DP.create_dp_table(dimensions[1:], default) for _ in range(dimensions[0])]
    
    @staticmethod
    def probability_dp(states, transitions, initial_state):
        """
        Solve probability DP problems.
        
        Args:
            states: List of possible states
            transitions: Dict mapping state to list of (next_state, probability) pairs
            initial_state: Starting state
            
        Returns:
            Dict mapping each state to its probability
        """
        probs = {state: 0 for state in states}
        probs[initial_state] = 1
        
        for state in states:
            for next_state, prob in transitions.get(state, []):
                probs[next_state] += probs[state] * prob
                
        return probs

# Game theory utilities
def game_theory_dp(states, is_winning, memoize=True):
    """
    Determine if the current player can win from each state in a game.
    
    Args:
        states: List of possible game states
        is_winning: Function that takes a state and returns True if it's a winning state
        
    Returns:
        Dict mapping each state to True if it's a winning state, False otherwise
    """
    memo = {}
    
    def can_win(state):
        if state in memo:
            return memo[state]
        
        if is_winning(state):
            result = True
        else:
            result = False
            for next_state in get_next_states(state):
                if not can_win(next_state):
                    result = True
                    break
                    
        if memoize:
            memo[state] = result
        return result
    
    return {state: can_win(state) for state in states}

# Common operations for subset problems
def subset_sum(nums, target):
    """
    Determine if there's a subset of nums that sums to target.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        True if there's a subset that sums to target, False otherwise
    """
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] |= dp[i - num]
            
    return dp[target]

def count_subsets_with_sum(nums, target):
    """
    Count the number of subsets of nums that sum to target.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        Number of subsets that sum to target
    """
    dp = [0] * (target + 1)
    dp[0] = 1
    
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] += dp[i - num]
            
    return dp[target]