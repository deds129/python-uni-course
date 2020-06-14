#Задание 1
print(" 8.1 Дано имя файла и целые положительные числа N и K. Создать текстовый файл с указанным именем и записать в него N строк, каждая из которых состоит из K символов «*» (звездочка).")

Name=input("Введите имя файла: ")
Name=Name+".txt"
N = int(input("Количество строк: "))
K = int(input("Количество символов * в строке: "))
SS = open(Name, 'w')
for i in range(N):
    SS.write('*'*K + '\n')
SS.close()
print("Файл успешно создан")


#Задание 2
print(" 8.2 Дано имя файла и целое число N (0 < N < 27). Создать текстовый файл с указанным именем")
print("и записать в него N строк: первая строка должна содержать строчную (то есть маленькую) латинскую букву «a»,")
print("вторая — буквы «ab», третья — буквы «abc» и т. д.; последняя строка должна содержать N начальных строчных латинских букв в алфавитном порядке")

Name=input("Введите имя файла: ")
Name=Name+".txt"
f = open(Name, 'w')
N = int(input('   Введите кол-во строк 1-26: '))
a = 'abcdefghijklmnopqrstuvwxyz'
import string
for j in range(N):
    for i in range(j+1):
        s = ''+ a[i]
        f.write(s)
    f.write('\n')
f.close()
print("Файл успешно создан")


#Задание 3
print(" 8.3 Дана строка S и текстовый файл. Добавить строку S в конец файла.")

Name=input("Введите имя файла: ")
Name=Name+".txt"
SS = open(Name, 'a')
s = str(input("Введите строку для добавления: "))
SS.write("\n")
SS.write(s)
SS.close()
print("Строка успешно добавлена")


#Задание 4
print(" 8.4 Даны два текстовых файла. Добавить в конец первого файла содержимое второго файла.")

Name1=input("Введите имя первого файла: ")
Name1=Name1+".txt"
Name2=input("Введите имя второго файла: ")
Name2=Name2+".txt"
S1 = open( Name1, 'a')
S2 = open( Name2, 'r')
S1.write("\n")
S1.write(S2.read())
S1.close()
S2.close()
print("Содержимое файла скопировано!")


# Задание 5
print(" 8.5 Дана строка S и текстовый файл. Добавить строку S в начало файла.")

Name=input("Введите имя файла: ")
Name=Name+".txt"
SS = open(Name, 'a')
s = str(input("Введите строку для добавления: "))
SS.write(s)
SS.write("\n")
SS.close()
print("Строка успешно добавлена")



#Задание 6
print(" 8.6 Дано целое число K и текстовый файл. Вставить пустую строку перед строкой файла с номером K. Если строки с таким номером нет, то оставить файл без изменений.")

Name=input("Введите имя файла: ")
Name=Name+".txt"
k = int(input("Введите номер строки: "))
f = open(Name, 'r+')
file = open('вспомогательный.txt', 'a')
for line in open(Name).readlines()[:k-1]:
    file.write(line.strip()+'\n')
for line in open(Name).readlines()[k-1:]:
    file.write('\n'+line.strip())
file.close()
f.close()
f = open(Name, 'w')
file = open('вспомогательный.txt' , 'r+')
f.write(file.read())
file.close()
import os
os.remove('вспомогательный.txt')
f.close()
print("Задание выполнено")


#Задание 7
print(" 8.7 Дан текстовый файл. Продублировать в нем все пустые строки.")

Name=input("Введите имя файла: ")
Name=Name+".txt"
f = open( Name, 'r')
lines = f.readlines()
f.close()
f = open( Name, 'w')
for line in lines:
    f.write(line)
    if not line.strip():
        f.write('\n')
f.close()
print("Пустые строки продублированы")


#Задание 8
print(" 8.8 Дана строка S и текстовый файл. Заменить в файле все пустые строки на строку S.")

Name=input("Введите имя файла: ")
Name=Name+".txt"
f = open( Name, 'r')
s = input("Введите строку: ")
lines = f.readlines()
f.close()
f = open(Name, 'w')
for line in lines:
    if not line.strip():
        f.write(s)
    f.write(line)
f.close()
print("Пустые строки изменены")


#Задание 9
print(" 8.9 Дан непустой текстовый файл. Удалить из него первую строку")

Name=input("Введите имя файла: ")
Name=Name+".txt"
f = open( Name, 'r+')
for line in open(Name).readlines()[1:]:
    f.write(line.strip()+'\n')
f.close()
print("Строка удалена")


#Задание 10
print(" 8.10 Дан непустой текстовый файл. Удалить из него последнюю строку.")

Name=input("Введите имя файла: ")
Name=Name+".txt"
f = open( Name, 'r', encoding='utf-8')
lines = f.readlines()
n = len(lines)
f.close()
f = open( Name, 'w', encoding='utf-8')
i=0
while i<n-1:
    f.write(lines[i])
    i+=1
f.close()
print("Строка удалена")


#Задание 11
print(" 8.11 Дан текстовый файл. Заменить в нем все подряд идущие пробелы на один пробел.")

Name=input("Введите имя файла: ")
Name=Name+".txt"
f = open( Name, 'w')
f.write("тут      введен  текст   с пробелами \n что   бы   посмотреть   их   удаление")
f.close()
f = open( Name, 'r')
a = str(f.read())
a = a.split(' ')
n = 0
while n < len(a):
    if a[n] == '':
        del a[n]
    else:
        n += 1
a = ' '.join(a)
f.close()
f = open( Name, 'w')
f.write(a)
f.close()
print("Лишние пробелы удалены")


#Задание 12
print(" 8.12 Дан текстовый файл, содержащий более трех строк. Удалить из него последние три строки.")

Name=input("Введите имя файла: ")
Name=Name+".txt"
f = open( Name, 'r', encoding='utf-8')
lines = f.readlines()
n = len(lines)
f.close()
f = open( Name, 'w', encoding='utf-8')
i=0
while i<n-3:
    f.write(lines[i])
    i+=1
f.close()
print("Строки удалены")


#Задание 13
print(" 8.13 Дан текстовый файл. Найти количество абзацев в тексте, если абзацы отделяются друг от друга одной или несколькими пустыми строками.")

Name=input("Введите имя файла: ")
Name=Name+".txt"
f = open( Name, 'r')
lines = f.readlines()
n = len(lines)
f.close()
i=0; k=0
while i<n:
    t=0
    while not lines[i].strip():
        t+=1
        i+=1
    if t!=0:
        k+=1
    i+=1
k+=1
print("Количество абзацев: ",k)



# Задание 14

print('')
print(" 8.14. Дано целое число K и текстовый файл. Удалить из файла абзац с номером K (абзацы отделяются друг от друга одной или несколькими пустыми строками).")
print("Пустые строки, предшествующие и следующие за удаляемым абзацем, не удалять. Если абзац с данным номером отсутствует, то оставить файл без изменений.")

k = int(input('   Введите номер абзаца для удаления: '))
f = open('f1.txt', 'r+', encoding='utf-8')
for line in open('f1.txt').readlines()[:k-1]:
    f.write(line.strip()+'\n')
for line in open('f1.txt').readlines()[k:]:
    f.write('\n'+line.strip())
f.close()
print('Сделано!')


#Задание 15
print(" 8.15 Дан текстовый файл. Найти количество абзацев в тексте, если первая строка каждого абзаца начинается с 5 пробелов («красная строка»). Пустые строки между абзацами не учитывать.")

Name=input("Введите имя файла: ")
Name=Name+".txt"
f = open( Name, 'r')
k=0
lines = f.readlines()
n = len(lines)
i=0; h=""
while i<n:
    if len(lines[i])>5:
        h=lines[i][0]+lines[i][1]+lines[i][2]+lines[i][3]+lines[i][4]
        if h=="     ":
            k+=1
    i+=1
print("Количество абзацев: ",k)


# Задание 16

print('')
print(" 8.16. Дан текстовый файл, содержащий текст, выровненный по левому краю. Выровнять текст по правому краю, добавив в начало каждой непустой строки нужное количество пробелов (ширину текста считать равной 50).")

import textwrap 
print('   До:')
print(open('f1.txt', encoding='utf-8').read())
with open('f1.txt','r+',encoding='utf-8') as f:
    text = f.read()
    f.seek(0)
    for line in text.splitlines():
        f.write("{:>50}".format(line) +'\n') 
print('   После:')
print(open('f1.txt', encoding='utf-8').read())

# Задание 17

print('')
print(" 8.17. Дан текстовый файл, содержащий текст, выровненный по левому краю.")
print("Выровнять текст по центру, добавив в начало каждой непустой строки нужное количество")
print("пробелов (ширину текста считать равной 50). Строки нечетной длины перед центрированием дополнять слева пробелом.")
lines = map(str.strip, open('f2.txt', encoding='utf-8'))
a = '\n'.join((' ' * (25 - (len(line)//2)) if line else line) + line for line in lines)
f = open('f2.txt', 'w')
f.write(a)
f.close()
print(a)

# Задание 18

print('')
print(" 8.18. Дан текстовый файл, содержащий текст, выровненный по правому краю.")
print("Выровнять текст по центру, удалив из каждой непустой строки половину начальных пробелов.")
print("В строках с нечетным количеством начальных пробелов перед центрированием удалять первый начальный пробел.")
      
lines = map(str.strip, open('f1.txt', encoding='utf-8'))
a = '\n'.join((' ' * (25 - (len(line)//2)) if line else line) + line for line in lines)
f = open('f1.txt', 'w')
f.write(a)
f.close()
print(a)


































