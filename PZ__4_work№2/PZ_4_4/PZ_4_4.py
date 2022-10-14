while True:
    try:
        n = int(input('Введите любое число (Это нахождение факториала): '))
        if n <= 1:
            print('Ошибка введённое число должно быть больше 1!')
            continue
        number_1 = 1
        while n:
            number_1 *= n
            n -= 1
        print(number_1)
        break
    except Exception:
        print('Ошибка!')
        continue