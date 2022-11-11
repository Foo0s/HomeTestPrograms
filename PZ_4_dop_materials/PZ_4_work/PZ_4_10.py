number = int(input('Введите число: '))
number_x = 0
number_y = 1
i = 0
list_2 = []
id = 0
if number >= 3:
    while i < number:
        print(f'Числа Фибоначчи: {number_x}, {number_y}')
        number_x += number_y
        if number_x % 2 == 0:
            id += 1
        if number_y % 2 == 0:
            id += 1
        number_y += number_x
        i += 1
    print(f"Количество чётных чисел: {id}")


