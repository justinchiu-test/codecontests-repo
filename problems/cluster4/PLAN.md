## PLAN for Library and Refactoring

### Objectives
- Identify common patterns across problem solutions
- Create a shared `library.py` with reusable components
- Refactor each `main.py` to use the library for I/O and utilities

### Library Components
1. **Fast I/O**
   - Token-based scanner: `ni()` (int), `nf()` (float), `ns()` (string), `na(n)` (list of n ints)
2. **2D Vector Operations**
   - Class `Vec`: constructors, addition, subtraction, dot, cross, norm², normalization, rotation, scaling, angle
   - Utility `eq(a, b, eps)` for float comparison
3. **Math Utilities**
   - `gcd` imported from `math`
   - `atan2`, `pi`, `hypot` imported as needed

### Refactoring Strategy
1. Replace all ad-hoc input parsing (`input()`, `next(stdin)`) with library I/O (`ni()`, `na()`).
2. Remove duplicated geometry/vector classes and use `library.Vec` and associated methods.
3. Keep problem-specific logic in `main.py`, import only the needed routines.
4. For advanced geometry problems, extend `library.py` with additional classes/functions as needed.
5. Iterate: refactor one problem, run its tests, extend library for missing functionality, then proceed.
