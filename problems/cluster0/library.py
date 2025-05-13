"""
Library file for cluster0.
This contains shared code that can be imported by problems in this cluster.
"""
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def read_int():
    """Read a single integer from input."""
    return int(input())

def read_ints():
    """Read a list of integers from input."""
    return map(int, input().split())

def read_list():
    """Read a list of integers and return as a list."""
    return list(read_ints())

def read_str():
    """Read a string from input (excluding newline)."""
    return input().strip()

def read_strs():
    """Read a list of strings from input."""
    return input().split()
