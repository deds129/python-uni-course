import math

print("Практическая Работа №4.2" + '\n')
print("1.Дано число. Увеличьте его на 30%, на 120%.")
num1 = float(input('Введите число: '))
num2 = num1 + num1 * 0.3
num1 = num1 + num1 * 1.2
print("Число увеличенное на 30%: " + str(num2))
print("Число увеличенное на 120%: " + str(num1) + '\n')

print("2. Дано два числа. Найдите сумму 40% от первого числа и 84% от второго числа.")
num1 = float(input('Введите число 1: '))
num2 = float(input('Введите число 2: '))
num1 = num1 * 0.4
num2 = num2 * 0.84
sum = num1 + num2
print("Cумма чисел = " + str(sum) + '\n')

print(
    "3. Дан номер месяца. Вывести название поры года (весна, лето и так далее) или слово 'Ошибка', если месяца с таким номером не существует.")
num1 = float(input('Введите номер месяца: '))
if (num1 == 12 or num1 == 1 or num1 == 2):
    print("Зима" + '\n')
elif (num1 == 3 or num1 == 4 or num1 == 5):
    print("Весна" + '\n')
elif (num1 == 6 or num1 == 7 or num1 == 8):
    print("Лето" + '\n')
elif (num1 == 9 or num1 == 10 or num1 == 11):
    print("Осень" + '\n')
else:
    print("Ошибка!" + '\n')

print(
    "4. Пользователь вводит три действительных числа. Определить, существует ли треугольник с длинами сторон, равными этим числам. Если да, то определить, является ли данный треугольник остроугольным. ")
num1 = float(input('Введите сторону 1: '))
num2 = float(input('Введите сторону 2: '))
num3 = float(input('Введите сторону 3: '))
if (num1 >= num2 + num3) or (num2 >= num1 + num3) or (num3 >= num2 + num1):
    print("Треугольника с данными длиннами сторон не существует")

else:
    print("Треугольника с данными длиннами сторон  существует")
    if num1 > num2:
        mx = num1
    else:
     mx = num2
    if (num3 > mx):
     mx = num3

    if num1 < num2:
        mn = num1
    else:
     mn = num2
    if num3 < mn:
        mn = num3
    sr = num1 + num2 + num3 - mn - mx
    if math.sqrt(mn) + math.sqrt(sr) > math.sqrt(mx):
        print("Треугольник остроугольный " + '\n')
    else:
        print("Треугольник не остроугольный" + '\n')

print("5. Найти приблизительное значения числа e с помощью формулы e=1+11!+12!+13!+...")
print("Приблизительное значение числа e" + str(round(math.e,2)) + '\n')

print("6. Напишите программу, которая определяет, можно ли из четырех отрезков с данными длинами a, b, c и d составить прямоугольник.")
n1 = float(input('Введите сторону 1: '))
n2 = float(input('Введите сторону 2: '))
n3 = float(input('Введите сторону 3: '))
n4 = float(input('Введите сторону 4: '))
if ((n1==n2) and (n3==n4)) or ((n1==n3) and (n2==n4)) or((n1==n4)or(n2==n3)):
    print("прямоугольник составить можно" + '\n')
else:
    print("прямоугольник составить нельзя" + '\n')

print("7. Два нечетных простых числа, отличающиеся на 2, называются близнецами. Например, числа 5 и 7. Напишите программу, которая будет находить все числа-близнецы на отрезке [2; 1000].")
def fact(x):
    if x<2:
        f = False
    elif x==2:
        f= True
    elif (x%2)==0:
        f=False
    else:
        f =True
        y=3
        while(y**2<=x) and (f==True):
            if(x%y)==0:
                f=False
            else:
                y=y+2

    return f
for i in range(2,998):
    if fact(i) and (fact(i+2)):
        print(str(i) + " " + str(i+2))

print("")
print("8. Напишите программу для сокращения дроби, сложения,вычитания, умножения и деления двух дробей.")

def NOD(a,b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a

    nod = a + b
    return nod
def NOK(a,b):
    nok=a*b/NOD(a,b)
    return nok
def SOKR(ch1,zn1):
    x =NOD(zn1,ch1)
    n=(int)(zn1/x)
    m=(int)(ch1/x)
    if(n==1):
         print("Сокращенная дробь: " + str(m))
    else:
        print("Сокращенная дробь: "  + str(m)+ "/"+str(n) + '\n')


flag =int(input('[1] - сократить дробь [2] - действия с дробями '))
if flag==1:
    ch1 = float(input('Введите числитель  дроби: '))
    zn1 = float(input('Введите знаменатель  дроби: '))
    SOKR(ch1,zn1)
elif flag ==2:
    ch1 = float(input('Введите числитель 1 дроби: '))
    zn1 = float(input('Введите знаменатель 1 дроби: '))
    ch2 = float(input('Введите числитель 2 дроби: '))
    zn2 = float(input('Введите знаменатель 2 дроби: '))
    deist = str(input('введите знак операции '))
    if(deist=="*"):
        ch3 = ch1*ch2
        zn3=zn1*zn2
        SOKR(ch3,zn3)
    elif(deist=="/"):
        ch3=ch1*zn2
        zn3=zn1*ch2
        SOKR(ch3,zn3)
    elif (deist=="+"):
        ch3 = (ch1*zn2)+(ch2*zn1)
        zn3=zn1*zn2
        SOKR(ch3,zn3)
    elif (deist=="-"):
        ch3 = (ch1*zn2)-(ch2*zn1)
        zn3=zn1*zn2
        SOKR(ch3,zn3)
    else:
        print("вы ввели неправильный знак операции")
else:
    print("ошибка выбора опции")

print("9. На поверхности планеты, являющейся шаром с радиусом R, заданы две точки своими широтой и долготой. Найти минимальную длину пути по поверхности этой планеты из одной точки в другую.")
radius = float(input('Введите радиус планеты: '))
lon1 = float(input('Введите долготу 1: '))
lat1 = float(input('Введите широту 1: '))
lon2 = float(input('Введите долготу 2: '))
lat2 = float(input('Введите широту 2: '))
T = math.acos(math.sin(lat1)*math.sin(lat2) + math.cos(lat1)*math.cos(lat2)*math.cos(math.fabs(lon1-lon2)))
rast = radius*T
print("Минимальная длинна пути = " + str(rast))






