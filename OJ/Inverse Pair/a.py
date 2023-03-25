#!/usr/bin/env python3
t = int(input())

for testcase in range(1, t+1):
  list = [int(i) for i in input().split()]
  cnt = 0
  for i in range(0, len(list)-1):
    for j in range(0, len(list)-1):
      if list[j] > list[j+1]:
        (list[j], list[j+1]) = (list[j+1], list[j])
        cnt += 1

  print(f'Case #{testcase}: {cnt}')