#!/usr/bin/env python3
t = int(input())

for testcase in range(1, t+1):
    s1 = set(map(int, input().split()))
    s2 = set(map(int, input().split()))
    s3 = s1.intersection(s2)

    print(f'Case #{testcase}: {sorted(list(s3))}')