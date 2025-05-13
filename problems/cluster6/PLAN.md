# Plan for cluster6 Library

## Objectives
- Consolidate common functionality across problem solutions to reduce code duplication
    - Faster and consistent input/output handling
    - Simplified token scanning
    - Modular arithmetic utilities
    - Combination and factorial computations

## Proposed APIs (`library.py`)

### Input & IO
- Override built-in `input` to use `sys.stdin.readline` for speed

### Token Scanner
- `_tokens`: internal token iterator
- `ni()`: read next integer
- `nf()`: read next float
- `ns()`: read next string token
- `ar_int(n)`: read list of n integers
- `ar_float(n)`: read list of n floats
- `ar_str(n)`: read list of n strings

### Modular Arithmetic
- `egcd(a, b)`: extended GCD, returns (x, y, g)
- `mod_inv(a, m)`: modular inverse of a modulo m

### Combinatorics
- `class Comb`:
    - `__init__(self, n, mod=10**9+7)`: precompute `fact` and `invfact` up to n
    - `C(self, n, k)`: compute `n choose k` modulo `mod`

### Floating Utilities
- `pf(x, prec=10)`: print float `x` with `prec` decimal places

## Refactoring Steps

For each problem directory:

1. Add `import library` at the top of `main.py`
2. Remove custom input/IO boilerplate (e.g., FastIO classes, `input = ...` overrides)
3. Replace manual token parsing with scanner functions (`ni`, `ns`, etc.) where beneficial
4. Remove duplicated modular arithmetic code:
    - Replace `extgcd`/`mod_inv` definitions with `library.mod_inv`
    - Replace factorial + inverse precomputations with `Comb`
5. Replace direct prints of formatted floats with `library.pf`
6. Clean up unused helper functions
7. Run tests: `bash {problem}/run.sh` and ensure all pass

Repeat until every solution uses `library.py` and all tests pass.
