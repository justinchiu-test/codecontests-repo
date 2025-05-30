# 327_C. Magic Five

**ID:** 327_c_magic_five_12222
**Difficulty:** 9

## Description

There is a long plate s containing n digits. Iahub wants to delete some digits (possibly none, but he is not allowed to delete all the digits) to form his "magic number" on the plate, a number that is divisible by 5. Note that, the resulting number may contain leading zeros.

Now Iahub wants to count the number of ways he can obtain magic number, modulo 1000000007 (109 + 7). Two ways are different, if the set of deleted positions in s differs.

Look at the input part of the statement, s is given in a special form.

Input

In the first line you're given a string a (1 ≤ |a| ≤ 105), containing digits only. In the second line you're given an integer k (1 ≤ k ≤ 109). The plate s is formed by concatenating k copies of a together. That is n = |a|·k.

Output

Print a single integer — the required number of ways modulo 1000000007 (109 + 7).

Examples

Input

1256
1


Output

4


Input

13990
2


Output

528


Input

555
2


Output

63

Note

In the first case, there are four possible ways to make a number that is divisible by 5: 5, 15, 25 and 125.

In the second case, remember to concatenate the copies of a. The actual plate is 1399013990.

In the third case, except deleting all digits, any choice will do. Therefore there are 26 - 1 = 63 possible ways to delete digits.

## Categories

- combinatorics
- math

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
1256
1
```

**Output**:
```
4
```

### Example 2

**Input**:
```
555
2
```

**Output**:
```
63
```

### Example 3

**Input**:
```
13990
2
```

**Output**:
```
528
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
