#!/usr/bin/env python3

import sys
numberOfArgs = len(sys.argv)
if numberOfArgs != 2 and numberOfArgs != 3:
  sys.stderr.write('Usage: %s inputFile\n' % sys.argv[0])
  sys.stderr.write('Usage: %s -n inputFile\n' % sys.argv[0])
  sys.exit(1)
if numberOfArgs == 2:
  try:
    fh = open(sys.argv[1], 'r')
  except:
    sys.stderr.write('cannot open input file %s\n' % sys.argv[1])
    sys.exit(2)
  for line in fh.readlines():
    print(line, end='')
else:
  try:
    fh = open(sys.argv[2], 'r')
  except:
    sys.stderr.write('cannot open input file %s\n' % sys.argv[2])
    sys.exit(2)
  numberOfline = 1
  for line in fh.readlines():
    print('%d ' % numberOfline, end='')
    numberOfline += 1
    print(line, end='')
fh.close