#!/usr/bin/env python3
def permute(nums):
  ans = []
  n = len(nums)
  def dfs(i):
    if i == n:
      ans.append(nums[:])
    else:
      for j in range(i, n):
        nums[i], nums[j] = nums[j], nums[i]
        dfs(i+1)
        nums[i], nums[j] = nums[j], nums[i]
  dfs(0)
  return sorted(ans)

# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(T):
    nums = list(map(int, input().split()))
    print(permute(nums))
