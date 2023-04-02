# Lists: mutable

L = [1,2,3]
print(L[0]) 

L[1] = "Hi" 
print(L) 

L + [6,7,8]
print(L) # [1, "Hi", 3] !!

# Tuple: immutable(read-only)

T = (12, 34, 56)
print(T[2])

U = 78,90,12
print(U)

V = 34,
print(V)



# Dictionary: unordered

d = {"Jan":1, "Feb":2, "Mar":3}
print(d["Feb"])

d["Apr"] = 4
print(d)

# Set: unordered

A = {1, 2, 3}; B = {1, 3, 5}; C = {2, 4, 6}
# print(A & B)
# print(A | C)
print(A - B)
print(A ^ B) # 有哪些值在一個(A或B)，但不是在兩個(A跟B)裡面。

