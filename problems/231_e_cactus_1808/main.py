#!/usr/bin/env python3

from collections import defaultdict
import os
import sys
from io import BytesIO, IOBase
from types import GeneratorType
from collections import defaultdict
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
sys.setrecursionlimit(3*10**4)



def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc




@bootstrap
def dfs1(cur,prev,v):
    depth[cur] = depth[prev] + 1
    parent[cur][0] = prev
    blacks[cur]=v
    if val[cur]:
        blacks[cur]+=1
    for i in tree[cur]:
        if (i != prev):
            yield dfs1(i, cur,blacks[cur])

    yield

def precomputeSparseMatrix(n):
    for i in range(1,level):
        for node in range(1,n+1):
            if (parent[node][i-1] != -1):
                parent[node][i] =parent[parent[node][i-1]][i-1]


def lca(u,v):
    if (depth[v] < depth[u]):
        u,v=v,u

    diff = depth[v] - depth[u]


    for i in range(level):
        if ((diff >> i) & 1):
            v = parent[v][i]


    if (u == v):
        return u

    i=level-1
    while(i>=0):

        if (parent[u][i] != parent[v][i]):
            u = parent[u][i]
            v = parent[v][i]

        i+=-1

    return parent[u][0]

@bootstrap
def dfs(u,p):

    global curr

    for j in adj[u]:
        if j!=p:
            if id[j]==0:
                id[j]=id[u]+1
                yield dfs(j,u)

            elif id[u]>id[j]:

                up[u]=curr
                down[j]=curr
                curr+=1
    yield

@bootstrap
def dfs2(u,p):

    vis[u]=1
    for j in adj[u]:
        if not vis[j]:
            yield dfs2(j,u)

    if up[u]:
        id[u]=up[u]

    else:
        id[u]=u
        for j in adj[u]:
            if j!=p:
                if id[j]!=j and down[j]==0:

                    id[u]=id[j]
    yield













n,m=map(int,input().split())
adj=[[] for i in range(n+1)]
edges=[]
for j in range(m):
    u,v=map(int,input().split())
    edges.append([u,v])
    adj[u].append(v)
    adj[v].append(u)

up=defaultdict(lambda:0)
down=defaultdict(lambda:0)

curr=n+1
id=[]
vis=[]
val=[]
tree=[]
depth=[]
for j in range(n+1):
    id.append(0)
    vis.append(0)
    val.append(0)
    tree.append([])
    depth.append(0)


id[1]=1
dfs(1,0)
dfs2(1,0)
res=sorted(list(set(id[1:])))
up=defaultdict(lambda:0)
l=len(res)
for j in range(l):
    up[res[j]]=j+1

d=defaultdict(lambda:0)
for j in range(1,n+1):
    id[j]=up[id[j]]
    d[id[j]]+=1
    if d[id[j]]>1:
        val[id[j]]=1




level=17

parent=[[0 for i in range(level)] for j in range(l+1)]
blacks=[0]*(l+1)
d=defaultdict(lambda:0)
for j in edges:
    u,v=j[0],j[1]
    p,q=id[u],id[v]
    if not d[p,q] and p!=q:
        tree[p].append(q)
        tree[q].append(p)

    d[p,q]=1
    d[q,p]=1






dfs1(1,0,0)

precomputeSparseMatrix(l)

k=int(input())
mod=10**9+7
value=[1]
for j in range(1,l+1):
    value.append((2*value[-1])%(mod))
for j in range(k):
    a,b=map(int,input().split())
    u1,v1=id[a],id[b]
    lc=lca(u1,v1)

    res=value[blacks[u1]+blacks[v1]-2*blacks[lc]]

    if val[lc]:
        res*=2

    print(res%mod)
