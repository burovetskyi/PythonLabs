import os
text = 'This is very cool\ntwo lines text'
f = open('text.txt', 'w')
f.write(text)
f.close()
file_rozmir = os.stat('text.txt')
print(f'rozmir v bytes: {file_rozmir.st_size}')
my_list = text.split('\n')
x = open('fist.txt', 'w')
x.write(my_list[0])
x.close()
s = open('second.txt', 'w')
s.write(my_list[1])
s.close()



