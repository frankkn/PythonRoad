#!/usr/bin/env python3
from math import sqrt # you may use this function to calculate the area

class Triangle:
  # accepts the three sides of triangle
  _a = _b = _c = 0.0
  def __init__(self, s0, s1, s2):
    self._a = s0
    self._b = s1
    self._c = s2

  # return the perimeter of this triangle.
  @property
  def perimeter(self):
    return int(self._a + self._b + self._c)

  # return the area of this triangle.
  @property
  def area(self):
    s = (self._a + self._b + self._c) / 2
    return sqrt(s*(s-self._a)*(s-self._b)*(s-self._c))

# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(T):
    side = list(map(int, input().split()))
    t = Triangle(side[0], side[1], side[2])
    print(f'{t.perimeter} {t.area:.2f}')
