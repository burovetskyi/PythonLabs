f1 = f2 = 1
i=0
print(f1)
print(f2)
while i < 50:
    f1, f2 = f2, f1 + f2
    print(f2)
    i+=1


