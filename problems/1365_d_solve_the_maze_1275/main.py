#!/usr/bin/env python3

# ------------------- fast io --------------------
import os
import sys
from io import BytesIO, IOBase

BUFSIZE = 8192

class FastIO(IOBase):
    newlines = 0
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# ------------------- fast io --------------------

import collections
def block(s,b):
    global m
    global n
    global maze
    broke=False
    if b>0:
        if maze[s][b-1]==".":
            maze[s][b-1]="#"
        elif maze[s][b-1]=="G":
            broke=True
    if b<m-1:
        if maze[s][b+1]==".":
            maze[s][b+1]="#"
        elif maze[s][b+1]=="G":
            broke=True
    if s>0:
        if maze[s-1][b]==".":
            maze[s-1][b]="#"
        elif maze[s-1][b]=="G":
            broke=True
    if s<n-1:
        if maze[s+1][b]==".":
            maze[s+1][b]="#"
        elif maze[s+1][b]=="G":
            broke=True
    return broke
testcases=int(input())

for j in range(testcases):
    n,m=map(int,input().split())
    #n is rows,m is columns
    maze=[]
    for s in range(n):
        row=[k for k in input()]
        maze.append(row)
    #block all the bad guys in, surround them all in with walls
    b1=False
    dict1={}
    for s in range(n):
        for b in range(m):
            dict1[(s,b)]=[]
    for s in range(n):
        for b in range(m):
            if maze[s][b]=="B":
                broke=block(s,b)
                if broke==True:
                    b1=True
                    break
    good=0
    for s in range(n):
        for b in range(m):
            if maze[s][b]!="#":
                if maze[s][b]=="G":
                    good+=1
                if b>0:
                    if maze[s][b-1]!="#":
                        dict1[(s,b)].append((s,b-1))
                if b<m-1:
                    if maze[s][b+1]!="#":
                        dict1[(s,b)].append((s,b+1))
                if s>0:
                    if maze[s-1][b]!="#":
                        dict1[(s,b)].append((s-1,b))
                if s<n-1:
                    if maze[s+1][b]!="#":
                        dict1[(s,b)].append((s+1,b))
    visited=set([])
    for s in dict1.keys():
        if not(s in visited) and maze[s[0]][s[1]]=="G":
            queue=collections.deque([])
            vis=set([s])
            for b in dict1[s]:
                queue.append(b)
                vis.add(b)
                visited.add(b)
            while len(queue)>0:
                v0=queue.popleft()
                for b in dict1[v0]:
                    if not(b in vis):
                        vis.add(b)
                        queue.append(b)
                        if b in visited:
                            vis.add((n-1,m-1))
                            break
                        visited.add(b)
            if (n-1,m-1) in vis:
                continue
            else:
                b1=True
                break
    if good>=1 and maze[n-1][m-1]=="#":
        b1=True
    if b1==True:
        print("No")
    else:
        print("Yes")
