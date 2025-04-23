# 453_C. Little Pony and Summer Sun Celebration

**ID:** 453_c_little_pony_and_summer_sun_celebration_2233
**Difficulty:** 9

## Description

Twilight Sparkle learnt that the evil Nightmare Moon would return during the upcoming Summer Sun Celebration after one thousand years of imprisonment on the moon. She tried to warn her mentor Princess Celestia, but the princess ignored her and sent her to Ponyville to check on the preparations for the celebration.

<image>

Twilight Sparkle wanted to track the path of Nightmare Moon. Unfortunately, she didn't know the exact path. What she knew is the parity of the number of times that each place Nightmare Moon visited. Can you help Twilight Sparkle to restore any path that is consistent with this information?

Ponyville can be represented as an undirected graph (vertices are places, edges are roads between places) without self-loops and multi-edges. The path can start and end at any place (also it can be empty). Each place can be visited multiple times. The path must not visit more than 4n places.

Input

The first line contains two integers n and m (2 ≤ n ≤ 105; 0 ≤ m ≤ 105) — the number of places and the number of roads in Ponyville. Each of the following m lines contains two integers ui, vi (1 ≤ ui, vi ≤ n; ui ≠ vi), these integers describe a road between places ui and vi.

The next line contains n integers: x1, x2, ..., xn (0 ≤ xi ≤ 1) — the parity of the number of times that each place must be visited. If xi = 0, then the i-th place must be visited even number of times, else it must be visited odd number of times.

Output

Output the number of visited places k in the first line (0 ≤ k ≤ 4n). Then output k integers — the numbers of places in the order of path. If xi = 0, then the i-th place must appear in the path even number of times, else i-th place must appear in the path odd number of times. Note, that given road system has no self-loops, therefore any two neighbouring places in the path must be distinct.

If there is no required path, output -1. If there multiple possible paths, you can output any of them.

Examples

Input

3 2
1 2
2 3
1 1 1


Output

3
1 2 3


Input

5 7
1 2
1 3
1 4
1 5
3 4
3 5
4 5
0 1 0 1 0


Output

10
2 1 3 4 5 4 5 4 3 1

Input

2 0
0 0


Output

0

## Categories

- constructive algorithms
- dfs and similar
- graphs

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
2 0
0 0
```

**Output**:
```
0
```

### Example 2

**Input**:
```
3 2
1 2
2 3
1 1 1
```

**Output**:
```
7
1 2 3 2 1 2 1
```

### Example 3

**Input**:
```
5 7
1 2
1 3
1 4
1 5
3 4
3 5
4 5
0 1 0 1 0
```

**Output**:
```
10
2 1 3 4 5 4 5 4 3 1
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
