import math
import random
import string
import datetime
import time
# Практическая работа №7.1
#1
print("Задача №1")
def largestWord(text:list):
    lword=''
    for word in text:
        if len(word)>len(lword):
            lword=word
    return lword

def commonWord(text:list):
    cword=''
    for word in text:
        if text.count(word) > text.count(cword):
            cword = text.pop(text.index(word))
    return  cword

text = input('Введите текст: ')
tt = str.maketrans(dict.fromkeys(string.punctuation))
new_text = text.translate(tt)

sl =new_text.split(' ')
largest_word = largestWord(sl)
common_word = commonWord(sl)
print(largest_word)
print(common_word)
print("")
#2
print("Задача №2")
int = int(input('Введите число: '))
num_str = str(int)
print("Целое число в виде строки",num_str)
print("")
#3
print("Задача №3")
def get_extension(filename):
    filename_parts = filename.split('.')
    if len(filename_parts) < 2:
        raise ValueError('файл не имеет расширения!')
    first, *middle, last = filename_parts
    if not last or not first and not middle:
        raise ValueError('файл не имеет расширения!')
    return filename_parts[-1]
filename = input('Введите название файла:')
print("Расширение файла: ",get_extension(filename))
print("")
#4
print("Задача №4")
string = str(input('Введите строку: '))
upper = 0
lower = 0
for i in string:
    if i.isupper():
        upper += 1
    else:
        lower += 1
if upper > lower:
    print(string.upper())
elif i.islower:
    print(string.lower())
print("")

#5
print("Задача №5")
sum=0
while True:
    num1 = input('Введите 1е число ')
    num2 = input('Введите 2е число ')
    if num1.isdigit() and num2.isdigit():
        sum = float(num1) + float(num2)
        print("Cумма чисел= ",sum)
        break
    else:
        print("Ошибка! одно переменные введены неправильно, попробуйте еще раз!")
print("")

#6
CONV_TABLE = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))

def arab_to_roman( number ):
   if number <= 0: return ''

   ret = ''
   for arab, roman in CONV_TABLE:
       while number >= arab:
           ret += roman
           number -= arab

   return ret

def roman_to_arab(txt):
    txt = txt.upper()
    ret = 0
    for arab, roman in CONV_TABLE:
        while txt.startswith( roman ):
            ret += arab
            txt = txt[ len( roman ): ]
    return ret

num = int(input('Введите число (араб): '))
print(arab_to_roman(num))
newNum = input('Введите число (рим): ')
print(roman_to_arab(newNum))
print("")
#7
print("Задача №7")
n=int(input("Введите кол-во городов: "))
mas=[]
for i in range(0, n):
    a = input('Введите название города ')
    mas.append(a)
    mas = sorted(mas)
print(mas)
print("")

#8
# 11-11-2011 11:11:11
data = input('Введите дату в формате: Дата-Месяц-Год Час:Мин:Сек: ')
try:
    day = int(data[:2])
    month = int(data[3:5])
    year = int(data[6:10])
    h = int(data[11:13])
    m = int(data[14:16])
    s = int(data[17:])
    if (day>31) or (month>12) or (h>23) or (m>59) or (s>59):
        raise Exception()
    else:
        print("Данные корректны")
except Exception as e:
    print("Ошибка! Некорректные данные")





