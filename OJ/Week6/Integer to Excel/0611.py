t = int(input())
for i in range(1,t+1):
    n = int(input())
    ans = ''
    while n > 0:
        n = n-1
        ans = chr(ord('A') + n%26) + ans
        n //= 26
    print(f'Case #{i}: {ans}')