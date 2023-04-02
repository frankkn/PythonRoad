#!/usr/bin/env python3

# uppercase < lower case
print('Apple' < 'apple') # True
print('apple' >= 'applesauce') # False
b = (1,2,3) < (1,3)
print(b) # True

# Membership test
b1 = (1, 2) in (1, 2, 3)
print(b1) # False

# Concatienation with +
L = ('a', 'b', 'c') + ('d', 'e')
print(L) # ('a', 'b', 'c', 'd', 'e')
# ['counter'] + 'clockwise' <- TypeError

# Repetition with *
x = (1, 2)
y = (3, x)
print(y * 2) # (3, (1, 2), 3, (1, 2))