#!/usr/bin/env python3

#!/usr/bin/env python3
t = int(input())

for testcase in range(1, t+1):
    L = list(map(int, input().split()))
    flag = True
    for i in range(len(L)//2):
        if L[i] != L[len(L)-i-1]: 
            flag = False
            break
    ans = "Yes" if flag else "No"    
    print(f'Case #{testcase}: {ans}')