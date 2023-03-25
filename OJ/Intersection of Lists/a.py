#!/usr/bin/env python3
t = int(input())

for testcase in range(1, t+1):
  list1 = input().split()
  set1 = set([int(i) for i in list1])
  # print(f'set1: {set1}')
  list2 = input().split()
  set2 = set([int(i) for i in list2])
  # print(f'set2: {set2}')

  if set1 < set2:
    set3 = [i for i in set1 if i in set2 ]
  else:
    set3 = [i for i in set2 if i in set1 ]
  
  print(f'Case #{testcase}: {sorted(set3)}')