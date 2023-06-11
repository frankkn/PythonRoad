#!/usr/bin/env python3
def adder(*args):
  total = 0
  for i in range(0, len(args)):
    if i % 2 == 0:
      total += args[i]
    else:
      total -= args[i]
  return total

'''
if __name__ == '__main__':
    t = int(input())
    for i in range(1, t+1):
        args = map(int, input().split())
        print("Case #%d: %d" % (i, adder(*args)))
'''