import math
import random
#ЛАБОРАТОРНАЯ РАБОТА №6
#1
print("Задача №1")
n=int(input("Введите число элементов массива n: "))
mas=[]
for i in range(0, n):
    a = 0 if i % 2 == 0 else 1
    mas.append(a)
print(mas)
print("")

#2
print("Задача №2")
n=int(input("Введите число элементов массива n: "))
mas=[]
for i in range(0, n):
    a = i**2
    mas.append(a)
print(mas)
print("")

#3
print("Задача №3")
def sumNmult(mas:list):
    mult=1
    sum=0
    for i in mas:
        sum+=i
        mult*=i
    print("Cумма элементов списка = ",sum," произведение элементов списка = ",mult)

n=int(input("Введите число элементов массива n: "))
mas=[]
for i in range(0, n):
    a = float(input('Введите элемент массива '))
    mas.append(a)
print(mas)
sumNmult(mas)
print("")

#4
def ident(mas:list):
    for i in mas:
        if mas.count(i)>=2:
            print("В списке ЕСТЬ повторяющиеся элементы!")
            break
        else:
            print("В списке НЕТ повторяющихся элементов!")
            break
print("Задача №4")
n=int(input("Введите число элементов массива n: "))
mas=[]
for i in range(0, n):
    a = input('Введите элемент массива ')
    mas.append(a)
print(mas)
ident(mas)
print("")

#5
print("Задача №5")
def getIndex(array):
     imin = array.index(min(array))
     imax = array.index(max(array))
     if imin > imax:
            return imin, imax
     return imax, imin
def maxMinChange(mas:list):
    mas[getIndex(mas)[0]], mas[getIndex(mas)[1]] = mas[getIndex(mas)[1]], mas[getIndex(mas)[0]]
    return mas

n=int(input("Введите число элементов массива n: "))
mas=[]
for i in range(0, n):
    a = input('Введите элемент массива ')
    mas.append(a)
print(mas)
maxMinChange(mas)
print(mas)
print("")

#6
print("Задача №6")
n=int(input("Введите число элементов массива n: "))
mas=[]
for i in range(0, n):
    a = input('Введите элемент массива ')
    mas.append(a)
    mas = sorted(mas)
print(mas)

n=int(input("Введите число элементов массива n: "))
mas1=[]
for i in range(0, n):
    a = input('Введите элемент массива ')
    mas1.append(a)
n = 1
while n < len(mas1):
     for i in range(len(mas1)-n):
          if mas1[i] > mas1[i+1]:
               mas1[i],mas1[i+1] = mas1[i+1],mas1[i]
     n += 1
print(mas1)
print("")

#7
print("Задача №7")
def Hash(mas:list):
    for i in mas:
        if mas.count(i)>=2:
           mas.remove(i)
    return  mas

n=int(input("Введите число элементов массива n: "))
mas=[]
for i in range(0, n):
    a = input('Введите элемент массива ')
    mas.append(a)
print(mas)
mas =Hash(mas)
print(mas)
print("")
#8
print("Задача №8")
n=int(input("Введите число элементов массива n: "))
mas=[]
for i in range(0, n):
    a = input('Введите элемент массива ')
    mas.append(a)
    mas = sorted(mas)
print(mas)
print("")

n=int(input("Введите число элементов массива n: "))
mas1=[]
for i in range(0, n):
    a = input('Введите элемент массива ')
    mas1.append(a)
    mas1 = sorted(mas1)
print(mas1)
print("")

merge_list=mas+mas1
print(merge_list)
print("")
#9
print("Задача №9")
n=int(input("Введите число элементов массива n: "))
mas=[]
for i in range(0, n):
    a = int(input('Введите элемент массива '))
    mas.append(a)
print(mas)

for i in range(len(mas)):
    if mas[i]<0:
        mas.insert(i+1,0)
if mas[len(mas)-1]<0:
    mas.append(0)
print(mas)
print("")

#10
print("Задача №10")
n=int(input("Введите число элементов массива n: "))
mas=[]
for i in range(0, n):
    a = int(input('Введите элемент массива '))
    mas.append(a)
print(mas)
result = True
flag = False
for i in range(len(mas)-1):
    if(mas[i]>mas[i+1]):
        if(flag or mas[i]>mas[i+2]):
            result = False;
            break
        else:
            flag = True
print(result)
print("")

#11
print("Задача №11")
def sum(mas:list):
    sum = 0
    for i in mas:
        sum=+i
        return sum
def max(mas:list):
    max=mas[0]
    for i in mas:
        if i>max:
            max=i
    return max
def min(mas:list):
    min=mas[0]
    for i in mas:
        if i<min:
            min=i
    return min

mas=[]
for i in range(0, 8):
    a = int(input('Введите элемент массива '))
    mas.append(a)
print(mas)
print("")
print("Максимум списка = ",max(mas))
print("Минимум списка = ",min(mas))
print("Cумма элементов списка = ",sum(mas))
#12
print("Задача №12")
import random

count = 100
mas = []
while count != 0:
    mas.append(random.randint(0, 100))
    count -= 1


def prn(X):
    i = 0
    while i < len(X):
        print(X[i:i + 10])
        i += 10


prn(mas)
print('\n')
mas.sort()
prn(mas)
print("")

#13
print("Задача №13")
n=int(input("Введите число элементов массива n: "))
st=int(input("Введите начало диапазона: "))
fin=int(input("Введите конец диапазона: "))
mas=[]
i=0
while i<n:
    mas.append(random.randint(st,fin))
    i+=1
print(mas)
print("")

#14
print("Задача №14")
mas = list(range(0,100,17))
print (mas)
print("")

#15
print("Задача №15")
n=int(input("Введите число элементов массива n: "))
mas=[]
for i in range(0, n):
    a = int(input('Введите элемент массива '))
    mas.append(a)
print(mas)

counter=0
for i in mas:
    if i<0:
        counter+=1
print("Кол-во отрицательных элементов в списке= ", counter)
print("")

#16
print("Задача №16")
n=int(input("Введите число элементов массива n: "))
a = []
b = []

for items in range(0, n):
    words = input('Enter some words: ')
    b.append(len(words))
    a.append(words)
print(a)
print(b)
print("")