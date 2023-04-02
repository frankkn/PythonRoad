#!/usr/bin/env python3

# uniq: filters out repeated lines in a file

# $ uniq [options] [inputfile[outputfile]]

# Implement uniq

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
prevLine = ''
for line in fh.readlines():
  if line != prevLine:
    print(line, end='')
  prevLine = line
fh.close()