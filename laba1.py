from math import sqrt

a, b, c = int(input()), int(input()), int(input())

D = b**2 - 4*a*c

if D > 0:
    x1 = (-b + sqrt(D)) / 2*a
    x2 = (-b - sqrt(D)) / 2*a
    print(x1)
    print(x2)
elif D == 0:
    x1 = -b / 2*a
    print(x1)
else: print('Корней нет')