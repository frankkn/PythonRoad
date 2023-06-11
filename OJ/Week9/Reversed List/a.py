#!/usr/bin/env python3
# def reverse(L):
#   ans = []
#   for i in range(len(L)):
#     if type(L[i]) == list:
#       ans.append(reverse(L[i]))
#     else:
#       ans.append(L[i])
#   return list(reversed(ans))

def reverse(L):
  ans = []
  for i in L:
    if type(i) == list:
      ans.append(reverse(i))
    else:
      ans.append(i)
  return list(reversed(ans))

# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(T):
    L = eval(input())
    rL = reverse(L)
    print(L)
    print(rL)