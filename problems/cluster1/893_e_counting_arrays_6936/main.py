#!/usr/bin/env python3

from library import read_ints, mod_pow, MOD

# Implementation of combination calculation
class Combination:
    def __init__(self, mod):
        self.mod = mod
        self.factorials = [1, 1]
        self.inv_modulos = [0, 1]
        self.inv_factorials = [1, 1]
    
    def factorial(self, n):
        """Calculate n! mod MOD"""
        while n >= len(self.factorials):
            self.factorials.append((self.factorials[-1] * len(self.factorials)) % self.mod)
        return self.factorials[n]
    
    def inv(self, n):
        """Calculate modular inverse of n"""
        while n >= len(self.inv_modulos):
            # Using Fermat's little theorem: a^(p-2) ≡ a^(-1) (mod p) if p is prime
            self.inv_modulos.append(mod_pow(len(self.inv_modulos), self.mod - 2, self.mod))
        return self.inv_modulos[n]
    
    def inv_factorial(self, n):
        """Calculate modular inverse of n!"""
        while n >= len(self.inv_factorials):
            next_val = (self.inv_factorials[-1] * self.inv(len(self.inv_factorials))) % self.mod
            self.inv_factorials.append(next_val)
        return self.inv_factorials[n]
    
    def ncr(self, n, k):
        """Calculate nCk mod MOD"""
        if k < 0 or n < k:
            return 0
        return (self.factorial(n) * self.inv_factorial(k) % self.mod * self.inv_factorial(n - k) % self.mod)

def count_arrays(x, y):
    """
    Count the number of arrays with given constraints.
    x is the product of all array elements
    y is the length of the array
    """
    combo = Combination(MOD)
    
    # Handle prime factorization of x
    result = 1
    
    # Handle powers of 2
    count = 0
    while x % 2 == 0:
        count += 1
        x //= 2
    if count > 0:
        result = (result * combo.ncr(y + count - 1, count)) % MOD
    
    # Handle odd prime factors
    for i in range(3, int(x**0.5) + 1, 2):
        count = 0
        while x % i == 0:
            x //= i
            count += 1
        if count > 0:
            result = (result * combo.ncr(y + count - 1, count)) % MOD
    
    # Handle remaining prime if any
    if x > 2:
        result = (result * y) % MOD
    
    # Multiply by 2^(y-1) for possible sign combinations
    result = (result * mod_pow(2, y - 1, MOD)) % MOD
    
    return result

def main():
    t = int(input())
    for _ in range(t):
        x, y = read_ints()
        print(count_arrays(x, y))

if __name__ == "__main__":
    main()