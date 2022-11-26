import os

path="F:\mt-31-2022\LAB_6\LAB_1"

print("***Files***");
files = [f for f in os.listdir(path) if os.path.isfile(f)]
for f in files:
    print(f)

print("***Dir***");
files = [f for f in os.listdir(path) if os.path.isdir(f)]
for f in files:
    print(f)

print("***Dir and Files***");
files = os.listdir(path)
for f in files:
    print(f)
