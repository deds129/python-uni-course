import math
#ЛАБОРАТОРНАЯ РАБОТА №6
#1
print("Задача №1")
def Swap(x,y):
    el=x
    x=y
    y=el
    return x,y
a=input("Введите A: ")
b=input("Введите B: ")
c=input("Введите C: ")
d=input("Введите D: ")
a,b=Swap(a,b)
print("a:",a,"b:", b)

c,d=Swap(c,d)
print("c:",c,"d:",d)

b,c=Swap(b,c)
print("b:",b,"c:",c)
print("")

#2
print("Задача №2")
def concat(a,b):
        str1 = str(a) + str(b)
        return str1
a= str(input("Введите строку №1: "))
b= str(input("Введите строку №2: "))
a=concat(a,b)
print(a)
print("")

#3
print("Задача №3")
def mult():
    x = float(input("Вводите числа "))
    if x==0:
        return 0
    pr=1;
    while x != 0:
        pr*=x
        x=float(input())
    return  pr
print("Произведение чисел= ",mult())
print("")

#4
print("Задача №4")
def getInput():
    x = str(input("Введите строку: "))
    return x
x=getInput()
print("Введенная строка:",x)
print("")

#5
print("Задача №5")
def testInput(x):
    try:
        x = int(x)
        return True
    except:
        return False
x=input('Введите данные: ')
print(testInput(x))
print("")

#6
print("Задача №6")
def strToInt(el):
    try:
        el = int(el)
        return el
    except:
        print("Преобразование невозможно!")
x=input('Введите данные: ')
x = strToInt(x)
print(x)
print("")

#7
print("Задача №7")
def printInt(x):
    print(x)
x=int(input('Введите число: '))
printInt(x)
print("")

#8
print("Задача №8")
while 1:
    c = int(input("Введите код символа: "))
    if c==0: break
    print(chr(c))
print("")

#9
print("Задача №9")
n = str (input ("Введите строку "))
if (len(n) > 10):
    print ("Warning! ")
elif (len(n) == 10):
    print ("Длинна строки соответствует условиям ")
else:
    a = 10 - len(n)
    print (n + '*' * a)
print("")

#10
print("Задача №10")
i=1
a= float(input('Введите вещественное число: '))
min=max=a
while i<6:
    b= float(input('Введите вещественное число: '))
    if min>b:
        min=b
    if max<b:
        max=b
    i+=1
print ('Максимум: ' +str(round(max,2))  + '\n'+ 'Минимум: ' + str(round(min,2)))
print("")

#11
print("Задача №11")
def test():
    int_x = int(input('Введите целое число: '))
    if int_x > 0:
        positive()
    else:
        negative()
def positive():
    print('Положительное')
def negative():
    print('Отрицательное')
test()
print("")

#12
print("Задача №12")
pl_kryga = 0
pl_bok_poverhn_cyl = 0

def cylinder():
    figure = input('Что вы хотите вычислить? 1-площадь бок. поверхн. или 2 - площадь цилиндра: ')
    r = float(input('Ввдите параметр r: '))
    h = float(input('Введите параметр h: '))
    def circle():
        global pl_kryga
        pl_kryga = 3.14 * r ** 2

    def bok_poverhn_cyl():
        global pl_bok_poverhn_cyl
        pl_bok_poverhn_cyl = 2 * 3.14 * r * h

    def plosh_cylindra():
        circle()
        bok_poverhn_cyl()
        pl_cylindra = 2 * pl_kryga + pl_bok_poverhn_cyl
        print('Площадь цилиндра равна: ' + str(pl_cylindra))

    if figure == '1':
        bok_poverhn_cyl()
        print('Площадь боковой поверхности цилиндра = ' + str(pl_bok_poverhn_cyl))
    elif figure == '2':
        plosh_cylindra()
cylinder()
print("")

#13
print("Задача №13")
def TimetoHMS(T):
    H = int(T / 3600)
    M = int(T % 3600 / 60)
    S = int(T - H * 3600 - M * 60)
    return H,M,S
for i in range(5):
    T = int(input("Введите T: "))
    H,M,S=TimetoHMS(T)
    print('часы: ', H)
    print('минуты: ', M)
    print('секунды: ', S)
print("")

#14
print("Задача №14")
def isLeapYear(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False
year = int(input('Введите год: '))
print(isLeapYear(year))
print("")

#15
print("Задача №15")
def ShiftRight3(a,b,c):
    t=c
    c=b
    b=a
    a=t
    return a,b,c
a1=input('Введите A1 ')
b1=input('Введите B1 ')
c1=input('Введите C1 ')
a1,b1,c1 = ShiftRight3(a1,b1,c1)
print('Результат: ',a1,' ',b1,' ',c1)

a2=input('Введите A2 ')
b2=input('Введите B2 ')
c2=input('Введите C2 ')
a2,b2,c2 = ShiftRight3(a2,b2,c2)
print('Результат: ',a2,' ',b2,' ',c2)
print("")
