def RectPS(x1, y1, x2, y2, P=None, S=None):
    x = abs(x1- x2)
    y = abs(y1 - y2)
    print(f'x -> {x}')
    print(f'y -> {y}')
    P = 2*(x+y)
    S = x*y
    print(f"Периметр равен: {P}")
    print(f"Площадь равна: {S}")

try:
    x_1 = int(input('Введите число для x1 координаты: '))
    x_2 = int(input('Введите число для x2 координаты: '))
    y_1 = int(input('Введите число для y1 координаты: '))
    y_2 = int(input('Введите число для y2 координаты: '))
except ValueError:
    print('Ошибка')
else:
    RectPS(x_1, y_1, x_2, y_2)
