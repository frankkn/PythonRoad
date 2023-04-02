#!/usr/bin/env python3
#2.1 By position
s1 = 'Hello {}, your ID is {}'.format('Harry', 12345)
print(s1)

#2.2 By position index
s2 = 'Hello {0}, your ID is {1}'.format('Harry', 12345)
print(s2)

s3 = 'one {0}, two {0}s, three {0}s'.format('apple')
print(s3)

s4 = 'decimal {0}, hex{0:x}, bin {0:b}'.format(23)
print(s4)

#2.3 By keyword argument
u = 'Hello {name}, your ID is {id}'.format(name = 'Frank', id = 12345)
print(u)

# str.format() conversion type
# {:s} str, {:d} dec, {:x} hex, {:f} float
w = 'Hello {:s}, your ID is {:08d}'.format('Frank', 12345)
print(w) # 'Hello Frank, your ID is 00012345'

# Padding with Alignment
# < left-align > right-align ^ centered
x = 'Hello {name:_<20s}, your ID is {id:08d}'.format(name = 'Frank', id = 12345)
print(x) # 'Hello Frank_______________, your ID is 00012345'
