try:
    number_1 = int(input('Введите первое число: '))
    number_2 = int(input('Введите второе число: '))
    number_3 = int(input('Введите третье число: '))
    number_4 = int(input('Введите четвёртое число: '))
    box = 0
    if number_1 < 0 or number_2 < 0 or number_3 < 0 or number_4 < 0:
        if number_1 < 0:
            box += 1
        if number_2 < 0:
            box += 1
        if number_3 < 0:
            box += 1
        if number_4 < 0:
            box += 1
    print(f'Количество отрицательных чисел: {box}')
    print(number_3 + number_4 + number_2 + number_1)
except Exception:
    print('Error')