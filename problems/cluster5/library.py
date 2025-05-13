"""Library file for CodeContests cluster.
This provides fast I/O overrides and helper functions to simplify input parsing.
"""
import sys

# Override built-in input to use sys.stdin.readline and strip newline
def input(prompt=None):
    return sys.stdin.readline().rstrip('\n')

# Convenience functions for input parsing
def read_int():
    return int(input())

def read_ints():
    return map(int, input().split())

def read_list():
    return list(read_ints())

def read_str():
    return input()

def read_strs():
    return input().split()

# Read all remaining tokens from stdin (useful for problems needing all input at once)
def read_all():
    """Return a list of all whitespace-separated tokens from stdin."""
    return sys.stdin.read().split()

def read_all_ints():
    """Return an iterator of all ints from stdin."""
    return map(int, read_all())

# Set recursion limit high for recursive problems
sys.setrecursionlimit(10**7)
import builtins
# Override built-in input globally
builtins.input = input
