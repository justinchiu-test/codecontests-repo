#!/usr/bin/env python3

#!/usr/bin/env python3
"""
Choose best adjacent cardinal direction to maximize points served.
"""
from library import read_ints, best_cardinal_move

def main():
    n, x, y = read_ints()
    pts = [complex(*read_ints()) for _ in range(n)]
    cnt, (nx, ny) = best_cardinal_move(x, y, pts)
    print(cnt)
    print(nx, ny)

if __name__ == '__main__':
    main()
