#Пример 12
#a = 0
#print(a + b)
#Пример 12.1
#a = 0
#if a == 0:
 #   print(a)
  #  print(a + b)
#int("Hi")
#8 + "3"
#1/0
#Обработка исключений. Оператор try-except

sum = 0
n = 5
for i in range(1, n, 2):
    sum += i
print(sum)
#Пример 13
n = input("Введите целое число: ")
try:
    n = int(n)
    print("Удачно")
except:
    print("Что-то пошло не так")

try:
    a = float(input("Введите делимое: "))
    b = float(input("Введите делитель: "))
    c = a / b
    print("Частное: %.2f" % c)
except ValueError:
    print("Нельзя вводить строки")
except ZeroDivisionError:
    print("Нельзя делить на ноль")

#Пример 14.
try:
    n = input('Введите целое число: ')
    n = int(n)
except ValueError:
    print("Вы что-то попутали с вводом")
else: # выполняется, когда в блоке try не возникло исключения
    print("Все нормально. Вы ввели число", n)
finally: # выполняется в любом случае
    print("Конец программы")

#Пример 15.
try:
    n = input('Введите целое число: ')
    n = int(n)
except ValueError:
    print("Вы что-то попутали с вводом")
    3 / 0
except ZeroDivisionError:
    print("Деление на ноль")
else:
    print("Все нормально. Вы ввели число", n)
finally:
    print("Конец программы")

#Пример 24.
import random
print(random.random())
a = random.random()
print(a)
print(round(a, 2))
print(round(random.random(), 3))
print(random.random() * 10)
print(random.random() * (10 - 4) + 4)
#Пример 25.
import random
print(random.randint(0, 10))
print(random.randint(100, 200))
print(random.randrange(10, 20, 3))
#Пример 26.
print((random.random() * (1 + 1) - 1))
print(int(random.random() * 100))
print(int(random.random() * 100))
print(round(random.random() * 100 - 50)	)