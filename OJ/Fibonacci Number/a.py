def fib(n):
  # your code here
  if n < 2:
    return 1
  else:
    return fib(n-1) + fib(n-2)


# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(T):
  n = int(input())
  print(fib(n))