#!/usr/bin/env python3

int_to_str_month ={
  1:'January',
  2:'Feburuary',
  3:'March',
  4:'April',
  5:'May',
  6:'June',
  7:'July',
  8:'August',
  9:'September',
  10:'October',
  11:'November',
  12:'December'
}

def leap(year):
    return year % 400 == 0 or \
        year % 4 == 0 and year % 100 != 0

def DaysInMonthTear(month, year):
  return 31 if month in {1, 3, 5, 7, 8, 10, 12} else \
      30 if month in {4, 6, 9, 11} else \
      28 if not leap(year) else \
      29 

while True:
  s = input('enter date in mm/dd/yyyy: ')
  if s == 'quit':
    break
  else:
    input_list = s.split('/')

    month = int(input_list[0])
    str_month = ''
    if month >= 0 and month <= 12:
      str_month = int_to_str_month[month]
    else:
      print(f'Invalid month {month}: should be between 01 and 12')
      continue

    day = int(input_list[1])
    year = int(input_list[2])
    valid_day = DaysInMonthTear(month, year)
    if not (day >= 0 and day <= valid_day):
      if month == 2:
        print(f'Invalid day {day} for {str_month}: not a leap year')
      else:
        print(f'Invalid day {day} for {str_month}: should be between 01..{valid_day}')
      continue

    print(f'{str_month} {day}, {year}')
print('bye')