import math
import random
import string
import array
import re
#ЛАБОРАТОРНАЯ РАБОТА №8
#1
print("Задача №1")
filename = input('Введите имя файла: ')
N = int(input('Введите положительное целое число N: '))
K = int(input('Введите положительное целое число K: '))
list=[]
for i in range(N):
    list.append('*'*K)
with open(filename,"w") as file:
    for line in list:
        file.write(line+'\n')
print("")

#2
print("Задача №2")
filename = input('Введите имя файла: ')
N = int(input('Введите положительное целое число N (0 < N < 27): '))
list=[]
str=""
for i in range(N):
    str=str+string.ascii_lowercase[i]
    list.append(str)
with open(filename,"w") as file:
    for line in list:
        file.write(line+'\n')
print("")

#3
print("Задача №3")
filename = input('Введите имя файла: ')
S= input('Введите строку S: ')
with open(filename,"a") as file:
    file.write(S)
print("")

#4
print("Задача №4")
filename = input('Введите имя файла #1: ')
filename2 = input('Введите имя файла #2: ')
content=""
with open(filename2,"r") as file:
    content=file.read()

with open(filename,"a") as file:
    file.write(content)
print("")
#5
print("Задача №5")
filename = input('Введите имя файла: ')
S= input('Введите строку S: ')
with open(filename,"r") as file:
    content=file.read()
with open(filename,"w") as file:
    file.write(S+content)
print("")
print("")

#6
print("Задача №6")
filename = input('Введите имя файла: ')
k = int(input('Введите номер строки K: '))
k=k-1
list=[]
with open(filename, "r") as file:
    for line in file:
        list.append(line)
if len(list)>=k:
    list.insert(k,'\n')
with open(filename, "w") as file:
    for line in list:
        file.write(line)
print("")

#7
print("Задача №7")
filename = input('Введите имя файла: ')
list=[]
with open(filename, "r") as file:
    for line in file:
        list.append(line)
print(list)

b=[]
for i in list:
    if(i=='\n'):
        b.extend([i,i])
    else:
        b.extend([i])
with open(filename, "w") as file:
    for line in b:
        file.write(line)
print("")

#8
print("Задача №8")
filename = input('Введите имя файла: ')
S= str(input('Введите строку S: '))
S=S+'\n'
list=[]
with open(filename, "r") as file:
    for line in file:
        list.append(line)
b=[]
for i in list:
    if(i=='\n'):
        b.extend([S])
    else:
        b.extend([i])
with open(filename, "w") as file:
    for line in b:
        file.write(line)
print("")

#9
print("Задача №9")
filename = input('Введите имя файла: ')
with open(filename, 'r') as f:
    lines = f.readlines()

with open(filename, 'w') as f:
    f.writelines(lines[1:])
print("")

#10
print("Задача №10")
filename = input('Введите имя файла: ')
with open(filename, 'r') as f:
    lines = f.readlines()

with open(filename, 'w') as f:
    f.writelines(lines[0:len(lines)-1])
print("")

#11
print("Задача №11")
filename = input('Введите имя файла: ')
with open(filename, 'r') as f:
    content = f.read()
content=re.sub(r'\s+', ' ', content)
with open(filename, 'w') as f:
    f.write(content)
print("")

#12
print("Задача №12")
filename = input('Введите имя файла: ')
with open(filename, 'r') as f:
    lines = f.readlines()

with open(filename, 'w') as f:
    f.writelines(lines[0:len(lines)-3])
print("")

#13
print("Задача №13")
filename = input('Введите имя файла: ')
count=0
with open(filename, 'r') as f:
    content = f.read()
content=re.sub("\n\n+", "\n\n",content)
lines=[]
lines=content.split("\n")
for i in lines:
    if i=='':
        count+=1
print("В тексте %d абзацев(а)" %count)

#14
print("Задача №14")
filename = input('Введите имя файла: ')
k = int(input('Введите номер абзаца для удаления: '))
f = open(filename, 'r+')
for line in open(filename).readlines()[:k-1]:
    f.write(line.strip()+'\n')
for line in open(filename).readlines()[k:]:
    f.write('\n'+line.strip())
f.close()
print("")

#15
print("Задача №15")
filename = input('Введите имя файла: ')
with open(filename, 'r') as f:
    lines = f.readlines()
nn=0
for i in lines:
    if i[:5] == '     ' and i[5] != ' ' and i[5:] != '\n':
        nn += 1
print("В тексте %d абзацев(а)" %nn)
print("")

#16
print("Задача №16")
filename = input('Введите имя файла: ')
lines=[]
with open(filename,'r') as f:
    for line in f:
        c='{:>50}'.format(line.strip())
        lines.append(c)
print("")
with open(filename,'w') as f:
    for line in lines:
        f.write(line+'\n')
print("")

#17
print("Задача №17")
filename = input('Введите имя файла: ')
lines=[]
with open(filename,'r') as f:
    for line in f:
        c='{:^50}'.format(line.strip())
        lines.append(c)
print("")
with open(filename,'w') as f:
    for line in lines:
        f.write(line+'\n')
print("")

#18
print("Задача №18")
filename = input('Введите имя файла: ')
lines=[]
with open(filename,'r') as f:
    for line in f:
        c='{:^50}'.format(line.strip())
        lines.append(c)
print("")
with open(filename,'w') as f:
    for line in lines:
        f.write(line+'\n')