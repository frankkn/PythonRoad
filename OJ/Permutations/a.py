#!/usr/bin/env python3
# NEED TO DEBUG
def permute(nums):
  def dfs(i):
    if i == len(nums):
      ans.append(nums[:])
    for j in range(i, len(nums)):
      nums[i], nums[j] = nums[j], nums[i]
      dfs(i + 1)
      nums[i], nums[j] = nums[j], nums[i]

  ans = []
  dfs(0)
  return sorted(ans)
    
# def permute(nums):
#   from itertools import permutations
#   ans = permutations(nums)
#   ans = list(map(list, ans))
#   return ans

# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(T):
  nums = list(map(int, input().split()))
  print(permute(nums))