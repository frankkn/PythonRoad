#!/usr/bin/env python3

W = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
D = {'Sun':0, 'Mon':1, 'Tue':2, 'Wed':3, 'Thu':4, 'Fri':5, 'Sat':6}


L = W[:]
L.sort()
print(L)
L.sort(key = lambda s:W.index(s))
print(L)

L.sort()
print(L)
L.sort(key = lambda s:D[s])
print(L)