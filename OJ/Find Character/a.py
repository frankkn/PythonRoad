#!/usr/bin/env python3
t = int(input())

def index(text, pattern):
  i = 0
  while i < len(text):
    if pattern == text[i]:
      break
    i += 1
  else:
    return -1
  return i

for i in range(1, t+1):
  s = input().split()
  text = s[0]
  pattern = s[1]
  print(f'Case #{i}: {index(text, pattern)}')