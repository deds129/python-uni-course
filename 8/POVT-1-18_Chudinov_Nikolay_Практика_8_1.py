# Практическая работа 8.1
import os
import re


#1
#без использования регулярных выражений
print("Задача №1")
str = input("Введите полное имя файла ")
separator_index = str.index('.')
str = str[:separator_index]
str = os.path.basename(str)
print("Название файла: ",str)
#2
from re import *
def Check(address):
    k1=0; k2=0; i=0
    while i<len(address):
        if address[i]=="_":
            k+=1
        i+=1
    i=0
    while address[i]!="@":
        k2+=1
        i+=1
    name = compile('(^|\s)[-a-z0-9_{8,16}]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
    temp = name.match(address)
    if (temp)and(k1<2)and(k2>8):
        print("Корректный email")
    else:
        print("Некорретный email")
str = input("Введите email: ")
Check(str)

#3
print("Задача №3")
str = input("Введите строку ")
p = re.compile(r'\/\*.*?\*/')
new_str=re.sub(p,'',str)
print(new_str)
print("")

#4
print("Задача №4")
str = input("Введите строку ")
flag = True
if(str.isnumeric()):
    flag=True
else:
    flag=False
print(flag)
print("")

#5
print("Задача №5")
str = input("Введите строку ")
str=str.split()
new_str=' '.join(str)
print(new_str)
print("")

#6
print("Задача №6")
str = input("Введите строку ")
spl = str.split()
i=0
for el in spl:
    if('@' in el):
        spl[i]="[email]"
    i += 1
str=" ".join(spl)
print(str)
print("")

#7
print("Задача №7")
s = input('Введите текст: ')
n=int(input('Введите длину строки: '))
i=n
while(i-n<len(s)):
    print(s[i-n:i])
    i+=n
print("")


#8
def match(text, alphabet=set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')):
    return not alphabet.isdisjoint(text.lower())

print("Задача №8")
str = input("Введите пароль")
count=0
if(len(str)>6):
    count+=1
if(len(str)>12):
    count+=1
a=0
for i in str:
    if i.isdigit():
        a=2
count+=a

b=0
for i in str:
    if i.isupper():
        b=2
count+=b
bool = match(str)
if(bool):
    count+=2
special_char = False
for letter in str:
    if (not letter.isnumeric() and not letter.isdigit()):
        count+=2
        break
print("Надежность пароля = ",count,"/10")