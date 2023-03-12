#!/usr/bin/env python3

import sys
numberOfArgs = len(sys.argv)
if sys.argv[1] != '-n':
  if numberOfArgs < 2:
    sys.stderr.write('Usage: %s inputFiles\n' % sys.argv[0])
    sys.exit(1)
else:
  if numberOfArgs < 3:
    sys.stderr.write('Usage: %s -n inputFiles\n' % sys.argv[0])
    sys.exit(1)

if sys.argv[1] != '-n':
  for fileName in sys.argv[1:]:
    try:
      fh = open(fileName, 'r')
    except:
      sys.stderr.write('cannot open input file %s\n' % fileName)
      sys.exit(2)
    for line in fh.readlines():
      print(line, end='')

else:
  for fileName in sys.argv[2:]:
    try:
      fh = open(fileName, 'r')
    except:
      sys.stderr.write('cannot open input file %s\n' % fileName)
      sys.exit(2)
    numberOfline = 1
    for line in fh.readlines():
      print('%d ' % numberOfline, end='')
      numberOfline += 1
      print(line, end='')
    numberOfline = 0

fh.close