s = input("vvedit strichky ")
print("kilkist simvoliv")
print(len(s))
wordCount = 0

for word in s.split():
    if word.isalpha() == True:
        wordCount += 1

print('Kilkist sliv : \n' + str(wordCount))


