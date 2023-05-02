#!/usr/bin/env python3
t = int(input())

for testcase in range(1, t+1):
  n, k = map(int, input().split())
  nums = [2**i for i in range(n)]
  from itertools import combinations
  ans = sorted(list(map(sum, combinations(nums, k))))
  print(f'Case #{testcase}: {ans}')