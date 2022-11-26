import math
print('Введіть а:')
a = float(input())
print('Введіть b:')
b = float(input())
print('Введіть c:')
c = float(input())
D = (b**2) - (4 * a * c)
if D < 0:
    print('Рівняння коренів немає')
else:
    Dsqrt = math.sqrt(D)
    x1 = ((-b) - Dsqrt) / (2 * a )
    print(x1)
    x2 = ((-b) + Dsqrt) / (2 * a )
    print(x2)
