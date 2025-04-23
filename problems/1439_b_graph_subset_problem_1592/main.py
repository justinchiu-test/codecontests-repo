#!/usr/bin/env python3

import sys
input = sys.stdin.readline
testcase = int(input())
for _ in range(testcase):
  n,m,k = map(int,input().split())
  ab = [list(map(int,input().split())) for i in range(m)]
  if k == 1:
    print(2)
    print(1)
    continue
  if k*(k-1) > 2*m:
    print(-1)
    continue
  graph = [set() for i in range(n+1)]
  for a,b in ab:
    graph[a].add(b)
    graph[b].add(a)
  trash = set()
  stack = []
  for i in range(1,n+1):
    if len(graph[i]) < k-1:
      trash.add(i)
      stack.append(i)
  while stack:
    x = stack.pop()
    for y in graph[x]:
      if x in graph[y]:
        graph[y].remove(x)
        if len(graph[y]) < k-1:
          stack.append(y)
          trash.add(y)
    graph[x] = set()
  if n-len(trash) < k:
    print(-1)
    continue
  ansflg = 0
  ccand = []
  for i in range(1,n+1):
    if len(graph[i]) == k-1:
      ccand.append(i)
  while ccand:
    x = ccand.pop()
    if len(graph[x]) < k-1:
      trash.add(x)
      for y in graph[x]:
        if x in graph[y]:
          graph[y].remove(x)
          if len(graph[y]) == k-1:
            ccand.append(y)
      graph[x] = set()
      continue
    lsg = list(graph[x])
    for i in range(len(lsg)-1):
      for j in range(i+1,len(lsg)):
        if lsg[j] not in graph[lsg[i]]:
          trash.add(x)
          for y in graph[x]:
            if x in graph[y]:
              graph[y].remove(x)
              if len(graph[y]) == k-1:
                ccand.append(y)
          graph[x] = set()
          break
      else:
        continue
      break
    else:
      ansflg = 1
      break
  if ansflg:
    print(2)
    graph[x].add(x)
    print(*graph[x])
  elif n-len(trash) >= k+1:
    ansls = []
    for i in range(1,n+1):
      if i not in trash:
        ansls.append(i)
    print(1,len(ansls))
    print(*ansls)
  else:
    print(-1)
