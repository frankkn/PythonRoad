#!/usr/bin/env python3

print('customers: What are you serving today?')
s = input('We have ')
items = s.split(',')
menu = {}
for item in items: # ['beef noodles ($100)', ' dumplings ($60)', ' rice ($10)', ' vegetable ($40)', ' tea ($30)', ' juice ($20)']
  food_name = ""
  for c in item:
    if c != '(':
      food_name += c
    else:
      break
  if food_name[0] == ' ':
    food_name = food_name[1:]
  if food_name[-1] == ' ':
    food_name = food_name[:len(food_name)-1]

  price = item.split()[-1]
  price = price[2:len(price)-1]

  menu[food_name] = price
# for i in menu:
#   print(f'{i}:{menu[i]}')

c1 = input('customer1: ').split(', ')
c2 = input('customer2: ').split(', ')
c3 = input('customer3: ').split(', ')
c4 = input('customer4: ').split(', ')
c = [c1, c2, c3, c4]

from collections import defaultdict
order_sheet = defaultdict(int)
total = 0
for c_i in c:
  for food in c_i:
    order_sheet[food] += 1
    total += int(menu[food])
# for i in order_sheet:
#   print(f'{i}:{order_sheet[i]}')

confirm_order = ""
for i in order_sheet:
  confirm_order += i
  confirm_order += " * "
  confirm_order += str(order_sheet[i])
  confirm_order += ", "
confirm_order = confirm_order[:len(confirm_order)-2]
# confirm_order += '.'
print(f'Okay, you ordered {confirm_order}. ${total} in total.')


