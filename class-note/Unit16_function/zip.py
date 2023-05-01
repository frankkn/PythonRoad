#!/usr/bin/env python3

L1 = [3,7,2,5,10]
L2 = [6,1,0,9,8]
L3 = [4,8,3,6,11]

# L =list(map(max, L1, L2, L3))

L = [max(*t) for t in zip(L1, L2, L3)]

print(L) # [6, 8, 3, 9, 11]