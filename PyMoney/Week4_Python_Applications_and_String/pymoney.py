#!/usr/bin/env python3

deposit = (int)(input('How much money do you have? '))
record = input('Add an expense or income record with description and amount:\n').split(' ')
expense = (int)(record[1])
# print('Now you have %d dollars.' % (deposit + expense))
print(f'Now you have {deposit + expense} dollars.')
