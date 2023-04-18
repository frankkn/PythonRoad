#!/usr/bin/env python3
def pascal(row, col):
  if col == 0 or row == col:
    return 1
  else:
    return pascal(row-1, col-1) + pascal(row-1, col)

def print_pascal(n):
  for i in range(0, n):
    line = []
    for j in range(0, i+1):
      line.append(pascal(i, j))
    for item in line:
      print(f'{item:>3d}', end='')
    print('')
# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(T):
    n = int(input())
    print_pascal(n)
