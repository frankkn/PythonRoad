#!/usr/bin/env python3

def bin_to_dec(s):
  ans = 0
  s = s[::-1]
  for i in range(0, len(s)):
      ans += int(s[i]) * (2**i)
  return ans

def f(s, i, n, used, k, ans):
  if(used > k):
    return

  if i == n:
    if used == k:
      ans.append(bin_to_dec(s))
    return 

  s += '0'
  f(s, i+1, n, used, k, ans)
  s = s[:len(s)-1]

  s += '1'
  f(s, i+1, n, used+1, k, ans)
  s = s[:len(s)-1]

  return ans

t = int(input())

for testcase in range(1, t+1):
  n, k = list(map(int, input().split()))

  ans = []
  ans = f("", 0, n, 0, k, ans)

  print(f'Case #{testcase}: {ans}')