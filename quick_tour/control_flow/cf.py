# for-loop
L = [3, 2, 6, 5]
total = 0
for i in L:
  total += i
print(total)

# if-statement
L = [5, -5, 6, 7, 9, 0,-7]
negatives, positives, zeros = 0, 0, 0
for i in L:
  if i > 0:
    positives += 1
  elif i < 0:
    negatives += 1
  else:
    zeros += 1
print("Positive number:%d, Negative number:%d, Zero:%d" % (positives, negatives, zeros))

# while-loop
password = "ABCDE"
userword = input("Password: ")
while(userword != password):
  userword = input("Wrong password, try again: ")
print("Your password is correct.")