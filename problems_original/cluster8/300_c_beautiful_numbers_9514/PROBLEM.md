# 300_C. Beautiful Numbers

**ID:** 300_c_beautiful_numbers_9514
**Difficulty:** 9

## Description

Vitaly is a very weird man. He's got two favorite digits a and b. Vitaly calls a positive integer good, if the decimal representation of this integer only contains digits a and b. Vitaly calls a good number excellent, if the sum of its digits is a good number.

For example, let's say that Vitaly's favourite digits are 1 and 3, then number 12 isn't good and numbers 13 or 311 are. Also, number 111 is excellent and number 11 isn't. 

Now Vitaly is wondering, how many excellent numbers of length exactly n are there. As this number can be rather large, he asks you to count the remainder after dividing it by 1000000007 (109 + 7).

A number's length is the number of digits in its decimal representation without leading zeroes.

Input

The first line contains three integers: a, b, n (1 ≤ a < b ≤ 9, 1 ≤ n ≤ 106).

Output

Print a single integer — the answer to the problem modulo 1000000007 (109 + 7).

Examples

Input

1 3 3


Output

1


Input

2 3 10


Output

165

## Categories

- brute force
- combinatorics

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
1 3 3
```

**Output**:
```
1
```

### Example 2

**Input**:
```
2 3 10
```

**Output**:
```
165
```

### Example 3

**Input**:
```
2 5 53049
```

**Output**:
```
259705254
```


## Testing

Run the solution with:

```bash
./run.sh
```

Or test with a specific input file:

```bash
uv run main.py < tests/input_1.txt
```
