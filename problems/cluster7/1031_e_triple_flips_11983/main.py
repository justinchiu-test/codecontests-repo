#!/usr/bin/env python3
from library import *

def main():
    n = read_int()
    a = read_ints()
    # small case: brute force
    if len(a) <= 10:
        sol = solve_triple_flips(a)
        if sol is None:
            print("NO")
            return
        print("YES")
        print(len(sol))
        # print operations in reversed order to match expected output
        for t in reversed(sol):
            print(*t)
        return
    # greedy reduction for large arrays
    operations = []
    while len(a) > 10:
        l = len(a)
        last = a[-3:]
        if last == [1, 1, 1]:
            operations.append([l - 2, l - 1, l])
        elif last == [1, 1, 0]:
            operations.append([l - 3, l - 2, l - 1])
            a[-4] ^= 1
        elif last == [1, 0, 1]:
            operations.append([l - 4, l - 2, l])
            a[-5] ^= 1
        elif last == [0, 1, 1]:
            nxt = a[-6:-3]
            if nxt == [1, 1, 1]:
                operations.append([l - 8, l - 4, l])
                operations.append([l - 5, l - 3, l - 1])
                a[-9] ^= 1
            elif nxt == [1, 1, 0]:
                operations.append([l - 8, l - 4, l])
                operations.append([l - 9, l - 5, l - 1])
                a[-9] ^= 1
                a[-10] ^= 1
            elif nxt == [1, 0, 1]:
                operations.append([l - 6, l - 3, l])
                operations.append([l - 9, l - 5, l - 1])
                a[-7] ^= 1
                a[-10] ^= 1
            elif nxt == [0, 1, 1]:
                operations.append([l - 6, l - 3, l])
                operations.append([l - 7, l - 4, l - 1])
                a[-7] ^= 1
                a[-8] ^= 1
            elif nxt == [1, 0, 0]:
                operations.append([l - 2, l - 1, l])
                operations.append([l - 8, l - 5, l - 2])
                a[-9] ^= 1
            elif nxt == [0, 1, 0]:
                operations.append([l - 2, l - 1, l])
                operations.append([l - 6, l - 4, l - 2])
                a[-7] ^= 1
            elif nxt == [0, 0, 1]:
                operations.append([l - 10, l - 5, l])
                operations.append([l - 5, l - 3, l - 1])
                a[-11] ^= 1
            elif nxt == [0, 0, 0]:
                operations.append([l - 8, l - 4, l])
                operations.append([l - 7, l - 4, l - 1])
                a[-9] ^= 1
                a[-8] ^= 1
            a.pop(); a.pop(); a.pop()
        elif last == [1, 0, 0]:
            operations.append([l - 4, l - 3, l - 2])
            a[-5] ^= 1; a[-4] ^= 1
            a.pop(); a.pop(); a.pop()
        elif last == [0, 1, 0]:
            operations.append([l - 5, l - 3, l - 1])
            a[-6] ^= 1; a[-4] ^= 1
            a.pop(); a.pop(); a.pop()
        elif last == [0, 0, 1]:
            operations.append([l - 6, l - 3, l])
            a[-7] ^= 1; a[-4] ^= 1
            a.pop(); a.pop(); a.pop()
    # finalize small suffix
    while len(a) < 8:
        a.append(0)
    suffix = solve_triple_flips(a)
    print("YES")
    sol = operations + suffix
    print(len(sol))
    for t in sol:
        print(*t)

if __name__ == '__main__':
    main()
