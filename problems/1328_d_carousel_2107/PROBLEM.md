# 1328_D. Carousel

**ID:** 1328_d_carousel_2107
**Difficulty:** 10

## Description

The round carousel consists of n figures of animals. Figures are numbered from 1 to n in order of the carousel moving. Thus, after the n-th figure the figure with the number 1 follows. Each figure has its own type — the type of the animal corresponding to this figure (the horse, the tiger and so on). The type of animal of the i-th figure equals t_i.

<image> The example of the carousel for n=9 and t=[5, 5, 1, 15, 1, 5, 5, 1, 1].

You want to color each figure in one of the colors. You think that it's boring if the carousel contains two different figures (with the distinct types of animals) going one right after another and colored in the same color.

Your task is to color the figures in such a way that the number of distinct colors used is the minimum possible and there are no figures of the different types going one right after another and colored in the same color. If you use exactly k distinct colors, then the colors of figures should be denoted with integers from 1 to k.

Input

The input contains one or more test cases.

The first line contains one integer q (1 ≤ q ≤ 10^4) — the number of test cases in the test. Then q test cases follow. One test case is given on two lines.

The first line of the test case contains one integer n (3 ≤ n ≤ 2 ⋅ 10^5) — the number of figures in the carousel. Figures are numbered from 1 to n in order of carousel moving. Assume that after the n-th figure the figure 1 goes.

The second line of the test case contains n integers t_1, t_2, ..., t_n (1 ≤ t_i ≤ 2 ⋅ 10^5), where t_i is the type of the animal of the i-th figure.

The sum of n over all test cases does not exceed 2⋅10^5.

Output

Print q answers, for each test case print two lines.

In the first line print one integer k — the minimum possible number of distinct colors of figures.

In the second line print n integers c_1, c_2, ..., c_n (1 ≤ c_i ≤ k), where c_i is the color of the i-th figure. If there are several answers, you can print any.

Example

Input


4
5
1 2 1 2 2
6
1 2 2 1 2 2
5
1 2 1 2 3
3
10 10 10


Output


2
1 2 1 2 2
2
2 1 2 1 2 1
3
2 3 2 3 1
1
1 1 1

## Categories

- constructive algorithms
- dp
- graphs
- greedy
- math

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
4
5
1 2 1 2 2
6
1 2 2 1 2 2
5
1 2 1 2 3
3
10 10 10
```

**Output**:
```
2
1 2 1 2 2
2
1 2 1 2 1 2
3
1 2 1 2 3
1
1 1 1
```

### Example 2

**Input**:
```
4
5
1 2 1 2 2
6
1 2 2 1 2 2
5
1 2 1 2 3
3
10 10 10
```

**Output**:
```
2
1 2 1 2 2
2
1 2 1 2 1 2
3
1 2 1 2 3
1
1 1 1
```

### Example 3

**Input**:
```
4
5
1 2 1 2 2
6
1 2 2 1 2 2
5
1 2 1 2 3
3
14 10 10
```

**Output**:
```
2
1 2 1 2 2
2
1 2 1 2 1 2
3
1 2 1 2 3
2
1 2 2
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
