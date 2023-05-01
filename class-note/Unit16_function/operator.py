#!/usr/bin/env python3
import operator # dir(operator)
from operator import neg

L = [2, -5, 3, -4, 1]
# L = list(map(lambda x: -x, L))
L = list(map(neg, L))
print(L)