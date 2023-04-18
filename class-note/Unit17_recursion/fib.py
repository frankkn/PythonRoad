def fib(n):
  if n < 2:
    return 1
  else:
    return fib(n-1)+fib(n-2)

def fib_iterative_version(n):
    s0 = 1
    s1 = 1
    if n <= 1:
      return 1
    else:   
      for i in range (2, n+1):
        sn = s0 + s1
        s0 = s1
        s1 = sn
    return sn
fib_iterative_version(8)