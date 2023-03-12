#!/usr/bin/env python3

str = input('Enter a sentance: ')
banned_list = input('Enter prohibited list: ')
print(list(i for i in str if i not in banned_list))

