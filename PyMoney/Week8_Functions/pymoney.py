#!/usr/bin/env python3
import sys

def initialize():
  try:
    with open('records.txt', 'r+') as fh:
      try:
        initial_money = int(fh.readline())
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

def add(records):
  name, value = input('Add an expense or income record with description and amount:\n').split()
  if name in records.keys():
    records[name].append(int(value))
  else:
    records[name] = [int(value)]
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
    del_list = input('Which record do you want to delete?\n').split()
    if len(del_list) == 1: # cmd == delete 
      del records[''.join(del_list)] # tranform list into str
    else:
      name, value = del_list[0], del_list[1]
      if int(value) in records[name]:
        records[name].remove(int(value))
        if len(records[name]) == 0:
          del records[name]
      else:
        raise ValueError
  except ValueError:
    sys.stderr.write(f'Invalid input: {value} not found.')
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