"""
Library file for cluster6.
This contains shared code that can be imported by problems in this cluster.
"""
import sys
import builtins

# Override built-in input for faster IO
builtins.input = sys.stdin.readline

# Token-based scanner
_tokens = None
def _init_tokens():
    return sys.stdin.read().split()

def _token_iter():
    global _tokens
    if _tokens is None:
        _tokens = iter(_init_tokens())
    return _tokens

def ni():
    """Read next integer token"""
    return int(next(_token_iter()))

def nf():
    """Read next float token"""
    return float(next(_token_iter()))

def ns():
    """Read next string token"""
    return next(_token_iter())

def ar_int(n):
    """Read list of n integers"""
    return [ni() for _ in range(n)]

def ar_float(n):
    """Read list of n floats"""
    return [nf() for _ in range(n)]

def ar_str(n):
    """Read list of n string tokens"""
    return [ns() for _ in range(n)]

# Extended GCD
def egcd(a, b):
    if b == 0:
        return (1, 0, a)
    x, y, g = egcd(b, a % b)
    return (y, x - (a // b) * y, g)

def mod_inv(a, m):
    """Modular inverse of a under modulo m"""
    x, y, g = egcd(a, m)
    return x % m

class Comb:
    """Combination helper with precomputed factorials"""
    def __init__(self, n, mod=10**9+7):
        self.mod = mod
        self.fact = [1] * (n + 1)
        self.invfact = [1] * (n + 1)
        for i in range(2, n + 1):
            self.fact[i] = self.fact[i-1] * i % mod
        self.invfact[n] = pow(self.fact[n], mod - 2, mod)
        for i in range(n, 0, -1):
            self.invfact[i-1] = self.invfact[i] * i % mod
    def C(self, n, k):
        if k < 0 or k > n:
            return 0
        return self.fact[n] * self.invfact[k] % self.mod * self.invfact[n-k] % self.mod

def pf(x, prec=10):
    """Print float x with given precision"""
    fmt = "{:." + str(prec) + "f}"
    print(fmt.format(x))
