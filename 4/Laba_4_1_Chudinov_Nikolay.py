print("3.1. Составить алгоритм вывода значений следующих чисел: 1 , 2 , 3 ... , 15.")
for i in range(1,16):
	print(i)

print("3.2. Составить алгоритм вывода значений следующих чисел: 2 , 4 , ..., 20 .")
for i in range(2,21,2):
	print(i)

print("3.3. Составить алгоритм вывода таблицы перевода перевода 1, 2,... 20 долларов США в рубли по текущему курсу (значение курса вводится произвольно). ")
z = int(input("Введите курс доллара://"))
for i in range(1,21):
	print("{0}$ = {1} руб".format(i,i*z))

print("3.4. Составить таблицу  вывода стоимости 2, 3, ..., 10 кг конфет (цена 1 кг конфет вводится произвольно).")
a = float(input("Введите цену за килограм конфет: "))
for i in range(2,11):
	print(" {0}  |  {1}".format(str(i),str(i*a)))

print("3.5. Найти сумму ста первых натуральных чисел.")
a = 0
for i in range(1,101):
	a+=i
print("Сумма ста первых  натуральных чисел = "  + str(a))

print("3.6. Составить блок-схему для нахождения среднего арифметического всех целых чисел от 1 до 100.")
for i in range(1,101):
	a+=i
b = a/100
print("Среднее арифметическое всех целых чисел от 1 до 100. "  + str(b))

print("3.7 Дано натуральное число n и k. Вычислите сумму от k до n: 1/k^5")
sum = 0
k = int(input("Введите k "))
n = int(input("Введите n "))
for i in range(k,n+1):
	sum = sum+(1/(i**5))
print("Сумма = " +str(sum))

print("3.8 Дано натуральное число n и k. Составьте блок-схему для вычисления суммы от k до n:(2k-1)/(k+1)")
k = int(input("Введите k:"))
summ = 0
n = int(input("Введите n:"))
for i in range(k,n+1):
	summ = summ+((2*i-1)/(i+1))
print("Сумма = " +str(summ))

print("3.9 Дано натуральное число n и k. Вычислите произведение n множителей:(1+1/k)")
k = int(input("Введите k "))
sum = 1
n = int(input("Введите n "))
for i in range(k,n+1):
	sum *= (1+1/i)
print("Сумма = " +str(summ))