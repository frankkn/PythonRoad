def count(x):
  if type(x) != list:
    return 1
  c = 0
  for i in x:
    c = count(i)
  return c

def count(x):
  return 1 if type(x) != list \
    else sum(map(count, x))

def count(x):
  if type(x) != type([]):
    return 1
  elif len(x) == 0:
    return 0
  else:
    return count(x[0]) + count(x[1:])