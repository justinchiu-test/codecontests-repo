# 746_G. New Roads

**ID:** 746_g_new_roads_1518
**Difficulty:** 13

## Description

There are n cities in Berland, each of them has a unique id — an integer from 1 to n, the capital is the one with id 1. Now there is a serious problem in Berland with roads — there are no roads.

That is why there was a decision to build n - 1 roads so that there will be exactly one simple path between each pair of cities.

In the construction plan t integers a1, a2, ..., at were stated, where t equals to the distance from the capital to the most distant city, concerning new roads. ai equals the number of cities which should be at the distance i from the capital. The distance between two cities is the number of roads one has to pass on the way from one city to another.

Also, it was decided that among all the cities except the capital there should be exactly k cities with exactly one road going from each of them. Such cities are dead-ends and can't be economically attractive. In calculation of these cities the capital is not taken into consideration regardless of the number of roads from it.

Your task is to offer a plan of road's construction which satisfies all the described conditions or to inform that it is impossible.

Input

The first line contains three positive numbers n, t and k (2 ≤ n ≤ 2·105, 1 ≤ t, k < n) — the distance to the most distant city from the capital and the number of cities which should be dead-ends (the capital in this number is not taken into consideration).

The second line contains a sequence of t integers a1, a2, ..., at (1 ≤ ai < n), the i-th number is the number of cities which should be at the distance i from the capital. It is guaranteed that the sum of all the values ai equals n - 1.

Output

If it is impossible to built roads which satisfy all conditions, print -1.

Otherwise, in the first line print one integer n — the number of cities in Berland. In the each of the next n - 1 line print two integers — the ids of cities that are connected by a road. Each road should be printed exactly once. You can print the roads and the cities connected by a road in any order.

If there are multiple answers, print any of them. Remember that the capital has id 1.

Examples

Input

7 3 3
2 3 1


Output

7
1 3
2 1
2 6
2 4
7 4
3 5


Input

14 5 6
4 4 2 2 1


Output

14
3 1
1 4
11 6
1 2
10 13
6 10
10 12
14 12
8 4
5 1
3 7
2 6
5 9


Input

3 1 1
2


Output

-1

## Categories

- constructive algorithms
- graphs
- trees

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
7 3 3
2 3 1
```

**Output**:
```
7
1 2
1 3
2 4
3 5
2 6
4 7
```

### Example 2

**Input**:
```
3 1 1
2
```

**Output**:
```
-1
```

### Example 3

**Input**:
```
14 5 6
4 4 2 2 1
```

**Output**:
```
14
1 2
1 3
1 4
1 5
2 6
3 7
4 8
5 9
6 10
6 11
10 12
10 13
12 14
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
