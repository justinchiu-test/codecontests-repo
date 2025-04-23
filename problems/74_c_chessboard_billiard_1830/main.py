#!/usr/bin/env python3

import math
n,m=map(int,input().split())
print(math.gcd(n-1,m-1)+1)
