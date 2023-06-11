#!/usr/bin/env python3
t = int(input())

for testcase in range(1, t+1):
  target = int(input())
  L = input().split()
  L = [int(i) for i in L]

  dict = {}
  ans = []
  for i, v in enumerate(L):
    if target-v in dict:
      ans.append(i)
      ans.append(dict[target-v])
    else:
      dict[v] = i

  print(f'Case #{testcase}: {sorted(ans)}')