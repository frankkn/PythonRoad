#!/usr/bin/env python3
t = int(input())
import string

for testcase in range(1, t+1):
  s = input()
  ss = ''
  for i in s:
    if i in string.ascii_letters:
      if ord(i) == 90:
        ss += 'A'
      elif ord(i) == 122:
        ss += 'a'
      else:
        ss += chr(ord(i)+1)
    else:
      ss += i

  print(f'Case #{testcase}: {ss}')