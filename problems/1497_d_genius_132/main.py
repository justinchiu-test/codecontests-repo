#!/usr/bin/env python3

def nr():return int(input())
def nrs():return [int(i) for i in input().split()]
def f(n,t,s):
	d=[0]*n
	for i in range(1,n):
		for j in range(i-1,-1,-1):
			if t[i]==t[j]:continue
			sc=abs(s[i]-s[j])
			d[i],d[j]=max(d[i],d[j]+sc),max(d[j],d[i]+sc)
	return max(d)
for _ in range(nr()):
	n=nr()
	t=nrs()
	s=nrs()
	print(f(n,t,s))
