from itertools import combinations

T = int(input())
for i in range(1,T+1):
  n,k = map(int,input().split())
  nums = [2**i for i in range(n)] # 2^i for i = 0 ~ (n-1)
  ans = sorted(list(map(sum,combinations(nums,k)))) # C(nums, k) while nums is a list 
  print(f'Case #{i}: {ans}')
