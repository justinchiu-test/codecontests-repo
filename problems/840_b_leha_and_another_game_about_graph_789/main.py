#!/usr/bin/env python3

import os,io
input=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
import sys
import heapq
INF=10**9
def Dijkstra(graph, start,m):
  dist=[INF]*len(graph)
  parent=[INF]*len(graph)
  queue=[(0, start)]
  while queue:
    path_len, v=heapq.heappop(queue)
    if dist[v]==INF:
      dist[v]=path_len
      for w in graph[v]:
        if dist[w[0]]==INF:
          parent[w[0]]=[v,w[1]]
          heapq.heappush(queue, (dist[v]+1, w[0]))
  return (dist,parent)

n,m=map(int,input().split())
d=list(map(int,input().split()))
graph=[]
for i in range(n):
  graph.append([])
for i in range(m):
  u,v=map(int,input().split())
  graph[u-1].append([v-1,i])
  graph[v-1].append([u-1,i])
count=0
flag=0
for i in range(n):
  if d[i]==1:
    count+=1
  elif d[i]==-1:
    flag=1
if count%2==1 and flag==0:
  print(-1)
  sys.exit()
if count%2==1:
  for i in range(n):
    if d[i]==-1 and flag==1:
      d[i]=1
      flag=0
    elif d[i]==-1:
      d[i]=0
else:
  for i in range(n):
    if d[i]==-1:
      d[i]=0
dist,parent=Dijkstra(graph,0,m)
actualused=[0]*m
children=[0]*n
actualchildren=[0]*n
for i in range(1,n):
  children[parent[i][0]]+=1
stack=[]
for i in range(n):
  if children[i]==actualchildren[i]:
    stack.append(i)
while stack:
  curr=stack.pop()
  if curr==0:
    break
  p=parent[curr]
  k=p[0]
  if d[curr]==1:
    actualused[p[1]]=1
    d[k]=1-d[k]
  actualchildren[k]+=1
  if actualchildren[k]==children[k]:
    stack.append(k)
ans=[]
for i in range(m):
  if actualused[i]:
    ans.append(str(i+1))
print(len(ans))
print(' '.join(ans))
