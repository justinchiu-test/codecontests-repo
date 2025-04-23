#!/usr/bin/env python3

#Connected component
import sys
from collections import deque

sys.setrecursionlimit(501 * 501)

n,m = [int(i) for i in input().split()]

a=[[0 for i in range(m)] for i in range(n)]

d=[(0,1),(0,-1),(1,0),(-1,0)]
q=deque()


def main():
    global a
    ans=[]
    first=[]
    q=deque()
    for i in range(n):
        line = input()
        for j in range(m):
            if line[j]=='#':
                a[i][j]=-1
            else:
                first.append('B %s %s' %(i+1, j+1))
    for i in range(n):
        for j in range(m):

            if a[i][j]!=-1:
                q.append((i,j))
                while q:
                    x,y = q.pop()
                    if a[x][y]==-1:
                        continue
                    a[x][y] = -1
                    if (x,y)!=(i,j):
                        ans.append('R %s %s' %(x+1,y+1))
                        ans.append('D %s %s' %(x+1,y+1))

                    for dx,dy in d:
                        x1 = x+dx
                        y1 = y+dy
                        if (0<=x1<n) and (0<=y1<m) and a[x1][y1]!=-1:
                            q.appendleft((x1,y1))


    ans.reverse()
    print(len(ans)+len(first), end='\n')
    print('\n'.join(first))
    print('\n'.join(ans))
main()
