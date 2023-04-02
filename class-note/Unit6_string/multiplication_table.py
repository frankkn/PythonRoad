#!/usr/bin/env python3

def MultTable(L, R):
  '''L and R are ranges'''
  for left in L:
    for right in R:
      print('{:3d} x {:3d} = {:3d}'.format(left, right, left * right))

if __name__ == '__main__':
  lRange = range(9, 12)
  rRange = range(8, 11)
  MultTable(lRange, rRange)