import random 
num = random.randint(1, 9)
while True:
    a = int(input("vvedit chislo: "))
    if a != num:
        print("vvedit inshe") 
    else:
        print(num)
        break

