#!/usr/bin/env python3
# cat: print all lines
# -b number nonblank output lines
# -n number output lines
# -s squeeze multiple adjacent empty lines
# -v display nonprinting characters

# implement cat

import sys
numberOfArgs = len(sys.argv)
if numberOfArgs < 2:
  sys.stderr.write('Usage: %s inputFiles\n' % sys.argv[0])
  sys.exit(1)

for fileName in sys.argv[1:]:
  try:
    fh = open(fileName, 'r')
  except:
    sys.stderr.write('cannot open input file %s\n' % fileName)
    sys.exit(2)
  for line in fh.readlines():
    print(line, end='')
  fh.close