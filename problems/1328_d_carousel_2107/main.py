#!/usr/bin/env python3

for i in range(int(input())):
    n = int(input())
    kinds = [int(i) for i in input().split()]
    id1 = 1
    k = 1
    answer = [1] * n
    while id1 < n:
        if kinds[id1] == kinds[id1 - 1]:
            break
        if answer[id1 - 1] == 1:
            answer[id1] = 2
        else:
            answer[id1] = 1
        id1 += 1
        k = 2
    if id1 == n:
        if n % 2 and kinds[n - 1] != kinds[0]:
            answer[0] = 3
            print(3)
            print(*answer)
        else:
            print(2)
            print(*answer)
        continue
    id2 = n - 1
    while id2 >= 0:
        if kinds[id2] == kinds[(id2 + 1) % n]:
            break
        if answer[(id2 + 1) % n] == 1:
            answer[id2] = 2
        else:
            answer[id2] = 1
        id2 -= 1
        k = 2
    for j in range(id1, id2 + 1):
        if kinds[j] != kinds[j - 1]:
            if answer[j - 1] == 1:
                answer[j] = 2
            else:
                answer[j] = 1
            k = 2
        else:
            answer[j] = 1
    print(k)
    print(*answer)
