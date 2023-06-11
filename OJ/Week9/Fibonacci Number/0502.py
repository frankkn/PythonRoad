#!/usr/bin/env python3
def fib(n):
  return 1 if n < 2 else fib(n-1)+fib(n-2)

# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(T):
    n = int(input())
    print(fib(n))
