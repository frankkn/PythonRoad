#!/usr/bin/env python3
t = int(input())

for testcase in range(1, t+1):
  s = input()
  ans = 0
  base = 1
  for i in s[::-1]:
    ans += (ord(i)-64)*base
    base *= 26

  print(f'Case #{testcase}: {ans}')