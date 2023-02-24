# 0-31: control 32-127: text symbols

a = ord('A')
print(a)
b = chr(65)
print(b)

S = ""
for i in range(65, 91):
  S += chr(i)
print(S)

s = ""
for i in range(97, 113):
  s += chr(i)
print(s)