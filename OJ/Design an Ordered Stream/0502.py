#!/usr/bin/env python3
class OrderedStream:
  dict = {}
  _n = 0
  ptr = 1
  def __init__(self, n: int):
    self._n = n
    for i in range(1,n+1):
      self.dict[i] = None

  def insert(self, idKey: int, value: str):
    self.dict[idKey] = value
    ans = []
    while(self.ptr <= self._n and self.dict[self.ptr] != None):
      ans.append(self.dict[self.ptr])
      self.ptr += 1
    return ans
# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
stream = OrderedStream(5)
print(stream.insert(3, "ccccc"))
print(stream.insert(1, "aaaaa"))
print(stream.insert(2, "bbbbb"))
print(stream.insert(5, "eeeee"))
print(stream.insert(4, "ddddd"))
