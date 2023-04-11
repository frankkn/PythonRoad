#!/usr/bin/env python3
def evaluate(expr):
  result = int(eval(expr))
  return result

T = int(input())
for t in range(T):
    result = evaluate(input())
    print(result)