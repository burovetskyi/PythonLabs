result = 0
for i in range(5):
    print('Введіть число:')
    a = int(input())
    if a % 2 != 0:
        result += a
print(result)
