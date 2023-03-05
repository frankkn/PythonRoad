s1 = input('Enter a string: ')
s2 = input('Enter another string: ')

if(len(s1) < len(s2)):
  print('Shorter string: %s (length %d)' % (s1, len(s1)))
  print('Longer string: %s (length %d)' % (s2, len(s2)))
elif(len(s2) < len(s1)):
  print('Shorter string: %s (length %d)' % (s2, len(s2)))
  print('Longer string: %s (length %d)' % (s1, len(s1)))
else:
  print('First string: %s (length %d)' % (s1, len(s1)))
  print('Second string: %s (length %d)' % (s2, len(s2)))