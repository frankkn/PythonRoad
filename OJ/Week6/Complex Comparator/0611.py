t = int(input())
for i in range(1,t+1):
    x,y = input().split()
    x = complex(x)
    y = complex(y)
    a = x.real
    b = x.imag
    c = y.real
    d = y.imag
    if a > c and b > d:
        print(f'Case #{i}: {x} > {y}')
    elif a < c and b < d:
        print(f'Case #{i}: {x} < {y}')
    elif a == c and b == d:
        print(f'Case #{i}: {x} == {y}')
    elif a == c or b == d:
        if b > d or a > c:
            print(f'Case #{i}: {x} >= {y}')
        elif b < d or a < c:
            print(f'Case #{i}: {x} <= {y}')
    else:
        print(f'Case #{i}: {x} != {y}')
