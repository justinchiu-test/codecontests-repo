#!/usr/bin/env python3
from library import ni

def main():
    n = ni()
    x = ni(); y = ni()
    # counts: lu, ld, ru, rd, up, down, left, right
    lu = ld = ru = rd = up = down = left = right = 0
    for _ in range(n):
        a = ni(); b = ni()
        if a < x and b < y:
            ld += 1
        elif a < x and b > y:
            lu += 1
        elif a == x and b != y:
            if b > y:
                up += 1
            else:
                down += 1
        elif a > x and b < y:
            rd += 1
        elif a > x and b > y:
            ru += 1
        elif b == y and a != x:
            if a < x:
                left += 1
            else:
                right += 1
    options = [lu + ru + up,
               lu + ld + left,
               ru + rd + right,
               ld + rd + down]
    ans = max(options)
    idx = options.index(ans)
    print(ans)
    if idx == 0:
        print(x, y + 1)
    elif idx == 1:
        print(x - 1, y)
    elif idx == 2:
        print(x + 1, y)
    else:
        print(x, y - 1)

if __name__ == '__main__':
    main()
