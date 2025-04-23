#!/usr/bin/env python3

def add(vertex,neighbour):
    if vertex in graph:
        graph[vertex].append(neighbour)
    else:
        graph[vertex]=[neighbour]
    if neighbour in graph:     #####for undirected part remove to get directed
        graph[neighbour].append(vertex)
    else:
        graph[neighbour]=[vertex]

def dfs(graph,n,currnode):
    visited=[False for x in range(n+1)]
    stack=[currnode]
    ans=[]
    while stack:
        currnode=stack[-1]
        if visited[currnode]==False:
            visited[currnode]=True
            ans.append(currnode)
        if currnode in graph1:
            for neighbour in graph[currnode]:
                if visited[neighbour]==False:
                    visited[neighbour]=True
                    stack.append(neighbour)
                    ans.append(neighbour)
                    break    #####if we remove break it becomes bfs
            else:
                stack.pop() ####we are backtracking to previous node which is in  our stack
        else:
            stack.pop()
    return ans
n,m=[int(x) for x in input().split()]
nodes=n*m
arr=[None for i in range(nodes)]
for i in range(n):
    s=input()
    for j in range(m):
        arr[i*m+j]=s[j]
graph={}
for i in range(m,nodes):
    if i%m!=0 and arr[i]=="#":
        if arr[i-1]=="#":
            add(i,i-1)
        r=i//m;c=i%m
        if arr[(r-1)*m+c]=="#":
            add(i,(r-1)*m+c)
    elif i%m==0 and arr[i]=="#":
        #if arr[i+1]=="#":
            #add(i,i+1)
        r=i//m
        if arr[(r-1)*m]=="#":
            add((r-1)*m,i)

for i in range(1,m):
    if arr[i]=="#" and arr[i-1]=="#":
        add(i,i-1)

for i in range(nodes):
    if arr[i]=="#" and i not in graph:
        graph[i]=[]
graph1=graph.copy()
if len(graph)<3:
    print(-1)
else:
    found=False
    firstnode=[];secondnnode=[]
    for key,val in graph.items():
        if len(firstnode)==0:
            firstnode=[key,val]
            d=len(dfs(graph,nodes,firstnode[0]))
        elif len(secondnnode)==0:
            secondnnode=[key,val]
        else:
            del graph1[key]
            if len(dfs(graph1,nodes,firstnode[0]))-1!=d-1:
                found=True
                break
            graph1[key]=val
    else:
        del graph1[firstnode[0]]
        if len(dfs(graph1,nodes,secondnnode[0]))-1!=d-1:
            found=True
        graph1[firstnode[0]]=firstnode[1]
        del graph1[secondnnode[0]]
        if len(dfs(graph1,nodes,firstnode[0]))-1!=d-1:
            found=True
        graph1[secondnnode[0]]=secondnnode[1]

    if found==True:
        print(1)
    else:
        print(2)
