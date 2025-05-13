#!/usr/bin/env python3

import math
from library import getints
def a(x1,y1,x2,y2,x3,y3,x4,y4):
    b=sorted([[x1,y1],[x2,y2],[x3,y3],[x4,y4]])
    x1,y1=b[0]
    x2,y2=b[1]
    x3,y3=b[2]
    x4,y4=b[3]
    a1 = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    a2 = math.sqrt((x4-x2)**2 + (y4-y2)**2)
    a3 = math.sqrt((x4-x3)**2 + (y4-y3)**2)
    a4 = math.sqrt((x1-x3)**2 + (y1-y3)**2)
    return (
        a1 == a2 == a3 == a4 and a1 != 0
        and abs(abs(math.degrees(math.asin((y2-y1)/a1) - math.asin((y3-y1)/a4))) - 90) <= 1e-8
    )
def b(x1,y1,x2,y2,x3,y3,x4,y4):
    b=sorted([[x1,y1],[x2,y2],[x3,y3],[x4,y4]])
    x1,y1=b[0]
    x2,y2=b[1]
    x3,y3=b[2]
    x4,y4=b[3]
    a1 = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    a2 = math.sqrt((x4-x2)**2 + (y4-y2)**2)
    a3 = math.sqrt((x4-x3)**2 + (y4-y3)**2)
    a4 = math.sqrt((x1-x3)**2 + (y1-y3)**2)
    return (
        a1 == a3 and a2 == a4 and a1 != 0
        and abs(abs(math.degrees(math.asin((y2-y1)/a1) - math.asin((y3-y1)/a4))) - 90) <= 1e-8
    )
c = [list(getints()) for _ in range(8)]
z=False
for i in range(5):
    for j in range(i+1,6):
        for k in range(j+1,7):
            for l in range(k+1,8):
                if a(*c[i]+c[j]+c[k]+c[l]):
                    d=[]
                    e=[]
                    for m in range(8):
                        if m not in [i,j,k,l]:
                            d+=c[m]
                            e.append(m+1)
                    if b(*d):
                        print('YES')
                        print(i+1,j+1,k+1,l+1)
                        print(*e)
                        z=True
                        break
            if z:
                break
        if z:
            break
    if z:
        break
if not(z):
    print('NO')
