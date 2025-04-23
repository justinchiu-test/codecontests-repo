#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 00:37:06 2021

@author: rishi
"""
import math

def ncr(n,r):
    p=1
    k=1
    if(n-r<r):
        r=n-r;
    if(r!=0):
        while(r>0):
            p*=n
            k*=r
            m=math.gcd(p,k)
            p//=m
            k//=m
            n-=1
            r-=1
    else:
        p=1
    return p


ans=[]
t=int(input())
for _ in range(t):
    a,b,k=list(map(int,input().split()))
    va=list(map(int,input().split()))
    vb=list(map(int,input().split()))
    ma=dict()
    mb=dict()
    vc=[]
    anss=0
    if(k<2):
        ans.append(0)
        continue
    for i in range(k):
        if(va[i] not in ma.keys()):
            ma[va[i]]=1
        else:
            ma[va[i]]+=1
    for i in range(k):
        if(vb[i] not in mb.keys()):
            mb[vb[i]]=1
        else:
            mb[vb[i]]+=1

    for i in range(k):
        vc.append([va[i],vb[i]])
    for i in range(k):
        ca=vc[i][0]
        cb=vc[i][1]
        anss+=k-ma[ca]-mb[cb]+1
    ans.append(anss//2)








for an in ans:
    print(an)
