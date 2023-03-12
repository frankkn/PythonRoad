#!/usr/bin/env python3

d2 = {'one':1, 'two':2, 'three':3}
d3 = dict([('one', 1), ('two', 2), ('three', 3)])
d4 = {i: 2**i for i in range(1, 11)}

# "safely" lookup
ec = {'one':1, 'two':2, 'three':3}
ec.get('two') # 2
print(ec.get('four')) # None

# keys()
# values()
# items()

# d1.update(d2)
e1 = {'one':'一', 'dog':'狗'}
e2 = {'two':'二', 'dog':'犬'}
e1.update(e2)
print(e1) # {'one': '一', 'dog': '犬', 'two': '二'}

# copy(): shallow copy
e1 = {'one':'一', 'two':'二'}
e2 = e1.copy()
del e1['one']
print(e1) # {'two': '二'}
print(e2) # {'one': '一', 'two': '二'}

# %-style string formatting with dictionaries
D = {'lastname': 'Lee', 'firstname':'Mary', 'phone':'123-4567'}
print('name: %s %s, phone: %s' % (D['firstname'],D['lastname'],D['phone']))
print('name: %(firstname)s %(lastname)s, phone: %(phone)s' % D)

