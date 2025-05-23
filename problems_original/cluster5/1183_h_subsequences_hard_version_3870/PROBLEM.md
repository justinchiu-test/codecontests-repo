# 1183_H. Subsequences (hard version)

**ID:** 1183_h_subsequences_hard_version_3870
**Difficulty:** 14

## Description

The only difference between the easy and the hard versions is constraints.

A subsequence is a string that can be derived from another string by deleting some or no symbols without changing the order of the remaining symbols. Characters to be deleted are not required to go successively, there can be any gaps between them. For example, for the string "abaca" the following strings are subsequences: "abaca", "aba", "aaa", "a" and "" (empty string). But the following strings are not subsequences: "aabaca", "cb" and "bcaa".

You are given a string s consisting of n lowercase Latin letters.

In one move you can take any subsequence t of the given string and add it to the set S. The set S can't contain duplicates. This move costs n - |t|, where |t| is the length of the added subsequence (i.e. the price equals to the number of the deleted characters).

Your task is to find out the minimum possible total cost to obtain a set S of size k or report that it is impossible to do so.

Input

The first line of the input contains two integers n and k (1 ≤ n ≤ 100, 1 ≤ k ≤ 10^{12}) — the length of the string and the size of the set, correspondingly.

The second line of the input contains a string s consisting of n lowercase Latin letters.

Output

Print one integer — if it is impossible to obtain the set S of size k, print -1. Otherwise, print the minimum possible total cost to do it.

Examples

Input


4 5
asdf


Output


4


Input


5 6
aaaaa


Output


15


Input


5 7
aaaaa


Output


-1


Input


10 100
ajihiushda


Output


233

Note

In the first example we can generate S = { "asdf", "asd", "adf", "asf", "sdf" }. The cost of the first element in S is 0 and the cost of the others is 1. So the total cost of S is 4.

## Categories

- dp
- strings

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
4 5
asdf
```

**Output**:
```
4
```

### Example 2

**Input**:
```
5 6
aaaaa
```

**Output**:
```
15
```

### Example 3

**Input**:
```
5 7
aaaaa
```

**Output**:
```
-1
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
