#!/usr/bin/env python3

s = set('hello')
# set literal
s = {1,2,3,4,5}

# Set members must be immutable
# Incorrect sets
# s = {[1,2], [3,4]}
# s ={{(1,2,3)}, {4,5}}

# Set comprehension
{chr(65+i) for i in range(5)\
  if chr(i) not in ['A','E','I','O','U']}
{2**i for i in range(1,11)\
  if 2**i <= 1000}

# Set operators
# -, |, &, ^
# Set comparison operators
# >, >=, <, <=, ==, !=




