#!/usr/bin/env python3

#!/usr/bin/env python3
from library import ni

s = ni(); x = ni()
if x > s or (s - x) & 1:
    print(0)
    exit()
u = (s - x) // 2
# if any bit set in both u and x, no solution
if u & x:
    print(0)
    exit()
res = 1 << x.bit_count()
if s == x:
    # exclude trivial zero case
    res = max(0, res - 2)
print(res)
