#!/usr/bin/env python3

t = int(input())

for test in range(1, t+1):
    text, pattern = input().split()
    idx = -1
    for i in text:
        if i == pattern:
            idx = text.index(i)
    print(f'Case #{test}: {idx}')