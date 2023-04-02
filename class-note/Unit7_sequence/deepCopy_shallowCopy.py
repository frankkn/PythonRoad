#!/usr/bin/env python3

# Shallow copy
X = ['A', 'B']
L = [1, X, 2, 3]
print(L) # [1, ['A', 'B'], 2, 3]
M = L.copy()
print(M) # [1, ['A', 'B'], 2, 3]
X.pop() # 'B'
print(L) # [1, ['A'], 2, 3]
print(M) # [1, ['A'], 2, 3]
L.extend(['y', 'z'])
print(L) # [1, ['A'], 2, 3, 'y', 'z']
print(M) # [1, ['A'], 2, 3]

# Deep copy
import copy
X = ['A', 'B']
L = [1, X, 2, 3]
M = copy.deepcopy(L)
print('---')
print(L) # [1, ['A', 'B'], 2, 3]
print(M) # [1, ['A', 'B'], 2, 3]
X.pop()
print(L) # [1, ['A'], 2, 3]
print(M) # [1, ['A', 'B'], 2, 3]
L.extend(['y', 'z'])
print(L) # [1, ['A'], 2, 3, 'y', 'z']
print(M) # [1, ['A', 'B'], 2, 3]