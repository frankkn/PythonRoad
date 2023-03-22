#!/usr/bin/env python3
t = int(input())

dict ={
  1:'I', 
  5:'V',
  10:'X',
  50:'L',
  100:'C',
  500:'D',
  1000:'M',
  5000:'G',
  10000:'H'
}

for testcase in range(1, t+1):
  num = int(input())
  i = 1
  while num >= i: # Watch out >= instead of >
    i *= 10
  i /= 10

  roman = ''
  while num:
    last_digit = int(num // i)
    num %= i
    if last_digit <= 3:
      roman += dict[i]*last_digit
    elif last_digit == 4:
      roman += dict[i]
      roman += dict[i*5]
    elif 5 <= last_digit <= 8:
      roman += dict[i*5]
      roman += dict[i]*(last_digit-5)
    elif last_digit == 9:
      roman += dict[i]
      roman += dict[i*10]
    i /= 10

  print(f'Case #{testcase}: {roman}')