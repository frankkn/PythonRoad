#!/usr/bin/env python3
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
  deposit = (int)(input('How much money do you have? '))
  print('')
  while True:
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
        updateDeposit(-1 * list_sum)
        del D[''.join(del_list)] # tranform list into str
      else:
        name, value = del_list[0], del_list[1]
        if int(value) in D[name]:
          updateDeposit(-1 * int(value))
          D[name].remove(int(value))
          if len(D[name]) == 0:
            del D[name]
        else:
          raise ValueError(f'invalid input: {value} not found')
      print('')
    else:
      raise ValueError(f'invalid input: {cmd}')

start()
# if	__name__	==	'__main__':
#   start()

# 1. Support both view or VIEW or ViEw
# 2. Delete one record or all the records of specified name
