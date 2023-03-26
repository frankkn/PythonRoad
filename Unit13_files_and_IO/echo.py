#!/usr/bin/env python3
"Demonstrates stdio by echoing"
import sys
while True:
    line = sys.stdin.readline()
    if line == '': # ctrl+D
        break
    sys.stdout.write(line)