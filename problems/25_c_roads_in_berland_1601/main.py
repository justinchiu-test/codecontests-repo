#!/usr/bin/env python3

n = int(input())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))
q = int(input())
ans= []
for _ in range(q):
    x, y, w = map(int, input().split())
    x-=1
    y-=1
    mat[x][y] = mat[y][x] = min(mat[x][y], w)
    sum1 = 0
    for i in range(n):
        for j in range(n):
            a = mat[i][y]+mat[x][y]+mat[x][j]
            b = mat[i][x]+mat[x][y]+mat[y][j]
            c = mat[i][j]
            mat[i][j] = min(a, b, c)
        sum1 += sum(mat[i])
    ans.append(sum1//2)
print(*ans)
