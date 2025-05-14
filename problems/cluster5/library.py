"""
Shared library for code compression benchmarks.
Provides concise IO helper functions for common patterns.
"""
import sys

def rl():
    """Read a line from stdin and strip the trailing newline."""
    return sys.stdin.readline().rstrip('\n')

def ri():
    """Read a line and convert to integer."""
    return int(rl())

def ril():
    """Read a line, split by whitespace, and convert to list of ints."""
    return list(map(int, rl().split()))

def rsl():
    """Read a line and split by whitespace into list of strings."""
    return rl().split()

def rg():
    """Read a line and return a generator of ints."""
    return map(int, rl().split())
