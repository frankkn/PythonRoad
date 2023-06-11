#!/usr/bin/env python3
class MyString(str):
  def __lshift__(self,val):
    if len(self) <= 1:
      return self
    if val > len(self):
      val %= len(self)
    new_string = self[:]
    return new_string[val:] + new_string[:val]
  def __rshift__(self,val):
    if len(self) <= 1:
      return self
    if val > len(self):
      val %= len(self)
    new_string = self[:]
    new_string = new_string[len(self)-val:] + new_string[:len(self)-val]
    return new_string

  # def __lshift__(self,val): 
  #   if len(super().__str__()) == 0: 
  #     val = 0 
  #   else: 
  #     val %= len(super().__str__()) 
  #   return MyString(super().__str__()[val:] + super().__str__()[:val])

  # def __rshift__(self,val):
  #   if len(super().__str__()) == 0:
  #     val = 0
  #   else:
  #     val %= len(super().__str__())
  #   return MyString(super().__str__()[-1*val:] + super().__str__()[:-1*val])

# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for i in range(1,T+1):
  s = MyString(input())
  n1,n2 = map(int,input().split())
  print(f'Case #{i}_1: After left rotate {n1} positions the string will be "{s<<n1}"')
  print(f'Case #{i}_2: After right rotate {n2} positions the string will be "{s>>n2}"')
  print(f'Case #{i}_3: The origin string: "{s}"')