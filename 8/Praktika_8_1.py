#Задание 1
print(" 8.1.1 Дана строка, содержащая полное имя файла (например, 'D:\WebServers\home\lestsite\www\myfile.txt'). Выделите из этой строки имя файла без расширения")
s = str('D:\WebServers\home\testsite\www\myfile.txt')
import os
a = os.path.basename(s)
a = os.path.splitext(a)[0]
print("Имя файла:", a)


#Задание 2
print(" 8.1.2 Пользователь вводит email. Осуществить проверку на корректность (длина больше восьми, присутствует символ @, после которого присутствует символ '.', между этими двумя символами есть хотя бы две буквы, оканчивается на 'ru', 'com', 'net' или 'by', символ '_' может встречаться только один раз, до символа @ могут быть только цифры, буквы и символ '_').")
from re import *
def PROVERKA(address):
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
    BBB = name.match(address)
    if (BBB)and(k1<2)and(k2>8):
        print("Корректный email", BBB.group())
    else:
        print("Некорретный email")
s = input("Введите email: ")
PROVERKA(s)


#Задание 3
print(" 8.1.3 Исключить из строки группы символов, расположенные между символами «/*», «*/» включая границы. Предполагается, что нет вложенных скобок.")
s = 'Возможно последнее слово /* удалиться! удалиться! */было лишним'
print(" Исходная строка: ",s)
a = ('/*','*/')
print(" Новая строка: ",s[:s.find(a[0])]+s[s.rfind(a[1])+len(a[1]):])


#Задание 4
print(" 8.1.4 Определить является ли введенный текст записью целого числа, записью вещественного числа.")
n = input("Введите число: ")
try:
    int(n)
    print("Целое число")
except:
    try:
        float(n)
        print("Вещественное число")
    except ValueError:
        print("Не является числом")


#Задание 5
print(" 8.1.5 Удалить в строке все «лишние» пробелы, то есть из нескольких подряд идущих пробелов оставить только один.")
s = input("Введите строку:  ")
x = s.split()
x = ' '.join(x)
print("Новая строка: ",x)


#Задание 6
print(" 8.1.6 Дан текст. Заменить все email в этом тексте на '[email]'.")
print("Например, 'пишите мне на itmathrepetitor@gmail.ru по любому вопросу' преобразуется в 'пишите мне на [email] по любому вопросу'.")
s = 'пишите мне на itmathrepetitor@gmail.ru по любому вопросу'
print("Исходная строка: ", s)
x = s.split()
for i in range(len(x)):
    if ('@mail.ru' in x[i])or('@mail.com' in x[i])or('@mail.net' in x[i])or('@mail.by' in x[i]):
        x[i] = '[email]'
x = ' '.join(x)
print("Новая строка: ", x)


#Задание 7
print("8.1.7 Дан текст. Разбить его на строки (длина строк дана) так, чтобы разделение строк произошло на пробельном символе (если это невозможно, показать сообщение об ошибке) и строка равномерное дополнилась пробелами до необходимой длины.")
s = str(input("Введите текст: "))
s=s.split()
n=len(s)
d = int(input("Введите длину строки разбиения: "))
i=0; T=""; f=True; h=""
while i<n:
    if len(s[i])>d:
        f=False
        i=n
    else:
        h=s[i]
        i+=1
    while (i<n)and(len(h)!=d)and(f==True):
        while (i<n)and(len(h)+1+len(s[i])<=d):
            h=h+" "+s[i]
            i+=1
        if h!="":
            h=h+" "*(d-len(h))
        else:
            f=False
            i=n
    if f!=False:
        T+=h
    else:
        T=False
if T==False:
    print("   Ошибка!")
else:
    i=d
    while (i-d < len(T)):
        print(T[i-d:i])
        i += d


#Задание 8
print(" 8.1.8 Пользователь вводит пароль. Определите уровень сложности пароля (разработать алгоритм определения сложности по 10 балльной шкале).")
s = input("Введите пороль: ")
k1=0; k2=0; k3=0; k4=0; k5=0; k6=0; k7=0; k8=0; k9=0; k10=0 #критерии оценивания (можно посмотреть по каким критериям пороль не прошел, если вызвать соответствующие k)
if s=="":
    ball="Пороля нет"
else:
    ball = 0
    for i in range(len(s)): #содержаться цифры
        if s[i].isdigit():
            k1=1
            break
    for i in range(len(s)): #cодержаться символы нижнего регистра
        if s[i].islower():
            k2=1
            break
    for i in range(len(s)): #содержаться символы верхнего регистра
        if s[i].isupper():
            k3=1
            break
    for i in range(len(s)):
        if ('@'==s[i] or '#'==s[i] or '$'==s[i] or '%'==s[i] or '^'==s[i] or '&'==s[i]): #содержаться символы первого класса(символы клавишей с цифрами, когда строит английский язык)
            k4=1
            break
    for i in range(len(s)):
        if ('"'==s[i] or '№'==s[i] or ';'==s[i] or '%'==s[i] or ':'==s[i] or '?'==s[i]): #содержаться символы второго класса(символы клавишей с цифрами, когда строит русский язык)
            k5=1
            break
    for i in range(len(s)):
        if ('!'==s[i] or '`'==s[i] or '~'==s[i] or '*'==s[i] or '-'==s[i] or '='==s[i] or '+'==s[i]): #содержаться символы третьего класса (которые не меняются от переключения языка)
            k6=1
            break
    for i in range(len(s)):
        if ('|'==s[i] or '/'==s[i] or '{'==s[i] or '}'==s[i] or '['==s[i] or ']'==s[i] or '<'==s[i] or '>'==s[i] or '('==s[i] or ')'==s[i]): #содержаться палки и скобки
            k7=1
            break
    for i in range(len(s)):
        if (' ' in s[i]): #содержаться ли пробелы
            k8=1
            break
    if (len(s)>6): #длина больше 6
        k9=1
    if (s!="qwerty" or s!="12345677890" or s!="zxcvbn" or s!="password" or s!="пароль"): #Не является распространённым паролем
        k10=1
print(ball)



