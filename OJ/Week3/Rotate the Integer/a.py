#!/usr/bin/env python3
t = int(input())

def to_dec(s):
  i = 0
  no = 0
  while i < len(s):
    if s[i] == 1:
      no += 2**i
    i += 1
  return no

for i in range(1, t+1):
  num = int(input())
  if num*2 > 255:
    num = num*2-256+1
  else:
    num *= 2

  print(f'Case #{i}: {num}')