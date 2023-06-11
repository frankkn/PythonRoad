#!/usr/bin/env python3
class RecentCounter:
  _n = 0
  L = []
  def __init__(self):
    self._n = 0
    self.L = []  
  def ping(self, t):
    self.L.append(t)
    self._n += 1
    i = self._n-1
    cnt = 0
    while i >= 0:
      if self.L[i] + 3000 < t:
        break
      else:
        cnt += 1
        i -= 1
    return cnt

# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(1,T+1):
    counter = RecentCounter()
    calls = list(map(int,input().split()))
    for ind,time in enumerate(calls):
        print(f'Case #{t}_{ind}: {counter.ping(time)}')