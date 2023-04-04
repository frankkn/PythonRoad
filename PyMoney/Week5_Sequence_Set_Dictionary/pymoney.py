#!/usr/bin/env python3
def transform_str_to_list(recordstr):
  records = recordstr.split(', ')
  record_list = []
  for record in records:
    name, value = record.split()
    record_list.append((name, int(value))) # Required step 2
  # print(record_list)
  return record_list

def cal_expense(record_list):
  # Given a record list, sum up all the expense
  expense = 0
  for _,value in record_list:
    expense += value
  return expense

def output(recordstr, deposit):
  '''
  1. Print desired output format of records
  2. Calculate expense from records 
  3. Print the balance
  '''
  print(r"Here's your expense and income records:")
  print('\n'.join(rec for rec in recordstr.split(', ')))
  record_list = transform_str_to_list(recordstr)
  expense = cal_expense(record_list)
  print(f'Now you have {deposit + expense} dollars.')

def cal_balance(recordstr, deposit):
  record_list = transform_str_to_list(recordstr)
  exp = cal_expense(record_list)
  return deposit + exp

deposit = (int)(input('How much money do you have? '))
recordstr = input('Add some expense or income records with description and amount:\n')
output(recordstr, deposit)

if	__name__	==	'__main__':
  assert	cal_balance(recordstr = "breakfast -50, lunch -70, dinner -100, salary 3500", deposit = 1000) \
            ==	4280



