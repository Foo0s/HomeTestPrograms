try:
    number_1, number_2 = int(input('Введите первое значение: ')), int(input('Введите второе значение: '))
    a = number_1 + number_2
    if a % 5 == 0:
        a = number_1 + number_2
        print(a + 1)
    else:
        a = number_1 + number_2
        print(a - 2)
except ValueError:
    print('Error')