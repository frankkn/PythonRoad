from re import search

def is_strong(passwd):
  crit1 = len(passwd) >= 8
  crit2 = search(r'[a-z]', passwd) != None
  crit3 = search(r'[A-Z]', passwd) != None
  crit4 = search(r'[0-9]', passwd) != None
  crit5 = search(r'[-!@#$%^&*()+]', passwd) != None
  crit6 = search(r'(.)\1', passwd) == None
  return crit1 and crit2 and crit3 and crit4 and crit5 and crit6

T = int(input())
for t in range(T):
  passwd = input()
  if is_strong(passwd):
    print('Strong')
  else:
    print('Weak')