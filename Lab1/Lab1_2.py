print('Введіть число а:')
a = int(input())
print('Введіть число b:')
b = int(input())
if a % b == 0:
    print('а кратне b')
else:
    print('a не кратне b')
if b % a ==0:
    print('b кратне а')
else:
    print('b  не кратне а')
