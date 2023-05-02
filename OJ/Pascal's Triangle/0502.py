#!/usr/bin/env python3
def pascal(row, col):
  if col == 0 or row == col:
    return 1
  else:
    return pascal(row-1, col-1) + pascal(row-1, col)

def print_pascal(n):
  for i in range(n):
    for j in range(i+1):
      e = pascal(i,j)
      print(f'{e:3d}', end="")
    print('')
# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(T):
    n = int(input())
    print_pascal(n)