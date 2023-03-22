#!/usr/bin/env python3
t = int(input())

for testcase in range(1, t+1):
  s = input().split()
  op = ''
  a = complex(s[0]).real
  b = complex(s[0]).imag
  c = complex(s[1]).real
  d = complex(s[1]).imag
  if a > c and b > d:
    op = '>'
  elif a < c and b < d:
    op = '<'
  elif a == c and b == d:
    op = '=='
  elif (a == c and b > d) or (a > c and b == d):
    op = '>='
  elif (a == c and b < d) or (a < c and b ==d ):
    op = '<='
  else:
    op = '!='

  print(f'Case #{testcase}: {complex(s[0])} {op} {complex(s[1])}')