# Практическая работа 6.1
# Пример 27 - 28 .
print("Пример 27 - 28 .")
def countFood():
    a = int(input())
    b = int(input())
    print("Всего", a + b, "шт.")


print("Сколько бананов и ананасов для обезьян?")
countFood()
print("Сколько жуков и червей для ежей?")
countFood()
print("Сколько рыб и моллюсков для выдр?")
countFood()

# Пример 29:
print(" Пример 29: Пусть надо написать программу, вычисляющую площади разных фигур.")
def rectangle():  # функция вычисления площади прямоугольника
    a = float(input("Ширина: "))
    b = float(input("Высота: "))
    print("Площадь: %.2f" % (a * b))


def triangle():  # функция вычисления площади треугольника
    a = float(input("Основание: "))
    h = float(input("Высота: "))
    print("Площадь: %.2f" % (0.5 * a * h))


def circle():  # функция вычисления площади круга
    r = float(input("Радиус: "))
    print("Площадь: %.2f" % (3.14 * r ** 2))
figure = input("1-прямоугольник, 2-треугольник, 3-круг: ")
if figure == '1':
    rectangle()
elif figure == '2':
    triangle()
elif figure == '3':
    circle()
else:
    print("Ошибка ввода")
print("")


# Пример 30
print("Пример 30")
def rectangle():
    a = float(input("Ширина: "))
    b = float(input("Высота: "))
    print("Площадь: %.2f" % (a * b))


def triangle():
    a = float(input("Основание: "))
    h = float(input("Высота: "))
    print("Площадь: %.2f" % (0.5 * a * h))


figure = input("1-прямоугольник, 2-треугольник: ")
if figure == '1':
    rectangle()
elif figure == '2':
    triangle()
print("")
# Пример 31
print("Пример 31")
result = 0


def rectangle():
    a = float(input("Ширина: "))
    b = float(input("Высота: "))
    global result
    result = a * b


def triangle():
    a = float(input("Основание: "))
    h = float(input("Высота: "))
    global result
    result = 0.5 * a * h


figure = input("1-прямоугольник, 2-треугольник: ")
if figure == '1':
    rectangle()
elif figure == '2':
    triangle()
print("Площадь: %.2f" % result)
print("")


# Пример 32
print("Пример 32")
def cylinder():
    r = float(input())
    h = float(input())
    # площадь боковой поверхности цилиндра:
    side = 2 * 3.14 * r * h
    # площадь одного основания цилиндра:
    circle = 3.14 * r ** 2
    # полная площадь цилиндра:
    full = side + 2 * circle
    return full


square = cylinder()
print(square)
print("")
# Пример 33
print("Пример 33")
def cylinder():
    try:
        r = float(input())
        h = float(input())
    except ValueError:
        return
    side = 2 * 3.14 * r * h
    circle = 3.14 * r ** 2
    full = side + 2 * circle
    return full
print(cylinder())
print("")
# Пример 34
print("Пример 34")
def cylinder():
    r = float(input())
    h = float(input())
    side = 2 * 3.14 * r * h
    circle = 3.14 * r ** 2
    full = side + 2 * circle
    return side, full
sCyl, fCyl = cylinder()
print("Площадь боковой поверхности %.2f" % sCyl)
print("Полная площадь %.2f" % fCyl)
print("")
#Пример 35.
print("Пример 35.")
def cylinder(h, r=1):
    side = 2 * 3.14 * r * h
    circle = 3.14 * r ** 2
    full = side + 2 * circle
    return full
figure1 = cylinder(4, 3)
figure2 = cylinder(5)
print(figure1)  # figure1=131.88
print(figure2)
