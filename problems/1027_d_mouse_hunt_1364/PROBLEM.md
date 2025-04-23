# 1027_D. Mouse Hunt

**ID:** 1027_d_mouse_hunt_1364
**Difficulty:** 10

## Description

Medicine faculty of Berland State University has just finished their admission campaign. As usual, about 80\% of applicants are girls and majority of them are going to live in the university dormitory for the next 4 (hopefully) years.

The dormitory consists of n rooms and a single mouse! Girls decided to set mouse traps in some rooms to get rid of the horrible monster. Setting a trap in room number i costs c_i burles. Rooms are numbered from 1 to n.

Mouse doesn't sit in place all the time, it constantly runs. If it is in room i in second t then it will run to room a_i in second t + 1 without visiting any other rooms inbetween (i = a_i means that mouse won't leave room i). It's second 0 in the start. If the mouse is in some room with a mouse trap in it, then the mouse get caught into this trap.

That would have been so easy if the girls actually knew where the mouse at. Unfortunately, that's not the case, mouse can be in any room from 1 to n at second 0.

What it the minimal total amount of burles girls can spend to set the traps in order to guarantee that the mouse will eventually be caught no matter the room it started from?

Input

The first line contains as single integers n (1 ≤ n ≤ 2 ⋅ 10^5) — the number of rooms in the dormitory.

The second line contains n integers c_1, c_2, ..., c_n (1 ≤ c_i ≤ 10^4) — c_i is the cost of setting the trap in room number i.

The third line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n) — a_i is the room the mouse will run to the next second after being in room i.

Output

Print a single integer — the minimal total amount of burles girls can spend to set the traps in order to guarantee that the mouse will eventually be caught no matter the room it started from.

Examples

Input

5
1 2 3 2 10
1 3 4 3 3


Output

3


Input

4
1 10 2 10
2 4 2 2


Output

10


Input

7
1 1 1 1 1 1 1
2 2 2 3 6 7 6


Output

2

Note

In the first example it is enough to set mouse trap in rooms 1 and 4. If mouse starts in room 1 then it gets caught immideately. If mouse starts in any other room then it eventually comes to room 4.

In the second example it is enough to set mouse trap in room 2. If mouse starts in room 2 then it gets caught immideately. If mouse starts in any other room then it runs to room 2 in second 1.

Here are the paths of the mouse from different starts from the third example:

  * 1 → 2 → 2 → ...;
  * 2 → 2 → ...;
  * 3 → 2 → 2 → ...;
  * 4 → 3 → 2 → 2 → ...;
  * 5 → 6 → 7 → 6 → ...;
  * 6 → 7 → 6 → ...;
  * 7 → 6 → 7 → ...;



So it's enough to set traps in rooms 2 and 6.

## Categories

- dfs and similar
- graphs

## Source

Codeforces

## Examples

### Example 1

**Input**:
```
4
1 10 2 10
2 4 2 2
```

**Output**:
```
10
```

### Example 2

**Input**:
```
5
1 2 3 2 10
1 3 4 3 3
```

**Output**:
```
3
```

### Example 3

**Input**:
```
7
1 1 1 1 1 1 1
2 2 2 3 6 7 6
```

**Output**:
```
2
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
