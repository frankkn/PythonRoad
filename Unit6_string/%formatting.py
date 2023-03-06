#!/usr/bin/env python3

# string formatting with % operator
# %c, %d, %s, %f
month = 'Mar.'
day = 6
year = 2023
date = 'Due %s %d %d' % (month, day, year)
print(date)

n = 12345678
rep = '%d is %x hex, %o octal' % (n, n, n)
print(rep)

# %9.2f: 整個浮點數(不是整數!!)保留9個位置，小數點佔一個，小數點後佔兩個
z = '%09.2f' % 12.3 
print(z) # 000012.30

y = '%+09.2f' % -12.3
print(y) # -00012.30 if number is negative, still display -

a = '%08x' % 0x23
print(a) # 00000023

b = '%#08x' % 0x23
print(b) # 0x000023

c = '%5d' % 123456
print(c) # '123456'

# Scientific notation
# 2e3 = 2000.0 floating number 
q = '%1.3e' % 2.3
print(q) # 2.300e+00

w = '%10.3e' % 2.3
print(w) # ' 2.300e+00'

e = '%+15.3e' % 245.3
print(e) # '       +2.45300e+02'
