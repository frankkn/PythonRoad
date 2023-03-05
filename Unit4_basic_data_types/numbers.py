a = 0b1001; print(a)
b = 0o100_101_110; print(b) # octal
c = 0xB5D3; print(c) 

d = 46549; print(d)
e = oct(46549); print(e) # 0o132725
f = hex(46549); print(f) # 0xb5d5
g = 0xb5d5; print(g)

h = 0b_010_100
i = 0b_110_111
j = bin(h ^ i); print(j) # true if bits are different
