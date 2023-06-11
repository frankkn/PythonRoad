#!/usr/bin/env python3
t = int(input())

for testcase in range(1, t+1):
    num = int(input())
    msb = num >> 7      
    num &= ((1<<7)-1)
    num <<= 1
    num |= msb
    print(f'Case #{testcase}: {num}')