# 1172_C1. Nauuo and Pictures (easy version)

**ID:** 1172_c1_nauuo_and_pictures_easy_version_2723
**Difficulty:** 9

## Description

The only difference between easy and hard versions is constraints.

Nauuo is a girl who loves random picture websites.

One day she made a random picture website by herself which includes n pictures.

When Nauuo visits the website, she sees exactly one picture. The website does not display each picture with equal probability. The i-th picture has a non-negative weight w_i, and the probability of the i-th picture being displayed is \frac{w_i}{∑_{j=1}^nw_j}. That is to say, the probability of a picture to be displayed is proportional to its weight.

However, Nauuo discovered that some pictures she does not like were displayed too often. 

To solve this problem, she came up with a great idea: when she saw a picture she likes, she would add 1 to its weight; otherwise, she would subtract 1 from its weight.

Nauuo will visit the website m times. She wants to know the expected weight of each picture after all the m visits modulo 998244353. Can you help her?

The expected weight of the i-th picture can be denoted by \frac {q_i} {p_i} where \gcd(p_i,q_i)=1, you need to print an integer r_i satisfying 0≤ r_i<998244353 and r_i⋅ p_i≡ q_i\pmod{998244353}. It can be proved that such r_i exists and is unique.

Input

The first line contains two integers n and m (1≤ n≤ 50, 1≤ m≤ 50) — the number of pictures and the number of visits to the website.

The second line contains n integers a_1,a_2,…,a_n (a_i is either 0 or 1) — if a_i=0 , Nauuo does not like the i-th picture; otherwise Nauuo likes the i-th picture. It is guaranteed that there is at least one picture which Nauuo likes.

The third line contains n integers w_1,w_2,…,w_n (1≤ w_i≤50) — the initial weights of the pictures.

Output

The output contains n integers r_1,r_2,…,r_n — the expected weights modulo 998244353.

Examples

Input


2 1
0 1
2 1


Output


332748119
332748119


Input


1 2
1
1


Output


3


Input


3 3
0 1 1
4 3 5


Output


160955686
185138929
974061117

Note

In the first example, if the only visit shows the first picture with a probability of \frac 2 3, the final weights are (1,1); if the only visit shows the second picture with a probability of \frac1 3, the final weights are (2,2).

So, both expected weights are \frac2 3⋅ 1+\frac 1 3⋅ 2=\frac4 3 .

Because 332748119⋅ 3≡ 4\pmod{998244353}, you need to print 332748119 instead of \frac4 3 or 1.3333333333.

In the second example, there is only one picture which Nauuo likes, so every time Nauuo visits the website, w_1 will be increased by 1.

So, the expected weight is 1+2=3.

Nauuo is very naughty so she didn't give you any hint of the third example.

## Categories

- dp
- probabilities

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
1 2
1
1
```

**Output**:
```
3
```

### Example 2

**Input**:
```
2 1
0 1
2 1
```

**Output**:
```
332748119
332748119
```

### Example 3

**Input**:
```
3 3
0 1 1
4 3 5
```

**Output**:
```
160955686
185138929
974061117
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
