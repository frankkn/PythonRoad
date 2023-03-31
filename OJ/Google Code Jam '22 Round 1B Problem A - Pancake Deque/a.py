#!/usr/bin/env python3
t = int(input())

for testcase in range(1, t+1):
  n = int(input())
  # map(function, iterable)
  D = list(map(int, input().split()))
  
  prev = 0
  cnt = 0
  left, right = 0, n-1
  while left <= right:
    if D[left] <= D[right]:
      i = left
      left += 1
    else:
      i = right
      right -= 1
    if D[i] >= prev:
      prev = D[i]
      cnt += 1
  print(f'Case #{testcase}: {cnt}')