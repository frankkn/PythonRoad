table = {
            1:'I',
            4:'IV', 
            5:'V',
            9:'IX',
            10:'X',
            40:'XL',
            50:'L',
            90:'XC',
            100:'C',
            400:'CD',
            500:'D',
            900:'CM',
            1000:'M'
        }

arr = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
t = int(input())
for i in range(1,t+1):
    n = int(input())
    ans = ''
    ind = 0

    while(n > 0):
        while(n >= arr[ind]):
            n -= arr[ind]
            ans += table[arr[ind]]
        ind += 1

    print(f'Case #{i}: {ans}')
