# 1321_D. Navigation System

**ID:** 1321_d_navigation_system_8975
**Difficulty:** 10

## Description

The map of Bertown can be represented as a set of n intersections, numbered from 1 to n and connected by m one-way roads. It is possible to move along the roads from any intersection to any other intersection. The length of some path from one intersection to another is the number of roads that one has to traverse along the path. The shortest path from one intersection v to another intersection u is the path that starts in v, ends in u and has the minimum length among all such paths.

Polycarp lives near the intersection s and works in a building near the intersection t. Every day he gets from s to t by car. Today he has chosen the following path to his workplace: p_1, p_2, ..., p_k, where p_1 = s, p_k = t, and all other elements of this sequence are the intermediate intersections, listed in the order Polycarp arrived at them. Polycarp never arrived at the same intersection twice, so all elements of this sequence are pairwise distinct. Note that you know Polycarp's path beforehand (it is fixed), and it is not necessarily one of the shortest paths from s to t.

Polycarp's car has a complex navigation system installed in it. Let's describe how it works. When Polycarp starts his journey at the intersection s, the system chooses some shortest path from s to t and shows it to Polycarp. Let's denote the next intersection in the chosen path as v. If Polycarp chooses to drive along the road from s to v, then the navigator shows him the same shortest path (obviously, starting from v as soon as he arrives at this intersection). However, if Polycarp chooses to drive to another intersection w instead, the navigator rebuilds the path: as soon as Polycarp arrives at w, the navigation system chooses some shortest path from w to t and shows it to Polycarp. The same process continues until Polycarp arrives at t: if Polycarp moves along the road recommended by the system, it maintains the shortest path it has already built; but if Polycarp chooses some other path, the system rebuilds the path by the same rules.

Here is an example. Suppose the map of Bertown looks as follows, and Polycarp drives along the path [1, 2, 3, 4] (s = 1, t = 4): 

Check the picture by the link [http://tk.codeforces.com/a.png](//tk.codeforces.com/a.png)

  1. When Polycarp starts at 1, the system chooses some shortest path from 1 to 4. There is only one such path, it is [1, 5, 4]; 
  2. Polycarp chooses to drive to 2, which is not along the path chosen by the system. When Polycarp arrives at 2, the navigator rebuilds the path by choosing some shortest path from 2 to 4, for example, [2, 6, 4] (note that it could choose [2, 3, 4]); 
  3. Polycarp chooses to drive to 3, which is not along the path chosen by the system. When Polycarp arrives at 3, the navigator rebuilds the path by choosing the only shortest path from 3 to 4, which is [3, 4]; 
  4. Polycarp arrives at 4 along the road chosen by the navigator, so the system does not have to rebuild anything. 



Overall, we get 2 rebuilds in this scenario. Note that if the system chose [2, 3, 4] instead of [2, 6, 4] during the second step, there would be only 1 rebuild (since Polycarp goes along the path, so the system maintains the path [3, 4] during the third step).

The example shows us that the number of rebuilds can differ even if the map of Bertown and the path chosen by Polycarp stays the same. Given this information (the map and Polycarp's path), can you determine the minimum and the maximum number of rebuilds that could have happened during the journey?

Input

The first line contains two integers n and m (2 ≤ n ≤ m ≤ 2 ⋅ 10^5) — the number of intersections and one-way roads in Bertown, respectively.

Then m lines follow, each describing a road. Each line contains two integers u and v (1 ≤ u, v ≤ n, u ≠ v) denoting a road from intersection u to intersection v. All roads in Bertown are pairwise distinct, which means that each ordered pair (u, v) appears at most once in these m lines (but if there is a road (u, v), the road (v, u) can also appear).

The following line contains one integer k (2 ≤ k ≤ n) — the number of intersections in Polycarp's path from home to his workplace.

The last line contains k integers p_1, p_2, ..., p_k (1 ≤ p_i ≤ n, all these integers are pairwise distinct) — the intersections along Polycarp's path in the order he arrived at them. p_1 is the intersection where Polycarp lives (s = p_1), and p_k is the intersection where Polycarp's workplace is situated (t = p_k). It is guaranteed that for every i ∈ [1, k - 1] the road from p_i to p_{i + 1} exists, so the path goes along the roads of Bertown. 

Output

Print two integers: the minimum and the maximum number of rebuilds that could have happened during the journey.

Examples

Input


6 9
1 5
5 4
1 2
2 3
3 4
4 1
2 6
6 4
4 2
4
1 2 3 4


Output


1 2


Input


7 7
1 2
2 3
3 4
4 5
5 6
6 7
7 1
7
1 2 3 4 5 6 7


Output


0 0


Input


8 13
8 7
8 6
7 5
7 4
6 5
6 4
5 3
5 2
4 3
4 2
3 1
2 1
1 8
5
8 7 5 2 1


Output


0 3

## Categories

- dfs and similar
- graphs
- shortest paths

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
8 13
8 7
8 6
7 5
7 4
6 5
6 4
5 3
5 2
4 3
4 2
3 1
2 1
1 8
5
8 7 5 2 1
```

**Output**:
```
0 3
```

### Example 2

**Input**:
```
6 9
1 5
5 4
1 2
2 3
3 4
4 1
2 6
6 4
4 2
4
1 2 3 4
```

**Output**:
```
1 2
```

### Example 3

**Input**:
```
7 7
1 2
2 3
3 4
4 5
5 6
6 7
7 1
7
1 2 3 4 5 6 7
```

**Output**:
```
0 0
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
