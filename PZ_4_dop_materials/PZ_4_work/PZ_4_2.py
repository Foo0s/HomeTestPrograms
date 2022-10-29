try:
    number_1 = int(input('Введите первое число: '))
    number_2 = int(input('Введите второе число: '))
    number_3 = int(input('Введите третье число: '))
    number_4 = int(input('Введите четвёртое число: '))
    box = 0
    if number_1 % 2 == 0:
        box += 1
    if number_2 % 2 == 0:
        box += 1
    if number_3 % 2 == 0:
        box += 1
    if number_4 % 2 == 0:
        box += 1
    print(f'Количество чётных чисел: {box}')
except Exception:
    print('Error')