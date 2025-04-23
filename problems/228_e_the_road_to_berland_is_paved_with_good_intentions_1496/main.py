#!/usr/bin/env python3

s=list(map(int,input().split()))
n=s[0]
m=s[1]
roads=[]
for i in range(0,n+1):
    roads.append([])
for i in range(0,m):
    s=list(map(int,input().split()))
    roads[s[0]].append([s[1],s[2]])
    roads[s[1]].append([s[0],s[2]])

col=[-1]*(n+1)

##def dfs(v,c):
##    success=True
##    col[v]=c
##    for e in roads[v]:
##        if col[e[0]]==-1:
##            if e[1]:
##                success=success and dfs(e[0],c)
##            else:
##                success=success and dfs(e[0],1-c)
##        else:
##            if abs(col[e[0]]-c)!=1-e[1]:
##                return False
##    return success

bfs=True
for start in range(1,n+1):
    if col.count(-1)==1:
        break
    if col[start]==-1:
        Q=[start]
        col[start]=1
        while len(Q)>0 and bfs:
            curr=Q.pop(0)
            for e in roads[curr]:
                if col[e[0]]==-1:
                    Q.append(e[0])
                    if e[1]:
                        col[e[0]]=col[curr]
                    else:
                        col[e[0]]=1-col[curr]
                elif abs(col[e[0]]-col[curr])!=(1-e[1]):   #CONTRADICTION
                    bfs=False
                    Q=[]
                    break


if bfs:
    L=[j for j in range(1,n+1) if col[j]==1]
    print(len(L))
    ans=''
    for i in range(0,len(L)):
        ans+=str(L[i])+' '
    ans=ans[:len(ans)-1]
    print(ans)
else:
    print("Impossible")
