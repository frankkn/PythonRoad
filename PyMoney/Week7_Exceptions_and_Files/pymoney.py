#!/usr/bin/env python3
import sys

D = {}
deposit = 0

def updateDeposit(*values):
  global deposit
  for v in values:
    if isinstance(v, int):
      deposit += v
    else: 
      for i in v:
        deposit += i

def start():
  global D
  global deposit 
  # deposit = (int)(input('How much money do you have? '))
  print('')
  while True:
    try:
      cmd = input('What do you want to do (add / view / delete / exit)?: ').lower() # accept both VIEW or view
      if cmd == 'exit':
        break
      elif cmd == 'add':
        name, value = input('Add an expense or income record with description and amount:\n').split()
        if name in D.keys():
          D[name].append(int(value))
        else:
          D[name] = [int(value)]
        updateDeposit(int(value))
        print('')
      elif cmd == 'view':
        print("Here's your expense and income records:\n")
        print("%-20s %s" % ("Desciption", "Amount")) # left-aligned
        print("="*20 +  " " + "=" * 6)
        for name, values in D.items():
          print(f'{name:<20s}', end = " ")
          print(f"{','.join(str(i) for i in values).lstrip('[').rstrip(']')}")
        print("="*20 +  " " + "=" * 6)
        print(f'Now you have {deposit} dollars.')
        print('')
      elif cmd == 'delete':
        del_list = input('Which record do you want to delete?\n').split()
        # Enter name + amount to delete one record or name to delete all of records relating to name  
        if len(del_list) == 1:
          list_sum = sum(D[''.join(del_list)])
          print(f'Deposit before delete: {deposit}')
          updateDeposit(-1 * list_sum)
          print(f'Deposit after delete : {deposit}')
          del D[''.join(del_list)] # tranform list into str
        else:
          name, value = del_list[0], del_list[1]
          if int(value) in D[name]:
            print(f'Deposit before delete: {deposit}')
            updateDeposit(-1 * int(value))
            print(f'Deposit after delete : {deposit}')
            D[name].remove(int(value))
            if len(D[name]) == 0:
              del D[name]
          else:
            raise ValueError(f'invalid input: {value} not found')
        print('')
      else:
        raise ValueError(f'Invalid command: {cmd}')
    except ValueError as err:
      sys.stderr.write(str(err) + ". " + 'Try again.\n')
try:
  with open('records.txt', 'r+') as fh:
    try:
      deposit = int(fh.readline())
      sys.stdout.write(f'Your current deposit is: {deposit}.')
    except ValueError as err:
      sys.stderr.write(str(err) + '\n')
      fh.truncate(0)
      sys.stdout.write(f'Previous record is not valid.\nStart a new record.\n')
      deposit = int(input('How much money do you have? '))

    for line in fh.readlines():
      try:
        name, value_str = line.split()
        value_list = value_str.split(',')
        for v in value_list:
          for c in v:
            if not c.isdigit() and c != '-':
              raise ValueError
          if name in D:
            D[name].append(int(v))
          else:
            D[name] = [int(v)]
      except ValueError:
        sys.stderr.write(f'Found invalid record format: {name} {v}\nStart a new record.\n')
        deposit = int(input('How much money do you have? '))
        fh.truncate(0)
except FileNotFoundError:
  # sys.stderr.write(str(err) + '\n')
  sys.stdout.write("Previous record is not found.\nStart a new record.\n")
  while True:
    try:
      deposit = int(input('How much money do you have? '))
      break
    except ValueError as err:
      sys.stderr.write(str(err) + '\n' + 'Please enter an interger.\n')


start()

with open('records.txt', mode = 'w') as fh:
  fh.write(str(deposit) + '\n')
  for name, values in D.items():
    if isinstance(values, int):
      fh.write(name + ' ' + str(values) + '\n')
    else:
      value_str = ','.join(str(v) for v in values)
      fh.write(name + ' ' + value_str + '\n')

# if	__name__	==	'__main__':
#   start()

# 1. Support both view or VIEW or ViEw
# 2. Delete one record or all the records of specified name
