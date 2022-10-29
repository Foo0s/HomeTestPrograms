try:
    number = int(input('Введите число: '))
    if number >= 3:
        n_1 = 0
        n_2 = 1
        n_4 = 0
        n_5 = 0
        while n_4 <= number:
            n_3 = n_1 + n_2
            n_1 = n_2
            n_2 = n_3
            if n_3 % 2 == 0:
                print('Чётное число:', n_3)
                n_5 += 1
            n_4 += 1
        print('Количество чётных чисел: ', n_5)
    else:
        print('Error')
except Exception:
    print('Error')