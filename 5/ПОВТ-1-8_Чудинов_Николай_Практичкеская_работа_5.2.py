import math
import random

#5.2  Задачи числовые значения
#5.2.1
print("Для данного x вычислить значение функции")
x = int(input("Введите x: "))
if(x<=-1):
    y=1/(x**2)
elif(x>-1 and x<=2):
    y=x**2
else: y=4
print("y= ",y)
#5.2.2
print(" Даны действительные числа x, y вычислите u, ult u=3z^2-2z+5")
x = int(input("Введите x: "))
y = int(input("Введите y: "))
if(x+y<2):
    z=math.abs(x ** 2 + y ** 2)
elif (x+y==3)or(x+y==8):
    z=2*x*y
elif (x+y>=10):
    z=x-y
else:
    z=2*x+3*y
u=3*z**2-2*z+5
print("u=",u)

#5.2.3
print("Найти все натуральные числа до 200, сумма которых равна 13.")
for i in range(40,200):
    n=i
    s=0
    while n>0:
        s=s+n%10
        n=n//10
    if s==13:
        print(i)
#5.2.4
print("Дано трехзначное натуральное число. Вычислить произведение ненулевых цифр этого числа.")
trehzach  = int(input("Введите трехзначное число: "))
mult=1
a = int(trehzach/100)
c = int(trehzach/10%10)
b=int(trehzach%10)
if (a!=0):
    mult*=a
if (c!=0):
    mult*=c
if(b!=0):
    mult*=b
print("Призведение ненулевый цифр трехзначного числа= ", mult)
#5.2.5
print(" Дано натуральное число n. Вычислить произведение и количество нечетных цифр числа. ")
n = int(input("Введите натуральное  число n: "))
count = 0
mult = 1
while n > 0:
    digit = n % 10
    if digit%2==1:
        mult *= digit
        count += 1
    n = n // 10
print("Произведение нечетных цифр= ",mult,"их количество= ",count)
#5.2.6
print(" Дано трехзначное натуральное число n. Имеется ли в нем цифра 1?")
trehzach  = int(input("Введите трехзначное число: "))
a = int(trehzach/100)
c = int(trehzach/10%10)
b=int(trehzach%10)
if (a==1 or c==1 or b==1):
    print("В числе содержится цифра 1")
else:
    print("В числе не содержится цифра 1")
#5.2.7
print("Дано натуральное число n. Сколько цифр в числе n?")
n=input("Введите число n ")
print("В числе ",len(n)," цифр(ы)")
#5.2.8
print("Дано неотрицательное число М. Сколько первых натуральных чисел нужно взять, чтобы сумма их квадратов стала больше или равно М?")
m = int(input('Введите неотрицательное число M: '))
counter=0
n=1
summ=0
while summ < m:
    summ = (n*(n+1)*(2*n+1))/6
    n+=1
    counter+=1
print("Нужно взять ",counter," первых чисел")
#5.2.9
print(" Определить сумму всех нечетных чисел от 1 до 99. ")
sum=0
for i in range(1,99):
    if i%2==1:
        sum+=i;
print(sum)
#5.2.10
print("Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь. ")
trehzach  = float(input("Введите трехзначное число: "))
a = trehzach/100
c = trehzach/10%10
b=trehzach%10
print("Cумма числе трехзначного числа= ",int(a+b+c),"Произведение цифр трехзначного числа= ", int(a*b*c))
#5.2.11
print("Написать программу, которая генерирует в указанных пользователем границах случайное целое число.")
n = int(input('Введите нижнюю границу разброса: '))
n1 = int(input('Введите верхнюю границу разброса: '))
print("Сгенерированное случайное число =",random.randint(n, n1))
