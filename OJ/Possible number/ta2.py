def possible_num(n):
  record = {i:[] for i in range(n+1)}
  for i in range(1<<n):
    cnt = 0
    num = i
    while i > 0:
      cnt += (1 & i)
      i = i>>1
    record[cnt].append(num)

  return record


ans = {i:possible_num(i) for i in range(1,17)}

T = int(input())
for i in range(1,T+1):
  n,k = map(int,input().split())
  print(f'Case #{i}: {ans[n][k]}')
