T = int(input())
for t in range(T):
    excel = input()
    num = 0
    for c in excel:
        num = num*26 + (ord(c) - ord('A') + 1)
    print(f'Case #{t+1}: {num}')