#!/usr/bin/env python3

# wc mult.py
# > 9 32 249 mult.py
# 9 lines 32 words 249 characters

import sys
numberOfArgs = len(sys.argv)
if numberOfArgs != 2:
  sys.stderr.write('Usage: %s inputFile\n' % sys.argv[0])
  sys.exit(1)
try:
  fh = open(sys.argv[1], 'r')
except:
  sys.stderr.write('cannot open input file %s\n' % sys.argv[1])
  sys.exit(2)
lines = words = chars = 0
for line in fh.readlines():
  lines += 1
  words += len(line.split())
  chars += len(line)
fh.close
print('{:8d}{:8d}{:8d} {}'.format(lines, words, chars, sys.argv[1]))