# 900_E. Maximum Questions

**ID:** 900_e_maximum_questions_7560
**Difficulty:** 11

## Description

Vasya wrote down two strings s of length n and t of length m consisting of small English letters 'a' and 'b'. What is more, he knows that string t has a form "abab...", namely there are letters 'a' on odd positions and letters 'b' on even positions.

Suddenly in the morning, Vasya found that somebody spoiled his string. Some letters of the string s were replaced by character '?'.

Let's call a sequence of positions i, i + 1, ..., i + m - 1 as occurrence of string t in s, if 1 ≤ i ≤ n - m + 1 and t1 = si, t2 = si + 1, ..., tm = si + m - 1.

The boy defines the beauty of the string s as maximum number of disjoint occurrences of string t in s. Vasya can replace some letters '?' with 'a' or 'b' (letters on different positions can be replaced with different letter). Vasya wants to make some replacements in such a way that beauty of string s is maximum possible. From all such options, he wants to choose one with the minimum number of replacements. Find the number of replacements he should make.

Input

The first line contains a single integer n (1 ≤ n ≤ 105) — the length of s.

The second line contains the string s of length n. It contains small English letters 'a', 'b' and characters '?' only.

The third line contains a single integer m (1 ≤ m ≤ 105) — the length of t. The string t contains letters 'a' on odd positions and 'b' on even positions.

Output

Print the only integer — the minimum number of replacements Vasya has to perform to make the beauty of string s the maximum possible.

Examples

Input

5
bb?a?
1


Output

2


Input

9
ab??ab???
3


Output

2

Note

In the first sample string t has a form 'a'. The only optimal option is to replace all characters '?' by 'a'.

In the second sample using two replacements we can make string equal to "aba?aba??". It is impossible to get more than two occurrences.

## Categories

- data structures
- dp
- strings

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
9
ab??ab???
3
```

**Output**:
```
2
```

### Example 2

**Input**:
```
5
bb?a?
1
```

**Output**:
```
2
```

### Example 3

**Input**:
```
14
a?a?b????b?ba?
3
```

**Output**:
```
7
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
