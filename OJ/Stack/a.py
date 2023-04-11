#!/usr/bin/env python3
st = None
squ_sum = 0

def init():
  global st
  global squ_sum
  st = []
  squ_sum = 0
  return None

def push(val):
  global st
  global squ_sum
  st.append(val)
  squ_sum += val**2
  return None

def pop():
  global st
  global squ_sum
  v = st.pop()
  squ_sum -= v**2
  return None

def top():
  global st
  return st[-1]

def getSquareSum():
  global squ_sum
  return squ_sum


