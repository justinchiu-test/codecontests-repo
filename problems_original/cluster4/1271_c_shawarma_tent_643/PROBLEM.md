# 1271_C. Shawarma Tent

**ID:** 1271_c_shawarma_tent_643
**Difficulty:** 9

## Description

The map of the capital of Berland can be viewed on the infinite coordinate plane. Each point with integer coordinates contains a building, and there are streets connecting every building to four neighbouring buildings. All streets are parallel to the coordinate axes.

The main school of the capital is located in (s_x, s_y). There are n students attending this school, the i-th of them lives in the house located in (x_i, y_i). It is possible that some students live in the same house, but no student lives in (s_x, s_y).

After classes end, each student walks from the school to his house along one of the shortest paths. So the distance the i-th student goes from the school to his house is |s_x - x_i| + |s_y - y_i|.

The Provision Department of Berland has decided to open a shawarma tent somewhere in the capital (at some point with integer coordinates). It is considered that the i-th student will buy a shawarma if at least one of the shortest paths from the school to the i-th student's house goes through the point where the shawarma tent is located. It is forbidden to place the shawarma tent at the point where the school is located, but the coordinates of the shawarma tent may coincide with the coordinates of the house of some student (or even multiple students).

You want to find the maximum possible number of students buying shawarma and the optimal location for the tent itself.

Input

The first line contains three integers n, s_x, s_y (1 ≤ n ≤ 200 000, 0 ≤ s_x, s_y ≤ 10^{9}) — the number of students and the coordinates of the school, respectively.

Then n lines follow. The i-th of them contains two integers x_i, y_i (0 ≤ x_i, y_i ≤ 10^{9}) — the location of the house where the i-th student lives. Some locations of houses may coincide, but no student lives in the same location where the school is situated.

Output

The output should consist of two lines. The first of them should contain one integer c — the maximum number of students that will buy shawarmas at the tent. 

The second line should contain two integers p_x and p_y — the coordinates where the tent should be located. If there are multiple answers, print any of them. Note that each of p_x and p_y should be not less than 0 and not greater than 10^{9}.

Examples

Input


4 3 2
1 3
4 2
5 1
4 1


Output


3
4 2


Input


3 100 100
0 0
0 0
100 200


Output


2
99 100


Input


7 10 12
5 6
20 23
15 4
16 5
4 54
12 1
4 15


Output


4
10 11

Note

In the first example, If we build the shawarma tent in (4, 2), then the students living in (4, 2), (4, 1) and (5, 1) will visit it.

In the second example, it is possible to build the shawarma tent in (1, 1), then both students living in (0, 0) will visit it.

## Categories

- brute force
- geometry
- greedy
- implementation

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
7 10 12
5 6
20 23
15 4
16 5
4 54
12 1
4 15
```

**Output**:
```
4
11 12
```

### Example 2

**Input**:
```
4 3 2
1 3
4 2
5 1
4 1
```

**Output**:
```
3
4 2
```

### Example 3

**Input**:
```
3 100 100
0 0
0 0
100 200
```

**Output**:
```
2
99 100
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
