#!/usr/bin/env python3

# slicing operator
L = 'ABCDE'
print(L[-3:]) # CDE
# slicing with step
import string 
str = string.ascii_letters
print(str) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(str[::-1]) # ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba
print(str[::2]) # acegikmoqsuwyACEGIKMOQSUWY
print(str[26:52:3]) # ADGJMPSVY
print(str[51:25:-3]) # ZWTQNKHEB
# slicing in assingment
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
L[1:4] = ['1', '2']
print(L) # ['a', '1', '2', 'e', 'f', 'g']
L[0:0] = ['x', 'y', 'z'] # insert at beginning
print(L) # ['x', 'y', 'z', 'a', '1', '2', 'e', 'f', 'g'] 
L[1:3] = []
print(L) # ['x', 'a', '1', '2', 'e', 'f', 'g']

