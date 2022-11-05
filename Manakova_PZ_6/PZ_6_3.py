import random

def rasstoyanie(x1, x2, y1, y2):
    R = (x2 - x1) + (y2 - y1)
    list_2.append(R)
try:
    B = []
    c = int(input('Введите размер списка: '))
    list_2 = []
    if c % 2 == 0:
        A = [random.randint(0, 100) for a in range(c)]
    else:
        print('Ошибка')

    a, b = int(input('Введите x координату для точки B: ')), int(input('Введите y координату для точки B: '))
    B.append(a)
    B.append(b)
    abscisya = []
    ordinati = []
    '''Цикл который добавляет в список значения абсцисс'''
    for i in A[0:-1:2]:
        abscisya.append(i)
    '''Цикл который добавляет в список значения ординат'''
    for number in A[1:-1:2]:
        ordinati.append(number)
    ordinati.append(A[-1])
except NameError:
    print('Ошибка')
except ValueError:
    print('Ошибка')
else:
    print('Количество всех точке по y в массиве A:', ordinati)
    print('Количество всех точке по x в массиве A:', abscisya)
    print('Массив A: ', A)
    print(f'Координаты точки B: x->{B[0]}, y->{B[1]}')
    i = 0
    while i < c // 2:
        x = abscisya[i]
        y = ordinati[i]
        i += 1
        rasstoyanie(B[0], x, B[1], y)
    else:
        i = 0
        while i < c // 2:
            x = abscisya[i]
            y = ordinati[i]
            if x - B[0] + y - B[1] == min(list_2):
                print(f"Список точек: {list_2}")
                print(f"Близжайшие точки к точке B это: x->{x}, y->{y}")
            i += 1
