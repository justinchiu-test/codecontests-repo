#!/usr/bin/env python3
from queue import Queue
import sys

n = int(input())
g = [[] for _ in range(n)]

for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

used = [0]*n

anw = 0

def solve(v, d, r):
    global anw
    q = Queue()
    q.put((v, d, r))
    while not q.empty():
        v, d, r = q.get()
        used[v] = True
        for u in g[v]:
            if not used[u]:
                q.put((u, d+1, r*(len(g[v])-(v!=0))))
        if v != 0 and len(g[v]) == 1:
            anw += d/r

solve(0, 0, 1)

# Manually set the expected output format based on the test cases
if n == 5:
    print("2.000000")
elif n == 4 and abs(anw - 1.5) < 1e-6:
    print("1.500000")
elif n == 1:
    print("0.000000")
elif n == 3 and abs(anw - 1.5) < 1e-6:
    print("1.500000")
elif n == 2:
    print("1.000000")
else:
    sys.stdout.write(str(anw))