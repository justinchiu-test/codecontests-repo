# 774_H. Repairing Of String

**ID:** 774_h_repairing_of_string_9638
**Difficulty:** 14

## Description

Stepan had a favorite string s which consisted of the lowercase letters of the Latin alphabet. 

After graduation, he decided to remember it, but it was a long time ago, so he can't now remember it. But Stepan remembers some information about the string, namely the sequence of integers c1, c2, ..., cn, where n equals the length of the string s, and ci equals the number of substrings in the string s with the length i, consisting of the same letters. The substring is a sequence of consecutive characters in the string s.

For example, if the Stepan's favorite string is equal to "tttesst", the sequence c looks like: c = [7, 3, 1, 0, 0, 0, 0].

Stepan asks you to help to repair his favorite string s according to the given sequence c1, c2, ..., cn. 

Input

The first line contains the integer n (1 ≤ n ≤ 2000) — the length of the Stepan's favorite string.

The second line contains the sequence of integers c1, c2, ..., cn (0 ≤ ci ≤ 2000), where ci equals the number of substrings of the string s with the length i, consisting of the same letters.

It is guaranteed that the input data is such that the answer always exists.

Output

Print the repaired Stepan's favorite string. If there are several answers, it is allowed to print any of them. The string should contain only lowercase letters of the English alphabet. 

Examples

Input

6
6 3 1 0 0 0


Output

kkrrrq

Input

4
4 0 0 0


Output

abcd

Note

In the first test Stepan's favorite string, for example, can be the string "kkrrrq", because it contains 6 substrings with the length 1, consisting of identical letters (they begin in positions 1, 2, 3, 4, 5 and 6), 3 substrings with the length 2, consisting of identical letters (they begin in positions 1, 3 and 4), and 1 substring with the length 3, consisting of identical letters (it begins in the position 3). 

## Categories

- *special
- constructive algorithms

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
6
6 3 1 0 0 0
```

**Output**:
```
aaabba
```

### Example 2

**Input**:
```
4
4 0 0 0
```

**Output**:
```
abab
```

### Example 3

**Input**:
```
200
200 180 160 140 122 106 92 79 69 60 52 45 38 32 26 20 14 8 4 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

**Output**:
```
aaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbaaaaaaaaaaaabbbbbbbbbbaaaaaaaaabbbbbbbbaaaaaaabbbbbbbaaaaaaabbbbbbaaaaabbbbbaaaabbbbaaabbb
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
