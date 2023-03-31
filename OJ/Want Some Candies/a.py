#!/usr/bin/env python3
t = int(input())

for testcase in range(1, t+1):
  L = [int(x) for x in input().split()]
  from collections import defaultdict
  d = defaultdict(int)
  for i in L:
    d[i] += 1
  cnt = 0
  for i in d:
    if cnt + 1 <= len(L)/2:
      cnt += 1
    else:
      break


  print(f'Case #{testcase}: {cnt}')