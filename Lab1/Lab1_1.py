print('Введіть сторону а')
a = int(input())
print('Введіть сторону b')
b = int(input())
if a == b:
    print('Це квадрат')
else:
    p = (a+b)*2
    S = a*b
    print('Перимтр прямокутника ', p)
    print('Площа прямокутника ', S)
