#!/usr/bin/env python3

# grep: print matched lines in the input file(s)
# $ grep pattern files
# $ man grep

# grep keyword *.py

# case-insensitive
# grep -i keyword files.py 

# implement grep

import sys
numberOfArgs = len(sys.argv)
if numberOfArgs != 3:
  sys.stderr.write('Usage: %s pattern inputFile\n' % sys.argv[0])
  sys.exit(1)
try:
  fh = open(sys.argv[2], 'r')
except:
  sys.stderr.write('cannot open input file %s\n' % sys.argv[2])
  sys.exit(2)
pattern = sys.argv[1]
for line in fh.readlines():
  if line.find(pattern) >= 0: # matched
    print(line, end='')
fh.close