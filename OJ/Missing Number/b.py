#!/usr/bin/env python3
t = int(input())

for testcase in range(1, t+1):
  arr = [int(i) for i in input().split()]
  cnt = [0 for i in range(1, len(arr)+2)]
  for i in arr:
    cnt[i] = 1
  ans = 0
  for i in cnt:
    if i == 0:
      ans = cnt.index(i)
      break

  print(f'Case #{testcase}: {ans}')