#!/usr/bin/env python3
t = int(input())

for testcase in range(1, t+1):
  numList = [int(num) for num in input().split()]
  i, j = 0, len(numList)-1
  ans = 'Yes'
  while i < j:
    if numList[i] != numList[j]:
      ans = 'No'
      break
    i += 1
    j -= 1

  print(f'Case #{testcase}: {ans}')