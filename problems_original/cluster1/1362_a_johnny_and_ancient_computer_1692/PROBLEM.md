# 1362_A. Johnny and Ancient Computer

**ID:** 1362_a_johnny_and_ancient_computer_1692
**Difficulty:** very hard

## Description

Johnny has recently found an ancient, broken computer. The machine has only one register, which allows one to put in there one variable. Then in one operation, you can shift its bits left or right by at most three positions. The right shift is forbidden if it cuts off some ones. So, in fact, in one operation, you can multiply or divide your number by 2, 4 or 8, and division is only allowed if the number is divisible by the chosen divisor. 

Formally, if the register contains a positive integer x, in one operation it can be replaced by one of the following: 

  * x ⋅ 2 
  * x ⋅ 4 
  * x ⋅ 8 
  * x / 2, if x is divisible by 2 
  * x / 4, if x is divisible by 4 
  * x / 8, if x is divisible by 8 



For example, if x = 6, in one operation it can be replaced by 12, 24, 48 or 3. Value 6 isn't divisible by 4 or 8, so there're only four variants of replacement.

Now Johnny wonders how many operations he needs to perform if he puts a in the register and wants to get b at the end.

Input

The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 1000) — the number of test cases. The following t lines contain a description of test cases.

The first and only line in each test case contains integers a and b (1 ≤ a, b ≤ 10^{18}) — the initial and target value of the variable, respectively.

Output

Output t lines, each line should contain one integer denoting the minimum number of operations Johnny needs to perform. If Johnny cannot get b at the end, then write -1.

Example

Input


10
10 5
11 44
17 21
1 1
96 3
2 128
1001 1100611139403776
1000000000000000000 1000000000000000000
7 1
10 8


Output


1
1
-1
0
2
2
14
0
-1
-1

Note

In the first test case, Johnny can reach 5 from 10 by using the shift to the right by one (i.e. divide by 2).

In the second test case, Johnny can reach 44 from 11 by using the shift to the left by two (i.e. multiply by 4).

In the third test case, it is impossible for Johnny to reach 21 from 17.

In the fourth test case, initial and target values are equal, so Johnny has to do 0 operations.

In the fifth test case, Johnny can reach 3 from 96 by using two shifts to the right: one by 2, and another by 3 (i.e. divide by 4 and by 8).

## Categories

- implementation

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
10
10 5
11 44
17 21
1 1
96 3
2 128
1001 1100611139403776
1000000000000000000 1000000000000000000
7 1
10 8
```

**Output**:
```
1
1
-1
0
2
2
14
0
-1
-1
```

### Example 2

**Input**:
```
1
703687441776640 327680
```

**Output**:
```
11
```

### Example 3

**Input**:
```
1
13776210264515 327680
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
