s = input("vvedit persu stroky: ")
x = input("vvedit drugy stroky: ")

if len(s) > len(x):
    print("persha bilsha")
elif len(s) < len(x):
    print("dryga bilsha")
elif s == x:
    print("rivni i odnakovi")
elif len(s) == len(x):
    print("rivni")

