#!/usr/bin/env python3

class UnionFind:
    def __init__(self, n):
        self.par = [-1]*n
        self.rank = [0]*n

    def Find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.Find(self.par[x])
            return self.par[x]

    def Unite(self, x, y):
        x = self.Find(x)
        y = self.Find(y)

        if x != y:
            if self.rank[x] < self.rank[y]:
                self.par[y] += self.par[x]
                self.par[x] = y
            else:
                self.par[x] += self.par[y]
                self.par[y] = x
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1

    def Same(self, x, y):
        return self.Find(x) == self.Find(y)

    def Size(self, x):
        return -self.par[self.Find(x)]

import sys
import io, os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

n, m, q = map(int, input().split())
uf = UnionFind(n+m)
for i in range(q):
    r, c = map(int, input().split())
    r, c = r-1, c-1
    uf.Unite(r, c+n)

S = set()
for i in range(n+m):
    S.add(uf.Find(i))
print(len(S)-1)
