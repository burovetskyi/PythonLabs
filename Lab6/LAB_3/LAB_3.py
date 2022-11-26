import pickle
f = open(r"F:\mt-31-2022\LAB_6\LAB_2\text.txt", "r")
fr = f.read()
f.close()

f = open(r"F:\mt-31-2022\LAB_6\LAB_2\fist.txt", "r")
fr1 = f.read()
f.close()

f = open(r"F:\mt-31-2022\LAB_6\LAB_2\second.txt", "r")
fr2 = f.read()
f.close()

value = {"text.txt": fr, 
    "fist.txt": fr1, 
    "second.txt": fr2}
print("Dictionary:\n", value)

s = open(r"dict.pickle", "wb")
pickle.dump(value, s)

s = open(r"dict.pickle", "rb")
b = pickle.load(s)
print(b)
