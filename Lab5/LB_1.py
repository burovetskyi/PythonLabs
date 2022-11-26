a = list(input())
Arr = []
print(a)
for j in a:
    if j not in Arr:
        Arr.append(j)
print("Nova stroka: " + str(Arr))
