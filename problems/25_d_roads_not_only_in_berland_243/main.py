#!/usr/bin/env python3

'''
    Auther: ghoshashis545 Ashis Ghosh
    College: jalpaiguri Govt Enggineering College

'''
from os import path
import sys
from heapq import heappush,heappop
from functools import cmp_to_key as ctk
from collections import deque,defaultdict as dd
from bisect import bisect,bisect_left,bisect_right,insort,insort_left,insort_right
from itertools import permutations
from datetime import datetime
from math import ceil,sqrt,log,gcd
def ii():return int(input())
def si():return input().rstrip()
def mi():return map(int,input().split())
def li():return list(mi())
abc='abcdefghijklmnopqrstuvwxyz'
mod=1000000007
# mod=998244353
inf = float("inf")
vow=['a','e','i','o','u']
dx,dy=[-1,1,0,0],[0,0,1,-1]

def bo(i):
    return ord(i)-ord('a')

file=1





def solve():




    n = ii()

    par = [i for i in range(n+1)]

    freq = [1 for i in range(n+1)]
    def find(i):
        if i==par[i]:
            return i

        par[i] = find(par[i])
        return par[i]

    def union(x,y):
        x = find(x)
        y = find(y)
        if x==y:
            return 0
        if freq[x] < freq[y]:
            par[x] = y
            freq[y] += 1
        else:
            par[y] = x
            freq[x] += 1
        return 1



    erase = []
    for i in range(n-1):

        x,y = mi()

        x1 = find(x)
        y1 = find(y)

        if x1==y1:
            erase.append([x,y])
            continue
        union(x,y)

    add = []

    x = list(set(par[1:]))

    for i in range(1,len(x)):
        if(union(x[0],x[i])):
            add.append([x[0],x[i]])

    print(len(add))
    for i in range(len(add)):
        print(*erase[i],end=" ")
        print(*add[i],end=" ")
        print()












if __name__ =="__main__":

    if(file):

        if path.exists('input.txt'):
            sys.stdin=open('input.txt', 'r')
            sys.stdout=open('output.txt','w')
        else:
            input=sys.stdin.readline
    solve()
