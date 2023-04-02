#!/usr/bin/env python3

import string
# help(string)

str = string.ascii_letters
print(str)

a = ',' in string.punctuation
print(a) # True

b = string.capwords('hello world')
print(b) # Hello World

def MakeCamelCase(s):
  return ''.join(string.capwords(s).split())
c = MakeCamelCase('this is a cat')
