# 518_D. Ilya and Escalator

**ID:** 518_d_ilya_and_escalator_1612
**Difficulty:** 10

## Description

Ilya got tired of sports programming, left university and got a job in the subway. He was given the task to determine the escalator load factor. 

Let's assume that n people stand in the queue for the escalator. At each second one of the two following possibilities takes place: either the first person in the queue enters the escalator with probability p, or the first person in the queue doesn't move with probability (1 - p), paralyzed by his fear of escalators and making the whole queue wait behind him.

Formally speaking, the i-th person in the queue cannot enter the escalator until people with indices from 1 to i - 1 inclusive enter it. In one second only one person can enter the escalator. The escalator is infinite, so if a person enters it, he never leaves it, that is he will be standing on the escalator at any following second. Ilya needs to count the expected value of the number of people standing on the escalator after t seconds. 

Your task is to help him solve this complicated task.

Input

The first line of the input contains three numbers n, p, t (1 ≤ n, t ≤ 2000, 0 ≤ p ≤ 1). Numbers n and t are integers, number p is real, given with exactly two digits after the decimal point.

Output

Print a single real number — the expected number of people who will be standing on the escalator after t seconds. The absolute or relative error mustn't exceed 10 - 6.

Examples

Input

1 0.50 1


Output

0.5


Input

1 0.50 4


Output

0.9375


Input

4 0.20 2


Output

0.4

## Categories

- combinatorics
- dp
- math
- probabilities

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
1 0.50 1
```

**Output**:
```
0.500000000000
```

### Example 2

**Input**:
```
4 0.20 2
```

**Output**:
```
0.400000000000
```

### Example 3

**Input**:
```
1 0.50 4
```

**Output**:
```
0.937500000000
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
