#!/usr/bin/env python3

# [expression for loopVar in iteration if condition]
L1 = [chr(65+i) for i in range(5)] # 65 is ASCII for 'A'
# ['A', 'B', 'C', 'D', 'E']

L2 = [2**i for i in range(1, 11)] # powers of 2 up to 2^10
# [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

L3 = [(chr(i), i) for i in range(65, 70)] # tuples of (char, code)
# [('A', 65), ('B', 66), ('C', 67), ('D', 68), ('E', 69)]

L4 = [chr(i) for i in range(65, 65+26)] # all uppercase letters
# ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

L5 = [chr(i) for i in range(65, 65+26) \
  if chr(i) not in ['A', 'E', 'I', 'O', 'U']] # non-vowel subset
# ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

L6 = [i*(i+1) for i in range(11)]
# [0, 2, 6, 12, 20, 30, 42, 56, 72, 90, 110]

L7 = [i*(i+1) for i in range(11) \
  if i*(i+1)%3 == 0] # filter for multiples of 3 
# [0, 6, 12, 30, 42, 72, 90]

L8 = [(i, j, i*j) for i in range(5) for j in range(5)] 
L9 = [(i, j, i*j) for i in range(5) for j in range(i, 5)] # upper triangle
L10 = [(i, j, i*j) for i in range(5) for j in range(i, 5) if i != j] # exclude diagonals
