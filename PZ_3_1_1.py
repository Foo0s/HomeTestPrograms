while True:
    try:
        a,b = int(input('Введите первое число: ')), int(input('Введите второе число: '))
        if a * b < 0:
            print(a*b+8)
            break
        else:
            print(a*b*1.5)
            break
    except Exception:
        print('Ошибка. Введите верные данные')
        continue