#!/usr/bin/env python3

from collections import  defaultdict
from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
import threading
def f(a):
	n=len(a)
	a=list(map(lambda s:s-1,a))
	root=None
	for i in range(len(a)):
		if a[i]==i:
			root=i
	vis=[0]*(n)
	traitors=[]
	for i in range(0,n):
		cycle=-1
		cur=i
		move=set()

		while vis[cur]==0:
			vis[cur]=1
			move.add(cur)
			if a[cur] in move:
				cycle=cur
			cur=a[cur]
		if cycle!=-1:
			traitors.append(cycle)
	ans=len(traitors)-1
	if root==None:
		a[traitors[0]]=traitors[0]
		root=traitors[0]
		ans+=1
	for i in traitors:
		if i!=root:
			a[i]=root
	print(ans)
	a=list(map(lambda s:s+1,a))
	return a
n=input()
a=list(map(int,input().strip().split()))
print(*f(a))
