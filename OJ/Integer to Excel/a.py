#!/usr/bin/env python3
t = int(input())

dict = {i:chr(i+64) for i in range(1, 27)}

for testcase in range(1, t+1):
  num = int(input())
  if num <= 26:
    print(f'Case #{testcase}: {dict[num]}')
    continue

  ans = ''

  while num > 26:
    res = divmod(num, 26)
    if res[1] != 0:
      ans += dict[res[1]]
      num = res[0]
    else:
      ans += 'Z'
      num = res[0]-1
  ans += dict[num]
  ans = ans[::-1]
  print(f'Case #{testcase}: {ans}')