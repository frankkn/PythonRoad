#!/usr/bin/env python3

def f():
  DNA = input()
  n = len(DNA)
  ans = []
  cur = ""
  idx = 0
  while idx < n:
    if idx == 0:
      cur += DNA[idx]
      idx += 1
      continue
    else:
      # case 1:prev == A
      if DNA[idx-1] == 'A':
        if DNA[idx] == 'A':
          ans.append(cur)
          cur = 'A'
        else:
          cur += DNA[idx]
      # case 2:prev != A
      else:
        if DNA[idx] == 'A':
          cur += 'A'
        else:
          ans.append(cur)
          cur = DNA[idx]
      idx += 1
  ans.append(cur)
  print(' '.join(ans))

if __name__ == '__main__':
  f()