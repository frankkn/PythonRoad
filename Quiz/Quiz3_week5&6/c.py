#!/usr/bin/env python3
t = int(input())

def invert(st):
  tmp = ''
  for i in st:
    tmp += '0' if i == '1' else '1'
  return tmp

def reverse(st):
  return st[::-1]

def kth(n):
  if n == 0: return '0'
  tmp = kth(n-1)
  s = tmp + '1'
  s += reverse(invert(tmp))
  return s

for testcase in range(1, t+1):
  nk = input().split()
  n = int(nk[0])
  k = int(nk[1])
  sn = kth(n)

  # print(f'S{n}:{sn}')
  print(f'Case #{testcase}: {sn[k-1]}')