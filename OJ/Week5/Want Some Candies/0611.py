#!/usr/bin/env python3
t = int(input())

for testcase in range(1, t+1):
    D = {}
    L = list(map(int, input().split()))
    cnt = 0
    ans = 0
    for i in L:
        if i not in D.keys():
            D[i] = 1
        else:
            D[i] += 1
        cnt += 1
    for i in D.items():
        if ans < cnt/2:
            ans += 1
        else:
            break
    print(f'Case #{testcase}: {ans}')