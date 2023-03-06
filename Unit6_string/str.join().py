#!/usr/bin/env python3

s1 = '_'.join(['hello', 'world', 'goodbye'])
print(s1)

s2 = '-'.join('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print(s2)

def MakeSankeCase(s):
  return '_'.join(s.split())

s3 = MakeSankeCase('this is a name')
print(s3)

