#!/usr/bin/env python3

import sys
from collections import defaultdict,deque
def getcost(ind,col1,col2,col3,count):
    #print(ind,'ind',count,'count')
    if count==1:
        #print(col1[ind-1],'collooorr')
        return col1[ind-1]
    if count==2:
        #print(col2[ind-1],'colllllooorrr')
        return col2[ind-1]
    #print(col3[ind-1],'cpppplll')
    return col3[ind-1]
n=int(sys.stdin.readline())
col1=list(map(int,sys.stdin.readline().split()))
col2=list(map(int,sys.stdin.readline().split()))
col3=list(map(int,sys.stdin.readline().split()))
tree=defaultdict(list)
for i in range(n-1):
    u,v=map(int,sys.stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)
z=True
leaf=[]
for i in tree:
    if len(tree[i])>2:
        print(-1)
        z=False
        break
    if len(tree[i])==1:
        leaf.append(i)
if z:
    dp=defaultdict(list)
    for i in range(1,n+1):
        dp[i]=[float('inf'),float('inf'),float('inf')]
    #print(leaf,'leaf')
    #for t in range(len(leaf)):
    l=[[1,2,3],[1,3,2],[2,3,1],[2,1,3],[3,1,2],[3,2,1]]
    m=[0,0,0,0,0,0]
    color=[[-1 for _ in range(n)] for x in range(6)]
    for j in range(6):
        count=0
        cost=0
        start=leaf[0]
        vis=defaultdict(int)
        vis[start]=1
        q=deque()
        q.append(start)
        color[j][start-1]=l[j][count%3]
        cost+=getcost(start,col1,col2,col3,l[j][count%3])
        #print(l[j][count%3],'check')
        count+=1
        while q:
            #print(q,'q')
            a=q.popleft()
            for i in tree[a]:
                #print(i,'i')
                if vis[i]==0:
                    #print(l[j][count%3],'check')
                    q.append(i)
                    #print(i,'i')
                    vis[i]=1
                    color[j][i-1]=l[j][count%3]
                    cost+=getcost(i,col1,col2,col3,l[j][count%3])
                    count+=1
        m[j]=cost
        #print(cost,'cost')
        #print('----')
    #print(m,'m')
    ind=-1
    ans=min(m)
    print(ans)
    #print(color,'color')
    for i in range(6):
        if m[i]==ans:
            break
    '''color=[-1 for _ in range(n)]
    count=0
    vis=defaultdict(int)
    q=deque()
    q.append(leaf[0])
    vis[leaf[0]]=1
    color[leaf[0]-1]=l[i][count%3]
    count+=1
    while q:
        a=q.popleft()
        for j in tree[a]:
            if vis[j]==0:
                q.append(j)
                vis[j]=1
                color[j-1]=l[i][count%3]
                count+=1
    print(ans)'''
    print(*color[i])
