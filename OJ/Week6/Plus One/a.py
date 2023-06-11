#!/usr/bin/env python3
t = int(input())

for testcase in range(1, t+1):
  s = int(''.join(input().split()))
  s += 1
  s = list(str(s))
  s = [int(x) for x in s]

  print(f'Case #{testcase}: {s}')