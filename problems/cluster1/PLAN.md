Library Plan
============

This document outlines the plan for `library.py`, which will contain shared utilities for all problems in this cluster.

1. IO Utilities
   - `read_int()` → Read and return a single integer from stdin.
   - `read_ints()` → Read a line of space-separated integers and return as a list.
   - `read_str()` → Read a line (string) without the trailing newline.
   - `read_strs()` → Read a line and split into a list of strings.
   - `read_all_ints()` → Read all remaining input and return as a list of integers.

2. Math Utilities
   - `gcd(a, b)` → Greatest common divisor (alias of `math.gcd`).
   - `lcm(a, b)` → Least common multiple.
   - `sieve(n)` → Return list of primes up to `n` (Eratosthenes sieve).
   - `prime_factors(n)` → Return list of prime factors of `n` (with multiplicity).
   - `prev_pow2(n)` → Largest power of two ≤ `n`.
   - `next_pow2(n)` → Smallest power of two ≥ `n`.

3. Modular Arithmetic
   - `modpow(a, b, mod)` → Compute `a**b % mod` efficiently.
   - `modinv(a, mod)` → Modular inverse of `a` under prime `mod` (Fermat's little theorem).

4. Solver Harness (optional)
   - If needed, support a `solve()` entrypoint and multiple-testcase boilerplate.

Once `library.py` is populated, solutions can import from it to reduce duplication.
