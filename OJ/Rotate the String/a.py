#!/usr/bin/env python3
t = int(input())

for testcase in range(1, t+1):
  s = input()
  shift = int(input())

  if len(s) != 0:
    shift %= len(s) 

    if shift >= 0:
      s = s[shift:] + s[:shift]
    else:
      s = s[shift:] + s[:len(s)+shift]

  print(f'Case #{testcase}: {s}')