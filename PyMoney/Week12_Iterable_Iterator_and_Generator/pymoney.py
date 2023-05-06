#!/usr/bin/env python3
import sys

class Record:
  """
  Represent a record.
  """
  def __init__(self, category, item, amount):
    """
    Initialize the record object's attributes.
    """
    self._category = category
    self._item = item
    self._amount = amount

  @property
  def category(self):
    return self._category

  @property
  def item(self):
    return self._item

  @property
  def money(self):
    return self._amount

class Records:
  """
  Maintain a list of all the 'Record's and the initial amount of money.
  """
  def __init__(self):
    """
    Initialize the program by reading records from records.txt and set the initial amount of money.
    """
    try:
      with open('records.txt', 'r+') as fh:
        try:
          self._initial_money = int(fh.readline())
          print('Welcome back!')
        except ValueError as err:
          fh.truncate(0)
          sys.stderr.write(str(err) + '\n')
          sys.stdout.write('Previous record is not valid.\nStart a new record.\n')
          self._initial_money = int(input('How much money do you have? '))

        self._records = [] # _records = ['category item amount', 'category item amount', ...]
        for line in fh.readlines():
          try:
            L = line.split()
            cate, item, amount = L[0], L[1], L[2]
            new_record = Record(cate, item, amount)
            self._records.append(new_record)
          except ValueError:
            fh.truncate(0)
            sys.stderr.write(f'Found invalid record format\nStart a new record.\n')
            self._initial_money = int(input('How much money do you have? '))

    except FileNotFoundError:
      self._records = []
      sys.stdout.write("Previous record is not found.\nStart a new record.\n")
      while True:
        try:
          self._initial_money = int(input('How much money do you have? '))
          break
        except ValueError as err:
          sys.stderr.write(str(err) + '\n' + 'Please enter an interger.\n')
    except PermissionError as err:
      sys.stderr.write(str(err) + '\n' + 'Permission denied. Please check file permissions.\n')
      self._initial_money = 0
      self._records = []
 
  def add(self, record, catogories):
    """
    Add a new record to the list.
    Usage: [category] [item] [amount]
    """
    while True:
      try:
        category, item, amount = record.split()
        try:
          amount = int(amount)
        except ValueError as err: 
          sys.stderr.write(str(err) + '\n' + 'Try again.\n')
        
        if categories.is_category_valid(category):
          new_record = Record(category, item, amount)
          self._records.append(new_record)
          break
        else:
          print('The specified category is not in the category list.')
          print('You can check the category list by command "view categories".')
          print('Fail to add a record.')
          break
      except ValueError as err:
        sys.stderr.write(str(err) + '\n' + 'Try again.\n')
        record = input('Add an expense or income record with category, description, and amount (separate by spaces):\n')
        self.add(record, categories)


  def view(self):
    """
    Print all the records and report the balance.
    """
    print("Here's your expense and income records:")
    print("%-20s %-20s %s" % ("Category", "Desciption", "Amount")) # left-aligned
    print("="*20 + " " + "="*20 +  " " + "=" * 6)
    total = self._initial_money
    line_no = 0
    for each_rec in self._records:
      cate, item, amount = each_rec._category, each_rec._item, each_rec._amount
      total += int(amount)
      line_no += 1
      print(f'{line_no:>2}.{cate:<17s} {item:<20s} {amount}')
    print("="*20 + " " + "="*20 + " " + "="*6)
    print(f'Now you have {total} dollars.')

  def delete(self, record):
    """
    Delete one or more records from the list.
    Usage(for one record): [category] [item] [amount].
    Usage(for multiple record): * [line_no].
    Usage(for category or item): [category/item] [category_name/item_name].
    """
    del_rec = record.split() # record = 'meal breakfast -50'
    try:
      if del_rec[0] == '*':
        if len(del_rec) <= 1:
          raise Exception
        del_list = sorted(list(map(int, del_rec[1:])))
        del_rec = []
        for no in del_list:
          for i, v in  enumerate(self._records):
            if i+1 == no:
              del_rec.append(v)
        self._records = list(filter(lambda x:x not in del_rec, self._records))
      elif len(del_rec) == 3:
        cate, name, amount = del_rec[0], del_rec[1], del_rec[2]
        for i, v in enumerate(self._records):
          if cate == v._category and name == v._item and amount == v._amount:
            self._records.remove(v)
      elif len(del_rec) == 2: # record = 'category meal' or record = 'item breakfast'
        col, name = del_rec[0], del_rec[1]
        if col not in dir(Record):
          raise Exception
        else:
          self._records = [rec for rec in self._records if rec.__dict__['_'+col] != name]
      else:
        raise Exception
    except:
      sys.stderr.write('Invalid input. Try again!\n')
      sys.stderr.write('Usage(for one record): [category] [item] [amount].\n')
      sys.stderr.write('Example: meal breakfast -50\n')
      sys.stderr.write('Usage(for multiple record): * [line_no].\n')
      sys.stderr.write('Example: * 1 3 5\n')
      sys.stderr.write('Usage(for category or item): [category/item] [category_name/item_name].\n')
      sys.stderr.write('Example: category meal or item breakfast\n')
 
  def revise(self, line_no, revise_record):
    """
    Revise a record from the list.
    Usage: Enter line_no , then enter [category] [item] [amount]
    """
    category, item, amount= revise_record.split()
    for i, v in enumerate(self._records):
      if i+1 == int(line_no):
        v._category = category
        v._item = item
        v._amount = amount
        break

  def find(self, target_categories):
    """
    Print all records in the specified category or in a subcategory under that one.
    """
    L = list(filter(lambda x: x._category in target_categories, self._records))
    print(f'Here\'s your expense and income records under category "{category}":')
    print("%-20s %-20s %s" % ("Category", "Desciption", "Amount")) # left-aligned
    print("=" * 20 + " " + "=" * 20 +  " " + "=" * 6)
    total = 0
    line_no = 0
    for each_rec in L:
      cate, item, amount = each_rec._category, each_rec._item, each_rec._amount
      total += int(amount)
      line_no += 1
      print(f'{line_no:>2}.{cate:<17s} {item:<20s} {amount}')
    print("="*20 + " " + "="*20 + " " + "="*6)
    print(f'The total amount above is {total}.')

  def save(self):
    """
    Save records to records.txt.
    """
    with open('records.txt', mode = 'w') as fh:
      fh.write(str(self._initial_money) + '\n')
      for rec in self._records:
        s = rec._category + " " + rec._item + " " + str(rec._amount)
        fh.write(s + '\n')

class Categories:
  """
  Maintain the category list and provide some methods.
  """
  def __init__(self):
    """
    Initialize predefined list of categories.
    """
    self._categories = ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', ['bus','railway']], \
                        'income', ['salary', 'bonus']]
 
  def view(self):
    """
    Print all the provided categories hierarchically.
    """
    def view_category(category, level = 0):
      if category == None:
        return
      if type(category) in {list, tuple}:
        for child in category:
          view_category(child, level + 1)
      else:
        print(f'{" " * 2 * level}- {category}')
    view_category(self._categories)

  def is_category_valid(self, test_category):
    """
    Check whether given category is in predefined categories.
    """
    def valid(categories, test_category):
      if type(categories) in {list, tuple}:
        for child in categories:
          if valid(child, test_category):
            return True
        return False
      return categories == test_category
    return valid(self._categories, test_category)
 
  def find_subcategories(self, category):
    """
    Find the target category and flatten the subcategories under it.
    """
    def find_subcategories_gen(category, categories, found = False):
      if type(categories) == list: # recursive case
        for index, child in enumerate(categories):
          yield from find_subcategories_gen(category, child, True)
          if child == category and index + 1 < len(categories) \
              and type(categories[index + 1]) == list:
              # When the target category is found,
              # recursively call this generator on the subcategories
              # with the flag set as True.
              yield from find_subcategories_gen(category, categories[index+1], True)
      else: # base case
        if categories == category or found == True:
          yield categories
    return list(find_subcategories_gen(category, self._categories))

# class definitions here

if __name__ == '__main__':

  categories = Categories()
  records = Records()
  
  while True:
    command = input('\nWhat do you want to do (add / view / delete / revise / view categories / find / exit)? ')
    if command == 'add':
      record = input('Add an expense or income record with category, item, and amount (separate by spaces):\n')
      records.add(record, categories)
    elif command == 'view':
      records.view()
    elif command == 'delete':
      delete_record = input("Which record do you want to delete? ")
      records.delete(delete_record)
    elif command == 'revise':
      line_no = input("Which record do you want to delete? (Enter line number)\n")
      revise_record = input('Enter revised expense or income record with category, item, and amount (separate by spaces):\n')
      records.revise(line_no, revise_record)
    elif command == 'view categories':
      categories.view()
    elif command == 'find':
      category = input('Which category do you want to find? ')
      target_categories = categories.find_subcategories(category)
      records.find(target_categories)
    elif command == 'exit':
      records.save()
      break
    else:
      sys.stderr.write('Invalid command. Try again.\n')