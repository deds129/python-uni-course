import math
import random
# Практическая работа №6.1
# 1
print(
    "1.Напишите функцию, поиска факториала числа, не используя встроенные методы. В основной программе пользователь осуществляет ввод числа n.")
def factor(n):
    fact = 1;
    if n == 0:
        print("Факториал числа n= ", fact)
    else:
        while n > 1:
            fact *= n
            n -= 1
    print("Факториал числа n= ", fact)
n = int(input('Введите число n = '))
factor(n)

#2
print("2.Напишите функцию, поиска min числа, не используя встроенные методы. В основной программе пользователь осу")
def minimum():
    min_el = 1.7976931348623157e+308
    x = input("Введите число ряда: ")
    try:
        x = float(x)
        flag = True
    except ValueError:
        flag = False
    while flag == True:
        if x < min_el:
            min_el = x
        x = input("Введите число ряда: ")
        try:
            x = float(x)
            flag = True
        except ValueError:
            flag = False
    if min_el == 1.7976931348623157e+308:
        print("Неверный формат числа")
        return
    return  min_el
print("Минимальное число ряда = ",minimum())

# 3
print(
    "3. Напишите функцию, требующую у пользователя ввести корректные данные целого числа, пока он их не введет правильно, либо не наберет «stop». ")
def dec():
    while 1:
        num = input("Введите число ")
        try:
            if num == "stop":
                break
            num = int(num)
            break

        except ValueError:
            print('Некорректный ввод, повторите попытку!')
dec()

# 4
print(
    "4.Напишите функцию, циклически заполняющую список данными, пока пользователь не вводит «stop». В основной программе данная последовательность выводится на печать.")
def inputter():
    data = []
    temp = input("Вводите данные ")
    while temp != "stop":
        data.append(temp)
        temp = input()
    return data
data = inputter()
print("Введенный список:")
for a in data:
    print(a + " ")

# 5
print(
    "5. Напишите функцию, циклически заполняющую словарь данными, пока пользователь не вводит «stop». В основной программе данная последовательность выводится на печать.")
def dic():
    d = {}
    k = input('Введите ключ: ')
    d[k] = input('Введите значение: ')

    while (d[k] != "stop") and (k != "stop"):
        k = input('Введите ключ: ')
        d[k] = input('Введите значение: ')
    #del d['stop']
    d.pop("stop")
    return d
dict = dic()
print(dict)

#6
print("6. Дополнить Пример 15 из лекции корректной обработкой всех исключений (см. рис ниже). ")
try:
    n=input('Введите целое число 1 ')
    n=int(n)
except ValueError:
    print("Некоррекстный ввод числа")
    try:
        3/0
    except ZeroDivisionError:
        print("Ошибка! Деление на ноль")
else:
    print("Было введено целое число")
finally:
    print("Конец программы")