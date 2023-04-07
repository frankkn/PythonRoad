#!/usr/bin/env python3
import sys

def initialize():
  try:
    with open('records.txt', 'r+') as fh:
      try:
        initial_money = int(fh.readline())
        print('Welcome back!')
      except ValueError as err:
        sys.stderr.write(str(err) + '\n')
        fh.truncate(0)
        sys.stdout.write(f'Previous record is not valid.\nStart a new record.\n')
        initial_money = int(input('How much money do you have? '))

      records = {}
      for line in fh.readlines():
        try:
          name, value_str = line.split()
          value_list = value_str.split(',')
          for v in value_list:
            for c in v:
              if not c.isdigit() and c != '-':
                raise ValueError
            if name in records:
              records[name].append(int(v))
            else:
              records[name] = [int(v)]
        except ValueError:
          sys.stderr.write(f'Found invalid record format: {name} {v}\nStart a new record.\n')
          initial_money = int(input('How much money do you have? '))
          fh.truncate(0)
  except FileNotFoundError:
    # sys.stderr.write(str(err) + '\n')
    records = {}
    sys.stdout.write("Previous record is not found.\nStart a new record.\n")
    while True:
      try:
        initial_money = int(input('How much money do you have? '))
        break
      except ValueError as err:
        sys.stderr.write(str(err) + '\n' + 'Please enter an interger.\n')
  except PermissionError as err:
    sys.stderr.write(str(err) + '\n' + 'Permission denied. Please check file permissions.\n')
    initial_money = 0
    records = {}
  finally:
    return initial_money, records

def calMoney(initial_money, records):
  money = initial_money
  for v in records.values():
    if isinstance(v, int):
      money += v
    else: 
      for i in v:
        money += i
  return money

def is_int(string):
  try:
    num = int(string)
    return True
  except ValueError:
    return False

def add(records):
  while True:
    try:
      name, value = input('Add an expense or income record with description and amount:\n').split()
      value = int(value)
      if name in records.keys():
        records[name].append(value)
      else:
        records[name] = [value]
      break
    except ValueError as err:
      sys.stderr.write(str(err) + '\n' + 'Try again.\n')
  return records

def view(initial_money, records):
  print("Here's your expense and income records:")
  print("%-20s %s" % ("Desciption", "Amount")) # left-aligned
  print("="*20 +  " " + "=" * 6)
  for name, values in records.items():
    print(f'{name:<20s}', end = " ")
    print(f"{','.join(str(i) for i in values).lstrip('[').rstrip(']')}")
  print("="*20 +  " " + "=" * 6)
  print(f'Now you have {calMoney(initial_money, records)} dollars.')

def delete(records):
  try:
    del_cmd = input('Which record do you want to delete?\n').split()
    if len(del_cmd) == 1: # del_cmd == breakfast
      try:
        if del_cmd in records:
          del records[''.join(del_cmd)] # tranform list into str
      except:    
        sys.stderr.write(f'Invalid input: {del_cmd} not found.\n') # (1)delete (2)ff
        
    elif len(del_cmd) == 2:
      try:
        name, value = del_cmd[0], del_cmd[1]
        if int(value) in records[name]:
          records[name].remove(int(value))
          if len(records[name]) == 0:
            del records[name]
        else:
          raise ValueError
      except ValueError:
        if is_int(value):
          sys.stderr.write(f'Value: {value} not found for {name}.\n') # (1)delete (2)b -999
        else:
          sys.stderr.write(f'Invalid Value: {value}.\n') # (1)delete (2)b c
    else:
      raise ValueError

  except ValueError:
    sys.stderr.write(f'Invalid delete format.\n') # e.g. (1)delete (2)a b c
  finally:
    return records

def save(initial_money, records):
  with open('records.txt', mode = 'w') as fh:
    fh.write(str(initial_money) + '\n')
    for name, values in records.items():
      if isinstance(values, int):
        fh.write(name + ' ' + str(values) + '\n')
      else:
        value_str = ','.join(str(v) for v in values)
        fh.write(name + ' ' + value_str + '\n')

# The 5 function definitions here
 
initial_money, records = initialize()
while True:
  command = input('\nWhat do you want to do (add / view / delete / exit)? ')
  if command == 'add':
    records = add(records)
  elif command == 'view':
    view(initial_money, records)
  elif command == 'delete':
    records = delete(records)
  elif command == 'exit':
    save(initial_money, records)
    break
  else:
    sys.stderr.write(f'Invalid command {command}. Try again.\n')