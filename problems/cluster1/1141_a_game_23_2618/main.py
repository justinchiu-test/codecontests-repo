#!/usr/bin/env python3

#!/usr/bin/env python3
"""
Solution for CF 1141A: count moves to transform n to m by *2 or *3.
"""
from library import ni

n = ni()
m = ni()
if m % n != 0:
    print(-1)
else:
    x = m // n
    cnt = 0
    while x % 2 == 0:
        x //= 2; cnt += 1
    while x % 3 == 0:
        x //= 3; cnt += 1
    print(cnt if x == 1 else -1)
