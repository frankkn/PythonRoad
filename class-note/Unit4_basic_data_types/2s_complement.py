# To negate a number, flip all bits then +1

a = 18
print(~a) # -19

b = 0b1011 >> 2
print(bin(b)) # 0b10

c = 0b1011 << 2
print(bin(c & 0b111111)) # 0b101100