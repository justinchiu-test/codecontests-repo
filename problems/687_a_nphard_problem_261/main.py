#!/usr/bin/env python3

M=lambda:map(int,input().split())
n,m=M()
graph=[set() for i in range(n)]
for _ in range(m):
    a,b=M()
    graph[a-1].add(b-1)
    graph[b-1].add(a-1)
visited=[-1 for i in range(n)]
stack=[]
for i in range(n):
    if visited[i]==-1 and len(graph[i])>0:
        visited[i]=True
        stack+=[i]
        while stack:
            x=stack.pop()
            for j in graph[x]:
                if visited[j]==visited[x]:
                    print(-1)
                    exit(0)
                if visited[j]==-1:
                    visited[j]=not visited[x]
                    stack+=[j]
A=[]
B=[]
for i in range(len(visited)):
    if visited[i]==True:
        A.append(i+1)
    elif visited[i]==False:
        B.append(i+1)
print(len(A))
print(*A)
print(len(B))
print(*B)
