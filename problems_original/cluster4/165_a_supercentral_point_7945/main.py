#!/usr/bin/env python3

n=int(input())
a=[]
for i in range(0,n):
    a.append([int(i) for i in input().split()])
ans=0
for i in range(0,n):
    c1=0
    c2=0
    c3=0
    c4=0
    for j in range(0,n):
        if a[i][0]>a[j][0] and a[i][1]==a[j][1]:
            c1+=1
        elif a[i][0]<a[j][0] and a[i][1]==a[j][1]:
            c2+= 1
        elif a[i][0]==a[j][0] and a[i][1]<a[j][1]:
            c3+= 1
        elif a[i][0]==a[j][0] and a[i][1]>a[j][1]:
            c4+= 1
    if c1>=1 and c2>=1 and c3>=1 and c4>=1:
        ans+=1
print(ans)