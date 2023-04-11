#!/usr/bin/env python3
def aver(*nums):
  total = 0.0
  for i in nums: 
    total += i
  return total/len(nums)

# T = int(input())
# for t in range(T):
#     nums = [int(n) for n in input().split()]
#     mean = aver(*nums)
#     print(f'{mean}')