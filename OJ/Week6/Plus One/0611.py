#!/usr/bin/env python3
t = int(input())

for testcase in range(1, t+1):
  L = list(input().split())
  ans = ""
  for i in range(len(L)):
    ans += str(L[i])
  ans = (int(ans) + 1)
  
  print(f'Case #{testcase}: {list(map(int, str(ans)))}')