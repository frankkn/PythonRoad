#!/usr/bin/env python3
def reverse(L):
  rL = L[::-1]
  for i, subL in enumerate(rL):
    if type(subL) == list:
      rL[i] = reverse(subL)
  return rL

t = int(input())
for c in range(t+1):
  L = input()
  L = reverse(L)
  print(L)