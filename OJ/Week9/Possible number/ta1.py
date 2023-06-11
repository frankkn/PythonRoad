def possible_num(nums,k):
  ans = []
  def helper(nums,k,tmp):
    if k == 0:
      ans.append(tmp)
    else:
      for i,v in enumerate(nums):
        helper(nums[i+1:],k-1,tmp+v)
  helper(nums,k,0)
  return sorted(ans)
T = int(input())
for t in range(1,T+1):
  n,k = map(int,input().split())
  nums = [2**i for i in range(n)]
  print(f'Case #{t}: {possible_num(nums,k)}')
