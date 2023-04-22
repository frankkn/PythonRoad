#!/usr/bin/env python3

def check():
  start = int(input())
  interval = int(input())
  sending = int(input())

  for i in range(3):
    start += interval
    if start >= sending:
      print(f'{start}')
      return
  print('Who knows...')

if __name__ == '__main__':
  check()