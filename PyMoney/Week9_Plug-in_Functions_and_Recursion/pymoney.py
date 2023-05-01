#!/usr/bin/env python3
import sys

def initialize():
  CD = {} # Cateogory - Description
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
          cate, name, value_str = line.split()
          value_list = value_str.split(',') # [-50,-60,-70]
          if cate in CD.keys():
            if name not in CD[cate]: # Redundant?
              CD[cate].append(name)
          else:
            CD[cate] = [name]

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
    return initial_money, records, CD

def cal_money(initial_money, records):
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

def add(categories, CD, records):
  while True:
    try:
      cate, name, value = input('Add an expense or income record with category, description, and amount (separate by spaces):\n').split()
      value = int(value)
      if is_category_valid(cate, categories):
        if cate in CD.keys():
          if name not in CD[cate]:
            CD[cate].append(name)
        else:
          CD[cate] = [name]
        if name in records.keys():
          records[name].append(value)
        else:
          records[name] = [value]
        break
      else:
        print('The specified category is not in the category list.')
        print('You can check the category list by command "view categories.')
        print('Fail to add a record.')
        break
    except ValueError as err:
      sys.stderr.write(str(err) + '\n' + 'Try again.\n')
  return CD, records

def view(initial_money, CD, records):
  print("Here's your expense and income records:")
  print("%-15s %-20s %s" % ("Category", "Desciption", "Amount")) # left-aligned
  print("="*15 + " " + "="*20 +  " " + "=" * 6)
  for cate in CD.keys():
    for name in CD[cate]:
      print(f'{cate:<15s}', end = " ")
      print(f'{name:<20s}', end = " ")
      print(f"{','.join(str(i) for i in records[name]).lstrip('[').rstrip(']')}")
  print("="*15 + " " + "="*20 + " " + "="*6)
  print(f'Now you have {cal_money(initial_money, records)} dollars.')

def delete(CD, records):
  try:
    del_cmd = input('Which record do you want to delete?\n').split()
    if len(del_cmd) == 2: # del_cmd == meal breakfast
      cate, name = del_cmd[0], del_cmd[1]
      try:
        if name in records.keys() and cate in CD.keys():
          del records[name]
          del CD[cate]
      except:
        sys.stderr.write(f'Invalid input: {del_cmd} not found.\n') # (1)delete (2)ff  
    elif len(del_cmd) == 3: # del_cmd == meal breakfast -50
      try:
        cate, name, value = del_cmd[0], del_cmd[1], del_cmd[2]
        if int(value) in records[name] and name in CD[cate]:
          records[name].remove(int(value))
          if len(records[name]) == 0:
            del records[name]
            CD[cate].remove(name)
            if len(CD[cate]) == 0:
              del CD[cate]
            
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
    return CD, records

def save(initial_money, CD, records):
  with open('records.txt', mode = 'w') as fh:
    fh.write(str(initial_money) + '\n')
    for cate in CD.keys(): # meal
      for name in CD[cate]: # breakfast -> lunch
        # for values in records[name]:
        # if len(records[name]) == 1:
        #   # if isinstance(values, int):
        #   fh.write(cate + ' ' + name + ' ' + records[name] + '\n')
        # else:
        value_str = ','.join(map(str, records[name]))
        fh.write(cate + ' ' + name + ' ' + value_str + '\n')

def initialize_categories():
  categories = ['expense', 
                  ['food', ['meal', 'snack', 'drink'], 
                'transportation', 
                  ['bus', 'railway']], 
                'income', 
                  ['salary', 'bonus']]
  return categories

def view_categories(categories, level=0):
  if categories == None:
    return
  if type(categories) in {list, tuple}:
    for child in categories:
      view_categories(child, level+1)
  else:
    print(f'{" " * 2 * level}- {categories}')

def is_category_valid(category, categories):
  if type(categories) in {list, tuple}:
    for child in categories:
      if is_category_valid(category, child):
        return True
    return False
  return category == categories

def find():
  cate = input('Which category do you want to find?\n')
  
# The 5 function definitions here
 
initial_money, records, CD = initialize()
categories = initialize_categories()
while True:
  command = input('\nWhat do you want to do (add / view / delete / view categories / find / exit)? ')
  if command == 'add':
    CD, records = add(categories, CD, records)
  elif command == 'view':
    view(initial_money, CD, records)
  elif command == 'delete':
    CD, records = delete(CD, records)
  elif command == 'view categories':
    view_categories(categories)  
  elif command == 'exit':
    save(initial_money, CD, records)
    break
  else:
    sys.stderr.write(f'Invalid command {command}. Try again.\n')