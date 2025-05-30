# 1149_B. Three Religions

**ID:** 1149_b_three_religions_220
**Difficulty:** 8

## Description

During the archaeological research in the Middle East you found the traces of three ancient religions: First religion, Second religion and Third religion. You compiled the information on the evolution of each of these beliefs, and you now wonder if the followers of each religion could coexist in peace.

The Word of Universe is a long word containing the lowercase English characters only. At each moment of time, each of the religion beliefs could be described by a word consisting of lowercase English characters.

The three religions can coexist in peace if their descriptions form disjoint subsequences of the Word of Universe. More formally, one can paint some of the characters of the Word of Universe in three colors: 1, 2, 3, so that each character is painted in at most one color, and the description of the i-th religion can be constructed from the Word of Universe by removing all characters that aren't painted in color i.

The religions however evolve. In the beginning, each religion description is empty. Every once in a while, either a character is appended to the end of the description of a single religion, or the last character is dropped from the description. After each change, determine if the religions could coexist in peace.

Input

The first line of the input contains two integers n, q (1 ≤ n ≤ 100 000, 1 ≤ q ≤ 1000) — the length of the Word of Universe and the number of religion evolutions, respectively. The following line contains the Word of Universe — a string of length n consisting of lowercase English characters.

Each of the following line describes a single evolution and is in one of the following formats: 

  * + i c (i ∈ \{1, 2, 3\}, c ∈ \{a, b, ..., z\}: append the character c to the end of i-th religion description. 
  * - i (i ∈ \{1, 2, 3\}) – remove the last character from the i-th religion description. You can assume that the pattern is non-empty. 



You can assume that no religion will have description longer than 250 characters.

Output

Write q lines. The i-th of them should be YES if the religions could coexist in peace after the i-th evolution, or NO otherwise.

You can print each character in any case (either upper or lower).

Examples

Input


6 8
abdabc
+ 1 a
+ 1 d
+ 2 b
+ 2 c
+ 3 a
+ 3 b
+ 1 c
- 2


Output


YES
YES
YES
YES
YES
YES
NO
YES


Input


6 8
abbaab
+ 1 a
+ 2 a
+ 3 a
+ 1 b
+ 2 b
+ 3 b
- 1
+ 2 z


Output


YES
YES
YES
YES
YES
NO
YES
NO

Note

In the first example, after the 6th evolution the religion descriptions are: ad, bc, and ab. The following figure shows how these descriptions form three disjoint subsequences of the Word of Universe:

<image>

## Categories

- dp
- implementation
- strings

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
6 8
abdabc
+ 1 a
+ 1 d
+ 2 b
+ 2 c
+ 3 a
+ 3 b
+ 1 c
- 2
```

**Output**:
```
YES
YES
YES
YES
YES
YES
NO
YES
```

### Example 2

**Input**:
```
6 8
abbaab
+ 1 a
+ 2 a
+ 3 a
+ 1 b
+ 2 b
+ 3 b
- 1
+ 2 z
```

**Output**:
```
YES
YES
YES
YES
YES
NO
YES
NO
```

### Example 3

**Input**:
```
1 1
t
+ 2 p
```

**Output**:
```
NO
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
