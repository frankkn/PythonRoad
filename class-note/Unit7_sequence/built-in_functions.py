#!/usr/bin/env python3

# min(), max(), sum()
s = [1,5,3,2,8]
print(sum(s)) # 19
print(max('ABCDE')) # 'E'

# any(): return True if any element is True
# all(): return True if all elements are True

# sorted(): makes a copy of the same type of data structure but with elements in sorted order
s = [1, 5, 3, 2, 8]
print(sorted(s)) # create a new list [1, 2, 3, 5, 8]
print(s) # [1, 5, 3, 2, 8]
# reversed(): makes an iterator with elements in reverse order
s = [1, 5, 3, 2, 8]
print(reversed(s)) # <list_reverseiterator object at 0x7f0bb6047310>
print(list(reversed(s))) # [8, 2, 3, 5, 1]

