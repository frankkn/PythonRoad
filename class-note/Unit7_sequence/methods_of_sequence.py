#!/usr/bin/env python3

# Mutation methods, list only
# append(e)
# extend(L): add L[:] to end of list
# pop(): remove last element
# insert(p, e): insert e at position p
# reverse()
# sort()
# remove(e): remove 1st occurrence of e
# claer()

L = ['Sun', 'Mon', 'Tue']
print(L.pop()) # 'Tue'
del(L[1]) # no return value
print(L) # ['Sun']

# Difference between mutation and create-and-reassign
L= ['h', 'e', 'l', 'l', 'o']
L.reverse()
print(L) # ['o', 'l', 'l', 'e', 'h']
M = ['h', 'e', 'l', 'l', 'o']
M = M[::-1] # create and reassign
print(M) # ['o', 'l', 'l', 'e', 'h']

L = list(range(4)) # L = [0, 1, 2, 3]
L.insert(3, 'z') 
print(L) # [0, 1, 2, 'z', 3]
L.extend(['y', 'z']) 
print(L) # [0, 1, 2, 'z', 3, 'y', 'z']
# L.sort() # TypeError: '<' not supported between instances of 'int' and 'str'

import random
L = list(range(10))
random.shuffle(L) # [1, 2, 9, 6, 7, 5, 3, 0, 8, 4]
print(L)
L.sort() # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(L)

# Queue
L = ['a', 'b', 'c']
L.append(3) # L = ['a', 'b', 'c', 3]
print(L.pop(0)) # 'a'
print(L.pop(0)) # 'b'

# all sequences: (str, tuple, list)
# index(e): index of 1st occurrence of e 
# count(e): times e occurs in list