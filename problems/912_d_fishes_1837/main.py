#!/usr/bin/env python3

n, m, r, k = map(int, input().split())

def count(y, x):
    minx = max(0, x-(r-1))
    maxx = min(m-1-(r-1), x)
    miny = max(0, y-(r-1))
    maxy = min(n-1-(r-1), y)
    res = (maxy-miny+1)*(maxx-minx+1)
    return res

#X = [[0]*m for i in range(n)]
#for i in range(n):
    #for j in range(m):
        #X[i][j] = count(i, j)
        #print(i, j, count(i, j))

#for i in range(n):
    #print(*X[i])

sy, sx = n//2, m//2
c = count(sy, sx)
cnt = 0
import heapq
q = [(-c, sy, sx)]
heapq.heapify(q)
visit = set()
visit.add((sy, sx))
E = 0
while q:
    c, y, x = heapq.heappop(q)
    c = -c
    E += c
    cnt += 1
    if cnt == k:
        break
    for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
        ny, nx = y+dy, x+dx
        if 0 <= ny < n and 0 <= nx < m:
            if (ny, nx) in visit:
                continue
            c = count(ny, nx)
            heapq.heappush(q, (-c, ny, nx))
            visit.add((ny, nx))

ans = E/((n-r+1)*(m-r+1))
print(ans)
