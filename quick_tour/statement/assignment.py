T = (a, b, c) = (1, 2, 3)
print(T)

x = 5; y = 3
print('Before swap, x = %d, y = %d' % (x, y))
(x, y) = (y, x)
print('After swap, x = %d, y = %d' % (x, y))