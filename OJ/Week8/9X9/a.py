#!/usr/bin/env python3
def get_products(a=1, b=9, c=1, d=9):
  L = []
  for i in range(a, b+1):
    for j in range(c, d+1):
      prod = i*j
      L.append(prod)
  return L