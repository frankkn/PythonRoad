#!/usr/bin/env python3
import sys

def initialize():
  """
  Initializes the program by reading records from a file and setting the initial amount of money.
  If the records.txt file exists and is valid, it reads the initial amount of money and records from the file.
  If the records.txt file does not exist or is invalid, it prompts the user to enter the initial amount of money and starts a new record.
  If the records.txt file has invalid records, it truncates the file and starts a new record.
  
  :return: A tuple containing the initial amount of money, the records dictionary, and the category-description dictionary.
  """
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
  """
  Calculates the total amount of money based on the initial amount of money and the records dictionary.
  
  :param initial_money: The initial amount of money.
  :param records: A dictionary containing the records.
  :return: The total amount of money.
  """
  money = initial_money
  for v in records.values():
    if isinstance(v, int):
      money += v
    else: 
      for i in v:
        money += i
  return money

def is_int(string):
  """
  Checks if a given string can be converted to an integer.
  
  :param string: The string to check.
  :return: True if the string can be converted to an integer, False otherwise.
  """
  try:
    num = int(string)
    return True
  except ValueError:
    return False

def add(categories, CD, records):
  """
  Adds a record to the records dictionary and the category-description dictionary.
  It prompts the user to enter the category, description, and amount of the record.
  If the category is valid, it adds the record to the dictionaries.
  
  :param categories: A list of valid categories.
  :param CD: A dictionary containing the category-description pairs.
  :param records: A dictionary containing the records.
  :return: The updated category-description dictionary and records dictionary.
  """
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
  """
  Displays the records in a formatted table.
  
  :param initial_money: The initial amount of money.
  :param CD: A dictionary containing the category-description pairs.
  :param records: A dictionary containing the records.
  :return: None.
  """
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
  """
  Deletes a record from the records dictionary and the category-description dictionary.
  It prompts the user to enter the record to delete.
  If the record exists, it deletes it from the dictionaries.
  
  :param CD: A dictionary containing the category-description pairs.
  :param records: A dictionary containing the records.
  :return: The updated category-description dictionary and records dictionary.
  """
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
  """
  Saves the current records to a file called "records.txt".
  The file includes the initial amount of money, as well as all records.

  :param initial_money: The initial amount of money.
  :param CD: A dictionary containing the category-description pairs.
  :param records: A dictionary containing the records.
  :return: None
  """
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
  """
  Initializes and returns a nested list of categories containing the categories of expenses and income, along with their respective subcategories.

  :return: A nested list of categories
  """
  categories = ['expense', 
                  ['food', ['meal', 'snack', 'drink'], 
                'transportation', 
                  ['bus', 'railway']], 
                'income', 
                  ['salary', 'bonus']]
  return categories

def view_categories(categories, level=0):
  """
  Recursively prints the categories passed as a nested list, along with their subcategories, with proper indentation.

  :param categories: A nested list of categories
  :param level: The indentation level (default 0)
  :return: None
  """
  if categories == None:
    return
  if type(categories) in {list, tuple}:
    for child in categories:
      view_categories(child, level+1)
  else:
    print(f'{" " * 2 * level}- {categories}')

def is_category_valid(category, categories):
  """
  Returns True if the given category is present in the nested list of categories, else returns False.

  :param category: The category to search for
  :param categories: A nested list of categories
  :return: True if category is found, False otherwise
  """
  if type(categories) in {list, tuple}:
    for child in categories:
      if is_category_valid(category, child):
        return True
    return False
  return category == categories

def find(CD, records, categories):
  """
  Asks the user to input a category name to search for and calls the find_subcategories() function to search for the category and its subcategories.

  :return: None
  """
  cate = input('Which category do you want to find?\n')
  print(find_subcategories(cate, categories))

  L = list(filter(lambda x: x in CD.keys(), find_subcategories(cate, categories)))

  print(f"Here's your expense and income records under category {cate}:")
  print("%-15s %-20s %s" % ("Category", "Desciption", "Amount")) # left-aligned
  print("="*15 + " " + "="*20 +  " " + "=" * 6)
  total = 0
  for each_cate in L:
    for each_des in CD[each_cate]:
      print(f'{each_cate:<15s}', end = " ")
      print(f'{each_des:<20s}', end = " ")
      print(f"{','.join(map(str, records[each_des])).lstrip('[').rstrip(']')}")
      total += sum(map(int, records[each_des]))
  print("="*15 + " " + "="*20 + " " + "="*6)
  print(f'The total amount above is {total}.')

def find_subcategories(category, categories):
  """
  Recursively searches for the given category in the nested list of categories and returns the category along with its subcategories, if found.

  :param category: The category to search for
  :param categories: A nested list of categories
  :return: A list containing the category and its subcategories, if found. Otherwise, returns True if the category is found but has no subcategories or returns an empty list if not found.
  """
  if type(categories) == list:
    for v in categories:
      p = find_subcategories(category, v)
      if p == True:
        index = categories.index(v)
        if index + 1 < len(categories) and \
            type(categories[index + 1]) == list: # the target category does not have subcategories
          return flatten(categories[index:index + 2])
        else:
          # return only itself if no subcategories
          return [v]
      if p != []:
        return p
  return True if categories == category else [] # return [] instead of False if not found

def flatten(L):
  if type(L) == list:
    result = []
    for child in L:
      result.extend(flatten(child))
    return result
  else:
    return [L]

# The 5 function definitions here
if __name__ == '__main__':
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
    elif command == 'find':
      find(CD, records, categories)
    elif command == 'exit':
      save(initial_money, CD, records)
      break
    else:
      sys.stderr.write(f'Invalid command {command}. Try again.\n')