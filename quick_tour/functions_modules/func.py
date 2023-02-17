def Total(L):
  'This accumulate all elements in L'
  total = 0
  for i in L:
    total += i
  return total

L = [1,3,5,7,9]
x = Total(L)
print(x)