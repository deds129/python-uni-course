import string
import random
from collections import Counter

# Практическая работа 8.2
#1
print("Задача №1")
def strChanger(str):
    str = str.replace('_',' ').title().replace(' ','')
    return str

str = input("Введите строку: ")
print(strChanger(str))
print("")

#2
print("Задача №2")
def converter(str):
    print("Как изменить строку?"+ '\n'+ "перевод всех символов в верхний регистр [1] "+
          '\n' +  "перевод всех символов в нижний регистр [2] " + '\n' +
        "перевод всех символов в нижний регистр и первых символов слов в верхний регистр [3] " +'\n'+
          "инвертирование регистра [4]" +  '\n' + "случайный регистр для каждого символа [5]")
    n = int(input("Введите номер операции "))
    if n==1:
        return str.upper()
    elif n==2:
        return str.lower()
    elif n == 3:
        return str.title()
    elif n == 4:
        return str.swapcase()
    elif n == 5:
        str2=''
        for a in str:
            str2 = str2+(random.choice(a.upper() + a.lower()))
        return str2
    else:
        print("Некорректный выбор функции")
        return str
str = input("Введите строку: ")
print(converter(str))
print("")
#3
print("Задача №3")
str = input("Введите строку: ")
print(str.title())
print("")

#4
print("Задача №4")
str = input("Введите строку: ")
res={}
res2={}
for keys in str:
    res[keys] = res.get(keys,0)+1
print("Частота повторения букв: ",res)

print("Частота повторения двубуквенных сочетаний: ",* sorted(Counter(zip(str, str[1:])).items()))
print("")

#5
print("Задача №5")
str = input("Введите текст: ")
str = str.lower()
tt = str.maketrans(dict.fromkeys(string.punctuation))
str = str.translate(tt)
list = []
list = str.split(" ")
counts=Counter(list)
print("Частота повторения слов" ,counts)
print("")

#6
print("Задача №6")
str = input('Введите текст: ').strip()
str += ' '
a = int(input('Введите максимально число слов в стоке: '))
c = 0
d = 1
j = 0
for i in range(len(str)):
    if str[i] == ' ':
        print(str[j:i], end = ' ')
        c += 1
        if c == d:
            print()
            d += 1
            c = 0
            if d == a + 1:
                d = 1
        j = i + 1

print("")