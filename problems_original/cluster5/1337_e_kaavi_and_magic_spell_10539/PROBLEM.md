# 1337_E. Kaavi and Magic Spell

**ID:** 1337_e_kaavi_and_magic_spell_10539
**Difficulty:** 11

## Description

Kaavi, the mysterious fortune teller, deeply believes that one's fate is inevitable and unavoidable. Of course, she makes her living by predicting others' future. While doing divination, Kaavi believes that magic spells can provide great power for her to see the future. 

<image>

Kaavi has a string T of length m and all the strings with the prefix T are magic spells. Kaavi also has a string S of length n and an empty string A.

During the divination, Kaavi needs to perform a sequence of operations. There are two different operations:

  * Delete the first character of S and add it at the front of A.
  * Delete the first character of S and add it at the back of A.



Kaavi can perform no more than n operations. To finish the divination, she wants to know the number of different operation sequences to make A a magic spell (i.e. with the prefix T). As her assistant, can you help her? The answer might be huge, so Kaavi only needs to know the answer modulo 998 244 353.

Two operation sequences are considered different if they are different in length or there exists an i that their i-th operation is different. 

A substring is a contiguous sequence of characters within a string. A prefix of a string S is a substring of S that occurs at the beginning of S.

Input

The first line contains a string S of length n (1 ≤ n ≤ 3000).

The second line contains a string T of length m (1 ≤ m ≤ n).

Both strings contain only lowercase Latin letters.

Output

The output contains only one integer — the answer modulo 998 244 353.

Examples

Input


abab
ba


Output


12

Input


defineintlonglong
signedmain


Output


0

Input


rotator
rotator


Output


4

Input


cacdcdbbbb
bdcaccdbbb


Output


24

Note

The first test:

<image>

The red ones are the magic spells. In the first operation, Kaavi can either add the first character "a" at the front or the back of A, although the results are the same, they are considered as different operations. So the answer is 6×2=12.

## Categories

- dp
- strings

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
cacdcdbbbb
bdcaccdbbb
```

**Output**:
```
24
```

### Example 2

**Input**:
```
defineintlonglong
signedmain
```

**Output**:
```
0
```

### Example 3

**Input**:
```
abab
ba
```

**Output**:
```
12
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
